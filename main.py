import requests
import os
from bs4 import BeautifulSoup
import random
import time
import threading
import re
import json
import cleantext
from flask import (
    Flask,
    jsonify,
    request,
)
from flask_cors import CORS
from dotenv import load_dotenv
import concurrent.futures
load_dotenv()
app = Flask(__name__)
CORS(app)
all_results = []
threads = []
future_list = []
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55"
]
# Lấy link GG từ GG_API
def get_google_search_results(query):
    api_key = os.getenv("API_KEY")
    cx = os.getenv("CX")
    base_url = "https://www.googleapis.com/customsearch/v1"

    params = {
        "q": query,
        "key": api_key,
        "cx": cx,
        "num": 10,
        "gl": "vn",
        "googlehost": "google.com.vn"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        items = data.get("items", [])
        urls = [item.get("link") for item in items]  
        return urls
    else:
        print(f"Error: {response.status_code}")
        return []
#Kiểm tra request có thành công không
def get_page_content(url):
    user_agent = random.choice(USER_AGENTS)
    headers = {"User-Agent": user_agent}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

def extract_text_from_webpage(url):
    page_content = get_page_content(url)
    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        text = soup.get_text()
        text = cleantext.clean_main(text)
        return text
    return None

def process_url_with_timeout(url):
        result = process_url(url)
        if result is not None:  
            all_results.append(result)
            
def process_url(url):
    content = extract_text_from_webpage(url)
    if content:
        result = {
            'url': url,
            'content': content
        }
        all_results.append(result)
@app.route('/api/search', methods=['POST'])
def search_and_save():
    data = request.get_json()
    if 'search_query' not in data:
        return jsonify({'error': 'Missing search_query in JSON data'}), 400

    search_query = data['search_query']
    search_results = get_google_search_results(search_query)
    # Tao luồng 
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for url in search_results:
            thread = executor.submit(process_url_with_timeout, url)
            future_list.append(thread) 

        # set thời gian chạy tối đa mỗi luồng
        completed, _ = concurrent.futures.wait(future_list, timeout=15)
        # Kiểm tra trạng thái của từng đối tượng Future
        # THông báo log trạng thái từng luồng URL hoàn thành hay ko
        for future in future_list:
            if future in completed:
                print(f"URL {future} đã hoàn thành.")  
            else:
                future.cancel()
                print(f"URL {future} không hoàn thành (bị hủy).")
    current_results = all_results.copy()
    all_results.clear()
    return jsonify(current_results)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9000)

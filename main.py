import requests
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
load_dotenv()
app = Flask(__name__)
CORS(app)
all_results = []
threads = []
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
        return text.strip()
    return None
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
    threads.clear()
    for url in search_results:
        thread = threading.Thread(target=process_url, args=(url,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    current_results = all_results.copy()
    all_results.clear()
    return jsonify(current_results) 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9000)

import requests
import os
import threading
import re
from flask import (
    Flask,
    jsonify,
    request,
)
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import requests
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
def get_content_summary_from_url(url, sentences_count=200):
    try:
        # Gửi yêu cầu HTTP với timeout 20 giây
        response = requests.get(url, timeout=20)

        if response.status_code == 200:
            parser = HtmlParser.from_url(url, Tokenizer("en"))
            document = parser.document

            summarizer = TextRankSummarizer()
            summary = summarizer(document, sentences_count=sentences_count)

            content = [str(sentence) for sentence in summary]

            return content
        else:
            print(f"Failed to fetch content from URL: {url}")
            return None

    except (requests.exceptions.RequestException, requests.exceptions.Timeout) as e:
        print(f"Error occurred while fetching content from URL: {url}")
        return None


def process_url(url):
    content = get_content_summary_from_url(url)
    if content:
        result = {
            'url': url,
            'content': content
        }
        all_results.append(result)
def clean_text(text):
    cleaned_text = re.sub(r'[\t\n\r]', ' ', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    cleaned_text = cleaned_text.strip()
    return cleaned_text
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

#!/usr/bin/env python3
"""Just fetch raw AI news from SerpAPI and save to JSON."""
import requests
import json
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
output_path = f"/Users/jiyingguo/.openclaw/workspace/news_summaries/gaoxiao_raw_{today}.json"

SERPAPI_KEY = "b28c2426b9015470508315f27a6782b552a5a5b39550fbc9b62ff381e67c360f"
url = f"https://serpapi.com/search.json?q=AI+OR+OpenAI+OR+Anthropic+OR+Nvidia+latest+news&tbm=nws&api_key={SERPAPI_KEY}&tbs=qdr:d2&gl=us&hl=en"

print(f"Fetching from SerpAPI...")
resp = requests.get(url, timeout=30)
print(f"Response status: {resp.status_code}")
if resp.status_code != 200:
    print(f"SerpAPI Error: {resp.status_code} {resp.text}")
    exit(1)

articles = resp.json().get('news_results', [])[:6]
print(f"Fetched {len(articles)} articles")

# Print article titles for debug
for i, a in enumerate(articles):
    print(f"  {i+1}. {a.get('title', 'N/A')}")

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

file_size = len(json.dumps(articles, ensure_ascii=False, indent=2))
print(f"Saved to {output_path}")
print(f"File size: {file_size} bytes")

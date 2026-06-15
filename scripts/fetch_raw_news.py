#!/usr/bin/env python3
"""Fetch raw AI news from SerpAPI and save as JSON."""
import requests, json, os
from datetime import datetime

SERPAPI_KEY = "b28c2426b9015470508315f27a6782b552a5a5b39550fbc9b62ff381e67c360f"
today_str = datetime.now().strftime("%Y-%m-%d")
output_dir = "/Users/jiyingguo/.openclaw/workspace/news_summaries"

print("Fetching from SerpAPI...")
url = f"https://serpapi.com/search.json?q=AI+OR+OpenAI+OR+Anthropic+OR+Nvidia+latest+news&tbm=nws&api_key={SERPAPI_KEY}&tbs=qdr:d2&gl=us&hl=en"
try:
    resp = requests.get(url, timeout=30)
    if resp.status_code != 200:
        print(f"SerpAPI Error: {resp.status_code} {resp.text}")
        exit(1)
except Exception as e:
    print(f"SerpAPI Request Error: {e}")
    exit(1)

raw_news = resp.json().get('news_results', [])[:6]
print(f"Fetched {len(raw_news)} articles.")

output_path = os.path.join(output_dir, f"gaoxiao_raw_{today_str}.json")
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(raw_news, f, ensure_ascii=False, indent=2)
print(f"Saved raw JSON to {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")

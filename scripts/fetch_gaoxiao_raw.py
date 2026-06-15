#!/usr/bin/env python3
"""Fetch AI news from SerpAPI and save as raw JSON (no translation)."""
import requests, json, os, sys
from datetime import datetime

SERPAPI_KEY = "b28c2426b9015470508315f27a6782b552a5a5b39550fbc9b62ff381e67c360f"

today = datetime.now().strftime("%Y-%m-%d")
outdir = os.path.expanduser("~/.openclaw/workspace/news_summaries")
os.makedirs(outdir, exist_ok=True)

outpath = os.path.join(outdir, f"gaoxiao_raw_{today}.json")

print("Fetching from SerpAPI...")
url = f"https://serpapi.com/search.json?q=AI+OR+OpenAI+OR+Anthropic+OR+Nvidia+latest+news&tbm=nws&api_key={SERPAPI_KEY}&tbs=qdr:d2&gl=us&hl=en"
try:
    resp = requests.get(url, timeout=15)
    if resp.status_code == 200:
        results = resp.json().get('news_results', [])[:6]
        with open(outpath, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"Saved {len(results)} articles to {outpath}")
        status_path = os.path.join(outdir, f"gaoxiao_status_{today}.json")
        with open(status_path, 'w') as f:
            json.dump({"stage": "fetched", "date": today, "article_count": len(results)}, f)
        print(f"Status updated: stage=fetched")
        sys.exit(0)
    else:
        print(f"SerpAPI Error: {resp.status_code} {resp.text}")
        sys.exit(1)
except Exception as e:
    print(f"Fetch Error: {e}")
    sys.exit(1)

#!/usr/bin/env python3
"""Fetch news using SerpAPI key from the existing script file."""
import sys, os, json, re, requests
from datetime import datetime

# Read the real SerpAPI key from the existing script file
with open('/Users/jiyingguo/.openclaw/workspace/scripts/send_daily_ai_news_real.py', 'r') as f:
    content = f.read()

match = re.search(r'SERPAPI_KEY\s*=\s*"([^"]+)"', content)
if not match:
    print("ERROR: Could not find SerpAPI key in script")
    sys.exit(1)

SERPAPI_KEY = match.group(1)
today = datetime.now().strftime("%Y-%m-%d")
output_path = f"/Users/jiyingguo/.openclaw/workspace/news_summaries/gaoxiao_raw_{today}.json"

print(f"Fetching from SerpAPI (key length: {len(SERPAPI_KEY)})...")
url = f"https://serpapi.com/search.json?q=AI+OR+OpenAI+OR+Anthropic+OR+Nvidia+latest+news&tbm=nws&api_key={SERPAPI_KEY}&tbs=qdr:d2&gl=us&hl=en"
resp = requests.get(url, timeout=30)

if resp.status_code != 200:
    print(f"ERROR: {resp.status_code} - {resp.text[:200]}")
    sys.exit(1)

articles = resp.json().get('news_results', [])[:6]
print(f"Fetched {len(articles)} articles")

for i, a in enumerate(articles):
    title = a.get('title', 'N/A')
    source = a.get('source', 'N/A')
    print(f"  {i+1}. [{source}] {title[:80]}")

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

file_size = os.path.getsize(output_path)
print(f"Saved: {output_path} ({file_size} bytes)")

# Write status
status = {"stage": "fetched", "articles": len(articles), "file_size": file_size, "timestamp": datetime.now().isoformat()}
status_path = f"/Users/jiyingguo/.openclaw/workspace/news_summaries/gaoxiao_status_{today}.json"
with open(status_path, 'w') as f:
    json.dump(status, f, ensure_ascii=False, indent=2)
print(f"Status: {status_path}")

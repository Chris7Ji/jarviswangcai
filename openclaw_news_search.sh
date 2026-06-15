#!/bin/bash
# OpenClaw News Search Script
API_KEY="b28c2426b9015470508315f27a6782b552a5a5b39550fbc9b62ff381e67c360f"

echo "=== CHINESE SEARCH ==="
python3 -c "
import urllib.request, json

api_key = '$API_KEY'
params = 'engine=google&q=OpenClaw+AI+Agent+%E6%9C%80%E6%96%B0%E7%89%88%E6%9C%AC+%E6%8A%80%E8%83%BD%E6%9B%B4%E6%96%B0+2026&tbs=qdr:w&num=10&hl=zh-CN&api_key=' + api_key
url = 'https://serpapi.com/search.json?' + params
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=20) as resp:
        d = json.loads(resp.read())
    r = d.get('organic_results', [])
    for i,x in enumerate(r[:10]):
        title = x.get('title','')
        source = x.get('source','')
        link = x.get('link','')
        snippet = x.get('snippet','')[:200]
        print(f'{i+1}. [{title}] | {source} | {link} | {snippet}')
    print(f'---TOTAL: {len(r)} results---')
except Exception as e:
    print(f'CHINESE_SEARCH_ERROR: {e}')
"

echo ""
echo "=== ENGLISH SEARCH ==="
python3 -c "
import urllib.request, json

api_key = '$API_KEY'
params = 'engine=google&q=OpenClaw+AI+agent+latest+release+GitHub+2026+new+features&tbs=qdr:w&num=10&api_key=' + api_key
url = 'https://serpapi.com/search.json?' + params
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=20) as resp:
        d = json.loads(resp.read())
    r = d.get('organic_results', [])
    for i,x in enumerate(r[:10]):
        title = x.get('title','')
        source = x.get('source','')
        link = x.get('link','')
        snippet = x.get('snippet','')[:200]
        print(f'{i+1}. [{title}] | {source} | {link} | {snippet}')
    print(f'---TOTAL: {len(r)} results---')
except Exception as e:
    print(f'ENGLISH_SEARCH_ERROR: {e}')
"

echo ""
echo "=== GITHUB RELEASES DIRECT ==="
python3 -c "
import urllib.request, json

api_key = '$API_KEY'
params = 'engine=google&q=site:github.com/openclaw/openclaw/releases+after:2026-05-01&num=10&api_key=' + api_key
url = 'https://serpapi.com/search.json?' + params
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=20) as resp:
        d = json.loads(resp.read())
    r = d.get('organic_results', [])
    for i,x in enumerate(r[:10]):
        title = x.get('title','')
        link = x.get('link','')
        snippet = x.get('snippet','')[:200]
        print(f'{i+1}. [{title}] | {link} | {snippet}')
    print(f'---TOTAL: {len(r)} results---')
except Exception as e:
    print(f'GITHUB_SEARCH_ERROR: {e}')
"

echo ""
echo "=== REDDIT SEARCH (past week) ==="
python3 -c "
import urllib.request, json

api_key = '$API_KEY'
params = 'engine=google&q=site:reddit.com/r/openclaw+after:2026-05-18&num=10&api_key=' + api_key
url = 'https://serpapi.com/search.json?' + params
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=20) as resp:
        d = json.loads(resp.read())
    r = d.get('organic_results', [])
    for i,x in enumerate(r[:10]):
        title = x.get('title','')
        link = x.get('link','')
        snippet = x.get('snippet','')[:200]
        print(f'{i+1}. [{title}] | {link} | {snippet}')
    print(f'---TOTAL: {len(r)} results---')
except Exception as e:
    print(f'REDDIT_SEARCH_ERROR: {e}')
"

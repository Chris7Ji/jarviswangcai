#!/bin/bash
# English search for OpenClaw news
API_KEY="b28c2426b9015470508315f27a6782b552a5a5b39550fbc9b62ff381e67c360f"
QUERY="OpenClaw AI agent latest release new features 2026 May"
curl -s "https://serpapi.com/search?q=${QUERY}&api_key=${API_KEY}&num=10&gl=us&hl=en" -o /tmp/serpapi_en.json
python3 -c "
import json,sys
with open('/tmp/serpapi_en.json') as f:
    d=json.load(f)
rs=d.get('organic_results',[])
print(f'Total organic results: {len(rs)}')
print(f'Total results: {d.get(\"search_information\",{}).get(\"total_results\",\"N/A\")}')
for i,r in enumerate(rs):
    print(f'--- Result {i+1} ---')
    print(f'Position: {r.get(\"position\",\"N/A\")}')
    print(f'Title: {r.get(\"title\",\"N/A\")}')
    print(f'Link: {r.get(\"link\",\"N/A\")}')
    print(f'Snippet: {r.get(\"snippet\",\"N/A\")}')
    print(f'Date: {r.get(\"date\",\"N/A\")}')
    src=r.get('source','')
    print(f'Source: {src}')
"

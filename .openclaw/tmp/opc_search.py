#!/usr/bin/env python3
"""Search OPC/solopreneur topics via SerpAPI and print results."""
import urllib.request, urllib.parse, json, sys, os

api_key = os.environ.get("SERPAPI_KEY", "b28c2426b9015470508315f27a6782b552a5a5b39550fbc9b62ff381e67c360f")

queries = [
    "一人公司 OPC 2026 趋势",
    "一人公司 工具 推荐 2026 AI",
    "OPC one person company china 2026",
    "solopreneur AI tools trends 2026",
    "一人公司 政策 深圳 北京 2026",
    "solopreneur tech stack 2026 n8n agent",
]

all_results = []

for q in queries:
    encoded = urllib.parse.quote(q)
    url = f"https://serpapi.com/search.json?q={encoded}&api_key={api_key}&num=8"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=20) as resp:
            d = json.loads(resp.read())
        items = d.get("organic_results", [])
        all_results.append({"query": q, "results": items})
        print(f"✅ [{q}] → {len(items)} results")
    except Exception as e:
        print(f"❌ [{q}] → {e}")

# Output summary
print("\n" + "="*80)
print("OPC 情报汇总")
print("="*80)

for entry in all_results:
    print(f"\n--- {entry['query']} ---")
    for r in entry['results'][:8]:
        print(f"  #{r.get('position','?')} {r.get('title','')}")
        print(f"     {r.get('link','')}")
        snippet = r.get('snippet','')[:180]
        if snippet:
            print(f"     {snippet}")
        print()

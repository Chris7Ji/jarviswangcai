import json, urllib.request, urllib.parse, sys

api_key = "b28c2426b9015470508315f27a6782b552a5a5b39550fbc9b62ff381e67c360f"
query = "OpenClaw AI Agent 最新版本 技能更新 2026"

params = urllib.parse.urlencode({
    "q": query,
    "engine": "google",
    "hl": "zh-cn",
    "gl": "cn",
    "num": 10,
    "api_key": api_key
})
url = f"https://serpapi.com/search.json?{params}"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
resp = urllib.request.urlopen(req, timeout=30)
data = json.load(resp)

results = data.get("organic_results", [])
print(f"Total results: {len(results)}")
for r in results:
    print("---")
    print(f"Title: {r.get('title','')}")
    print(f"Link: {r.get('link','')}")
    print(f"Snippet: {r.get('snippet','')}")
    print(f"Source: {r.get('source','')}")

#!/usr/bin/env python3
import json, urllib.request, urllib.parse, sys, os

API_KEY = "b28c2426b9015470508315f27a6782b552a5a5b39550fbc9b62ff381e67c360f"

def search_serpapi(query, num=5, hl="en"):
    params = {
        "q": query,
        "api_key": API_KEY,
        "engine": "google",
        "num": num,
        "hl": hl
    }
    url = "https://serpapi.com/search?" + urllib.parse.urlencode(params)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            d = json.loads(resp.read().decode())
            results = d.get("organic_results", [])
            return results
    except Exception as e:
        print(f"ERROR: {e}")
        return []

# Search 1
print("=== Search 1: longevity research breakthrough April 2026 ===")
r1 = search_serpapi("longevity research breakthrough April 2026", 5, "en")
for r in r1:
    print(json.dumps({"title": r.get('title',''), "link": r.get('link',''), "snippet": r.get('snippet',''), "source": r.get('source',''), "date": r.get('date','')}, ensure_ascii=False))
    print("---")

# Search 2
print("\n=== Search 2: health aging anti-obesity GLP-1 2026 ===")
r2 = search_serpapi("health aging anti-obesity GLP-1 2026", 5, "en")
for r in r2:
    print(json.dumps({"title": r.get('title',''), "link": r.get('link',''), "snippet": r.get('snippet',''), "source": r.get('source',''), "date": r.get('date','')}, ensure_ascii=False))
    print("---")

# Search 3
print("\n=== Search 3: 延缓衰老 科研成果 2026 ===")
r3 = search_serpapi("延缓衰老 科研成果 2026", 5, "zh-cn")
for r in r3:
    print(json.dumps({"title": r.get('title',''), "link": r.get('link',''), "snippet": r.get('snippet',''), "source": r.get('source',''), "date": r.get('date','')}, ensure_ascii=False))
    print("---")

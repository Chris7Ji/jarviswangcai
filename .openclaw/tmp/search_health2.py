import urllib.request
import urllib.parse
import json
import ssl
ssl_ctx = ssl.create_default_context()

# Try multiple keys
keys_to_try = [
    "b28c2426b9015470508315f27a6782b552a5a5b39550fbc9b62ff381e67c360f",
]

all_results = {}
queries = [
    "延缓衰老 科研成果 2026",
]

API_KEY = keys_to_try[0]
for q in queries:
    params = {
        "q": q,
        "api_key": API_KEY,
        "engine": "google",
        "num": "10",
        "tbm": "nws",
        "hl": "zh-CN"
    }
    url = "https://serpapi.com/search?" + urllib.parse.urlencode(params)
    print(f"Searching: {q}...")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=30, context=ssl_ctx)
        data = json.loads(resp.read().decode())
        results = []
        for r in data.get("news_results", data.get("organic_results", [])):
            item = {
                "title": r.get("title", ""),
                "link": r.get("link", r.get("source", "")),
                "source": r.get("source", ""),
                "date": r.get("date", r.get("publication_date", "")),
                "snippet": r.get("snippet", "")
            }
            results.append(item)
        all_results[q] = results[:6]
        print(f"  -> {len(results)} results")
    except Exception as e:
        all_results[q] = []
        print(f"  -> FAIL: {e}")

print(json.dumps(all_results, ensure_ascii=False, indent=2))

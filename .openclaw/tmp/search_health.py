import urllib.request
import urllib.parse
import json
import ssl

ssl_ctx = ssl.create_default_context()

API_KEY = "b28c2426b9015470508315f27a6782b552a5a5b39550fbc9b62ff381e67c360f"

queries = [
    "longevity research breakthrough 2026",
    "health aging anti-obesity GLP-1 2026",
    "\u7f13\u8868\u8870\u8001 \u79d1\u7814\u6210\u679c 2026"
]

all_results = {}

for q in queries:
    params = {
        "q": q,
        "api_key": API_KEY,
        "engine": "google",
        "num": "10",
        "tbm": "nws",
        "hl": "en"
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

with open("/Users/jiyingguo/.openclaw/workspace/.openclaw/tmp/health_search_raw.json", "w") as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print("Saved!")

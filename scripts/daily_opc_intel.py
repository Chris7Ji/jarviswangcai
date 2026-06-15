#!/usr/bin/env python3
"""Daily OPC (One Person Company) intelligence collector."""
import urllib.request, urllib.parse, json, os, datetime, html as html_mod

# SerpAPI key from MEMORY.md
SERPAPI_KEY = "b28c2426b9015470508315f27a6782b552a5a5b39550fbc9b62ff381e67c360f"

QUERIES = {
    "一人公司 OPC 2026": "一人公司 OPC 2026 趋势",
    "一人公司 工具 AI": "一人公司 工具 推荐 2026 AI",
    "OPC one person company": "OPC one person company 2026",
    "solopreneur AI tools": "solopreneur AI tools trends 2026",
    "一人公司 政策 2026": "一人公司 政策 深圳 北京 2026",
    "solopreneur tech stack n8n": "solopreneur tech stack n8n AI agent 2026",
}

def search(q, num=8):
    encoded = urllib.parse.quote(q)
    url = f"https://serpapi.com/search.json?q={encoded}&api_key={SERPAPI_KEY}&num={num}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            d = json.loads(resp.read())
        return d.get("organic_results", [])
    except Exception as e:
        return []

def esc(s):
    return html_mod.escape(s or "")

def main():
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    print(f"OPC Collector — {date_str}")
    
    all_data = {}
    for label, q in QUERIES.items():
        results = search(q)
        all_data[label] = results
        print(f"  {label}: {len(results)} results")
    
    # Generate HTML
    total = sum(len(r) for r in all_data.values())
    sections = ""
    for cat, results in all_data.items():
        if not results: continue
        items = ""
        for r in results[:6]:
            items += f"""<div class='item'>
  <a href='{esc(r.get('link',''))}' target='_blank' class='tl'>{esc(r.get('title',''))}</a>
  <div class='sn'>{esc((r.get('snippet','') or '')[:200])}</div>
</div>"""
        sections += f"<div class='s'><h2>{esc(cat)}</h2>{items}</div>"
    
    html = f"""<!DOCTYPE html>
<html lang='zh-CN'><head><meta charset='UTF-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'>
<title>OPC每日情报 {date_str}</title>
<style>
body{{font-family:-apple-system,'Segoe UI',Arial,sans-serif;max-width:720px;margin:0 auto;padding:20px;color:#222;background:#f8f9fa;line-height:1.6}}
.hd{{background:linear-gradient(135deg,#2563eb,#7c3aed);color:#fff;padding:24px;border-radius:12px;text-align:center;margin-bottom:16px}}
.hd h1{{margin:0;font-size:20px}}
.s{{background:#fff;border-radius:10px;padding:16px;margin-bottom:12px;box-shadow:0 1px 3px rgba(0,0,0,.08)}}
.s h2{{margin:0 0 8px;font-size:15px;color:#2563eb}}
.tl{{font-weight:600;color:#2563eb;text-decoration:none;font-size:13px}}
.tl:hover{{text-decoration:underline}}
.sn{{font-size:12px;color:#6b7280;margin-top:3px}}
.ft{{text-align:center;font-size:11px;color:#9ca3af;padding:12px}}
</style></head><body>
<div class='hd'><h1>🚀 OPC 每日情报</h1><div>{date_str} · {total}条</div></div>
{sections}
<div class='ft'>🐶🤖 旺财Jarvis · SerpAPI/Google</div>
</body></html>"""
    
    out_dir = os.path.expanduser("~/.openclaw/workspace/news_summaries")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"opc_daily_{date_str}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"\n✅ {out_path} ({os.path.getsize(out_path)} bytes, {total} articles)")

if __name__ == "__main__":
    main()

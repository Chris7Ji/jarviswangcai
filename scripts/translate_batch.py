#!/usr/bin/env python3
"""Translate news using DeepSeek API and generate HTML."""
import json, requests, time, os
from datetime import datetime

DEEPSEEK_KEY = "sk-451b20d00a1a425ea9b18f5c41ea8356"

def call_deepseek(prompt):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {DEEPSEEK_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "response_format": {"type": "json_object"}
    }
    resp = requests.post(url, json=payload, headers=headers, timeout=60)
    if resp.status_code == 200:
        return resp.json()['choices'][0]['message']['content']
    raise Exception(f"DeepSeek Error: {resp.status_code} {resp.text[:200]}")

def clean_json(text):
    text = text.strip()
    if "</think>" in text: text = text.split("</think>")[-1].strip()
    if text.startswith('```json'): text = text[7:]
    elif text.startswith('```'): text = text[3:]
    if text.endswith('```'): text = text[:-3]
    return text.strip()

def translate_batch(articles):
    """Translate all articles in one API call."""
    items = []
    for i, a in enumerate(articles):
        items.append(f'Article {i+1}:\nTitle: {a["title"]}\nSnippet: {a["snippet"][:200]}')
    
    batch_text = "\n\n".join(items)
    
    prompt = f"""Translate the following {len(articles)} English AI news articles to Chinese. For each article, provide:
1. A Chinese title translation
2. A detailed Chinese summary (about 100 Chinese characters) that explains the core content and significance

Output ONLY a JSON array with {len(articles)} objects, each with "title" (Chinese title) and "summary" (Chinese summary).
No markdown, no explanation.

{batch_text}"""

    result = call_deepseek(prompt)
    result = clean_json(result)
    
    try:
        translations = json.loads(result)
        if isinstance(translations, list) and len(translations) == len(articles):
            return translations
        elif isinstance(translations, dict):
            # Might be wrapped
            for key in translations:
                val = translations[key]
                if isinstance(val, list) and len(val) == len(articles):
                    return val
        return None
    except:
        return None

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    raw_path = f"news_summaries/gaoxiao_raw_{today}.json"
    html_path = f"news_summaries/gaoxiao_news_{today}.html"
    
    with open(raw_path) as f:
        raw_news = json.load(f)
    
    print(f"Loaded {len(raw_news)} articles")
    
    # Try batch translation first
    translations = translate_batch(raw_news)
    
    if translations:
        print(f"Batch translation succeeded with {len(translations)} articles")
        for i, t in enumerate(translations):
            raw_news[i]['trans_title'] = t.get('title', raw_news[i]['title'])
            raw_news[i]['trans_summary'] = t.get('summary', raw_news[i].get('snippet', ''))
            raw_news[i]['model'] = 'DeepSeek'
    else:
        print("Batch translation failed, trying individual...")
        for i, item in enumerate(raw_news):
            p = f'Translate this English news to Chinese, output JSON with "title" (Chinese) and "summary" (100字中文摘要). Title: {item["title"]}, Snippet: {item["snippet"][:200]}'
            try:
                r = call_deepseek(p)
                r = clean_json(r)
                j = json.loads(r)
                item['trans_title'] = j.get('title', item['title'])
                item['trans_summary'] = j.get('summary', item.get('snippet', ''))
                item['model'] = 'DeepSeek'
            except Exception as e:
                print(f"  [{i+1}] Failed: {e}")
                item['trans_title'] = item['title']
                item['trans_summary'] = item.get('snippet', '')
                item['model'] = 'Failed'
            time.sleep(1)
    
    # Generate HTML
    today_cn = datetime.now().strftime("%Y年%m月%d日")
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    items_html = ""
    for i, item in enumerate(raw_news):
        title = item.get('trans_title', item.get('title'))
        summary = item.get('trans_summary', item.get('snippet', ''))
        url = item.get('link', '#')
        source = item.get('source', 'Unknown')
        pub_date = item.get('published_date', '')
        model = item.get('model', 'Unknown')
        pub = f" | 发布：{pub_date}" if pub_date else ""
        
        items_html += f"""
        <div class="news-item">
            <div class="news-title">{i+1}. {title}</div>
            <div class="news-meta">来源：{source}{pub} | 翻译：{model}</div>
            <div class="news-summary">{summary}</div>
            <a class="news-link" href="{url}" target="_blank">🔗 点击阅读原文</a>
        </div>"""
    
    html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<title>高校分队 AI 新闻简报 - {today_cn}</title>
<style>
body{{font-family:'Microsoft YaHei',Arial,sans-serif;line-height:1.6;color:#333;max-width:800px;margin:0 auto;padding:20px;background:#f5f5f5}}
.header{{background:linear-gradient(135deg,#1a237e,#283593);color:#fff;padding:25px;border-radius:8px;margin-bottom:20px;text-align:center}}
.header h1{{margin:0;font-size:24px}}
.header .date{{margin-top:8px;font-size:14px;opacity:.9}}
.section{{background:#fff;padding:25px;margin-bottom:20px;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,.08)}}
.news-item{{margin-bottom:25px;padding-bottom:20px;border-bottom:1px solid #eee}}
.news-item:last-child{{border-bottom:none;margin:0;padding:0}}
.news-title{{font-weight:bold;color:#1a237e;margin-bottom:8px;font-size:17px;line-height:1.4}}
.news-summary{{color:#444;margin-bottom:10px;font-size:14px;line-height:1.7}}
.news-link{{display:inline-block;color:#1976d2;text-decoration:none;font-size:13px;font-weight:bold}}
.news-link:hover{{text-decoration:underline}}
.news-meta{{color:#888;font-size:11px;margin-bottom:8px}}
.footer{{text-align:center;color:#999;font-size:12px;margin-top:30px;padding-top:20px;border-top:1px solid #ddd}}
</style></head><body>
<div class="header">
<h1>🤖 高校分队 AI 新闻每日简报</h1>
<div class="date">{today_cn} · 早间版</div>
</div>
<div class="section">
{items_html}
</div>
<div class="footer">
<p>由旺财Jarvis自动生成 · {now_str}</p>
</div>
</body></html>"""
    
    with open(html_path, 'w') as f:
        f.write(html)
    
    print(f"\n✅ HTML saved to {html_path}")
    print(f"   Size: {os.path.getsize(html_path)} bytes")
    print(f"   Articles: {len(raw_news)}")
    
    for item in raw_news:
        print(f"  • {item.get('trans_title', item['title'])[:60]}")
        print(f"    Model: {item.get('model', '?')}")

if __name__ == "__main__":
    main()

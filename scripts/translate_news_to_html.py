#!/usr/bin/env python3
"""Step 2: Translate raw news JSON to HTML with 3-tier fallback."""
import json, requests, time, sys, os
from datetime import datetime

# --- Config ---
SERPAPI_KEY = "b28c2426b9015470508315f27a6782b552a5a5b39550fbc9b62ff381e67c360f"
GEMINI_KEY = "AIzaSyCg6HXyfPSjeh69Uq3xhJ8N4Jj8vkZpN9s"
MINIMAX_KEY = "sk-api-1f4920da6f7b4b44831055dad4aeb79d"
DEEPSEEK_KEY = "sk-451b20d00a1a425ea9b18f5c41ea8356"

def call_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent?key={GEMINI_KEY}"
    payload = {"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"responseMimeType": "application/json"}}
    proxies = {"http": "http://127.0.0.1:7897", "https": "http://127.0.0.1:7897"}
    resp = requests.post(url, json=payload, timeout=60, proxies=proxies)
    if resp.status_code == 200:
        text = resp.json()['candidates'][0]['content']['parts'][0]['text']
        return text
    raise Exception(f"Gemini Error: {resp.status_code} {resp.text[:200]}")

def call_minimax(prompt):
    url = "https://api.minimax.chat/v1/chat/completions"
    headers = {"Authorization": f"Bearer {MINIMAX_KEY}", "Content-Type": "application/json"}
    payload = {"model": "MiniMax-M2.7-highspeed", "messages": [{"role": "user", "content": prompt}]}
    resp = requests.post(url, json=payload, headers=headers, timeout=60)
    if resp.status_code == 200:
        return resp.json()['choices'][0]['message']['content']
    raise Exception(f"MiniMax Error: {resp.status_code} {resp.text[:200]}")

def call_deepseek(prompt):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {DEEPSEEK_KEY}", "Content-Type": "application/json"}
    payload = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}], "response_format": {"type": "json_object"}}
    resp = requests.post(url, json=payload, headers=headers, timeout=60)
    if resp.status_code == 200:
        return resp.json()['choices'][0]['message']['content']
    raise Exception(f"DeepSeek Error: {resp.status_code} {resp.text[:200]}")

def clean_json(text):
    text = text.strip()
    if "</think>" in text: text = text.split("</think>")[-1].strip()
    if text.startswith('```json'): text = text[7:]
    if text.startswith('```'): text = text[3:]
    if text.endswith('```'): text = text[:-3]
    return text.strip()

def translate_one(title, snippet):
    prompt = (
        f"请把以下英文新闻标题和摘要翻译成中文，并写一段详细的中文内容（100字左右），说明其核心内容和影响。"
        f"直接输出纯JSON格式：{{\"title\": \"中文标题\", \"summary\": \"详细的中文摘要\"}}。不要带 markdown ``` 标签。"
        f"原文标题: {title}，原文摘要: {snippet}"
    )
    model_used = "Gemini 3.1 Flash Lite"
    for attempt, (name, fn) in enumerate([
        ("Gemini 3.1 Flash Lite", call_gemini),
        ("MiniMax M2.7", call_minimax),
        ("DeepSeek", call_deepseek)
    ], 1):
        try:
            model_used = name
            res_text = fn(prompt)
            res_json = json.loads(clean_json(res_text))
            res_json["model"] = model_used
            return res_json
        except Exception as e:
            print(f"  [{name}] Attempt {attempt} failed: {e}")
            if attempt < 3:
                time.sleep(2)
                continue
            return {"title": title, "summary": snippet, "model": "All Failed"}
    return {"title": title, "summary": snippet, "model": "All Failed"}

def generate_html(news_items):
    today_str = datetime.now().strftime("%Y年%m月%d日")
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    items_html = ""
    for i, item in enumerate(news_items):
        title = item.get('trans_title', item.get('title'))
        summary = item.get('trans_summary', item.get('snippet', ''))
        url = item.get('link', '#')
        source = item.get('source', 'Unknown')
        pub_date = item.get('published_date', '')
        model = item.get('model', 'Unknown')
        
        pub_html = f" | 发布：{pub_date}" if pub_date else ""
        
        items_html += f"""
        <div class="news-item">
            <div class="news-title">{i+1}. {title}</div>
            <div class="news-meta">来源：{source}{pub_html} | 翻译模型：{model}</div>
            <div class="news-summary">{summary}</div>
            <a class="news-link" href="{url}" target="_blank">🔗 点击阅读原文</a>
        </div>
        """
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>高校分队 AI 新闻每日简报 - {today_str}</title>
    <style>
        body {{ font-family: 'Microsoft YaHei', Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f5f5f5; }}
        .header {{ background: linear-gradient(135deg, #1a237e, #283593); color: white; padding: 25px; border-radius: 8px; margin-bottom: 20px; text-align: center; }}
        .header h1 {{ margin: 0; font-size: 24px; }}
        .header .date {{ margin-top: 8px; font-size: 14px; opacity: 0.9; }}
        .header .subtitle {{ font-size: 12px; opacity: 0.7; margin-top: 5px; }}
        .section {{ background-color: white; padding: 25px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
        .news-item {{ margin-bottom: 25px; padding-bottom: 20px; border-bottom: 1px solid #eee; }}
        .news-item:last-child {{ border-bottom: none; margin-bottom: 0; padding-bottom: 0; }}
        .news-title {{ font-weight: bold; color: #1a237e; margin-bottom: 8px; font-size: 17px; line-height: 1.4; }}
        .news-summary {{ color: #444; margin-bottom: 10px; font-size: 14px; line-height: 1.7; }}
        .news-link {{ display: inline-block; color: #1976d2; text-decoration: none; font-size: 13px; font-weight: bold; padding: 4px 0; }}
        .news-link:hover {{ text-decoration: underline; }}
        .news-meta {{ color: #888; font-size: 11px; margin-bottom: 8px; }}
        .footer {{ text-align: center; color: #999; font-size: 12px; margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; }}
        .footer .disclaimer {{ color: #bbb; font-size: 11px; margin-top: 8px; }}
        @media only screen and (max-width: 600px) {{
            body {{ padding: 10px; }}
            .header {{ padding: 15px; }}
            .header h1 {{ font-size: 20px; }}
            .section {{ padding: 15px; }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 高校分队 AI 新闻每日简报</h1>
        <div class="date">{today_str} · 早间版</div>
        <div class="subtitle">内容动态抓取自权威媒体 · 由旺财Jarvis自动翻译整理</div>
    </div>
    <div class="section">
        {items_html}
    </div>
    <div class="footer">
        <p>本简报由旺财Jarvis 🤖🐶 使用AI技术自动生成</p>
        <p>生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        <div class="disclaimer">免责声明：新闻内容源自第三方媒体，翻译结果由AI模型生成，仅供参考</div>
    </div>
</body>
</html>"""
    return html

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    raw_path = f"news_summaries/gaoxiao_raw_{today}.json"
    html_path = f"news_summaries/gaoxiao_news_{today}.html"
    
    # Read raw JSON
    with open(raw_path) as f:
        raw_news = json.load(f)
    
    print(f"Loaded {len(raw_news)} articles from {raw_path}")
    
    # Translate each article
    processed = []
    for i, item in enumerate(raw_news):
        print(f"[{i+1}/{len(raw_news)}] Translating: {item['title'][:50]}...")
        result = translate_one(item['title'], item.get('snippet', ''))
        item['trans_title'] = result.get('title', item['title'])
        item['trans_summary'] = result.get('summary', item.get('snippet', ''))
        item['model'] = result.get('model', 'Unknown')
        processed.append(item)
        time.sleep(1)  # Rate limiting
    
    # Generate HTML
    print("\nGenerating HTML...")
    html_content = generate_html(processed)
    
    # Save HTML
    with open(html_path, 'w') as f:
        f.write(html_content)
    
    print(f"\n✅ HTML saved to {html_path}")
    print(f"   File size: {os.path.getsize(html_path)} bytes")
    print(f"   Articles translated: {len(processed)}")
    
    # Print summary for verification
    print("\n--- Translated Articles ---")
    for item in processed:
        print(f"  • {item['trans_title'][:60]}")
        print(f"    Model: {item['model']}")
    print("--------------------------")

if __name__ == "__main__":
    main()

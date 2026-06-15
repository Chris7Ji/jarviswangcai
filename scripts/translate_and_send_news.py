#!/usr/bin/env python3
"""Translate news from Tavily, generate HTML, send email."""
import json
import os
import requests
import time
import smtplib
import ssl
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

STATUS_DIR = "/Users/jiyingguo/.openclaw/workspace/news_summaries"
TODAY = "2026-05-20"
RAW_FILE = f"{STATUS_DIR}/gaoxiao_raw_{TODAY}.json"
HTML_FILE = f"{STATUS_DIR}/gaoxiao_news_{TODAY}.html"
STATUS_FILE = f"{STATUS_DIR}/gaoxiao_status_{TODAY}.json"

TO_EMAILS = [
    "liuwei44259@huawei.com", "tiankunyang@huawei.com", "qinhongyi2@huawei.com",
    "jiawei18@huawei.com", "jiyingguo@huawei.com", "linfeng67@huawei.com",
    "lvluling1@huawei.com", "suqi1@huawei.com", "susha@huawei.com",
    "wangdongxiao@huawei.com", "xiongguifang@huawei.com", "xushengsheng@huawei.com",
    "zhangqianfeng2@huawei.com", "zhangyexing2@huawei.com", "86940135@qq.com"
]

def update_status(stage, status, detail=""):
    data = {"stage": stage, "status": status, "detail": detail, "updated_at": datetime.now().isoformat()}
    with open(STATUS_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[STATUS] Stage={stage}, Status={status}")

GEMINI_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyDUXba29bf86c_pjadKWftMH6u30kEpN9s")
MINIMAX_KEY = os.environ.get("MINIMAX_API_KEY", "sk-api-bS8q_8MyM1yPPp05MLY9OYxRmnt7_J-tdLTSngjfikY4B-HKrRzFDb6HigbxLusav_28ILdivTB91OiHNu73Y29ZE2ktdAB1ezfJneH80t__lnVQA0bbZrY")
DEEPSEEK_KEY = os.environ.get("DEEPSEEK_API_KEY", "sk-451f43ffa9764b7e91430e4d39538356")
PROXIES = {"http": "http://127.0.0.1:7897", "https": "http://127.0.0.1:7897"}

def call_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent?key={GEMINI_KEY}"
    resp = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"responseMimeType": "application/json"}}, timeout=60, proxies=PROXIES)
    if resp.status_code == 200:
        return resp.json()['candidates'][0]['content']['parts'][0]['text']
    raise Exception(f"Gemini Error: {resp.status_code} {resp.text[:200]}")

def call_minimax(prompt):
    headers = {"Authorization": f"Bearer {MINIMAX_KEY}", "Content-Type": "application/json"}
    resp = requests.post("https://api.minimax.chat/v1/chat/completions", json={"model": "MiniMax-M2.7-highspeed", "messages": [{"role": "user", "content": prompt}]}, headers=headers, timeout=60)
    if resp.status_code == 200:
        return resp.json()['choices'][0]['message']['content']
    raise Exception(f"MiniMax Error: {resp.status_code} {resp.text[:200]}")

def call_deepseek(prompt):
    headers = {"Authorization": f"Bearer {DEEPSEEK_KEY}", "Content-Type": "application/json"}
    resp = requests.post("https://api.deepseek.com/v1/chat/completions", json={"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}], "response_format": {"type": "json_object"}}, headers=headers, timeout=60)
    if resp.status_code == 200:
        return resp.json()['choices'][0]['message']['content']
    raise Exception(f"DeepSeek Error: {resp.status_code} {resp.text[:200]}")

def translate_one(title, snippet):
    prompt = f'请把以下英文新闻标题和摘要翻译成中文，并写一段详细的中文内容（100字左右），说明其核心内容和影响。直接输出纯JSON格式：{{"title": "中文标题", "summary": "详细的中文摘要"}}。原文标题: {title}，原文摘要: {snippet}'
    errors = []
    for name, fn in [("Gemini 3.1 Flash Lite", call_gemini), ("MiniMax M2.7", call_minimax), ("DeepSeek", call_deepseek)]:
        try:
            text = fn(prompt)
            text = text.strip()
            if "</think>" in text: text = text.split("</think>")[-1].strip()
            if text.startswith('```json'): text = text[7:]
            elif text.startswith('```'): text = text[3:]
            if text.endswith('```'): text = text[:-3]
            text = text.strip()
            res = json.loads(text)
            res["model"] = name
            return res
        except Exception as e:
            errors.append(f"{name}: {e}")
            continue
    return {"title": title, "summary": snippet[:200], "model": f"Failed ({'; '.join(errors)})"}

def generate_html(news_items):
    today_cn = "2026年5月20日"
    items_html = ""
    for i, item in enumerate(news_items):
        title = item.get('trans_title', item.get('title'))
        summary = item.get('trans_summary', item.get('snippet', ''))
        url = item.get('link', '#')
        source = item.get('source', 'Unknown')
        items_html += f"""
<div class="news-item">
    <div class="news-title">{i+1}. {title}</div>
    <div class="news-meta">来源：{source} | 翻译模型：{item.get('model', 'Unknown')}</div>
    <div class="news-summary">{summary}</div>
    <a class="news-link" href="{url}" target="_blank">🔗 点击阅读真实原文</a>
</div>"""
    html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>高校分队 AI 新闻每日简报 - {today_cn}</title>
<style>
body {{ font-family: 'Microsoft YaHei', Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f5f5f5; }}
.header {{ background-color: #1a237e; color: white; padding: 20px; border-radius: 5px; margin-bottom: 20px; }}
.header h1 {{ margin: 0; font-size: 24px; }}
.header .date {{ margin-top: 5px; font-size: 14px; opacity: 0.9; }}
.section {{ background-color: white; padding: 20px; margin-bottom: 20px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
.news-item {{ margin-bottom: 20px; padding-bottom: 20px; border-bottom: 1px solid #eee; }}
.news-item:last-child {{ border-bottom: none; }}
.news-title {{ font-weight: bold; color: #1a237e; margin-bottom: 8px; font-size: 16px; }}
.news-summary {{ color: #555; margin-bottom: 8px; font-size: 14px; line-height: 1.5; }}
.news-link {{ color: #1976d2; text-decoration: none; font-size: 13px; font-weight: bold; }}
.news-meta {{ color: #888; font-size: 12px; margin-bottom: 5px; }}
.footer {{ text-align: center; color: #666; font-size: 12px; margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; }}
</style></head><body>
<div class="header"><h1>高校分队 AI 新闻每日简报</h1><div class="date">{today_cn}早间版 (内容动态抓取自权威媒体)</div></div>
<div class="section">{items_html}
</div>
<div class="footer"><p>本简报由旺财Jarvis自动抓取生成</p><p>生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p></div>
</body></html>"""
    return html

def send_email(html_body, subject):
    context = ssl.create_default_context()
    SMTP_SERVER = "smtp.qq.com"
    SMTP_PORT = 587
    EMAIL = "86940135@qq.com"
    PASSWORD = "icxhfzuyzbhbbjie"
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=20) as server:
            server.starttls(context=context)
            server.login(EMAIL, PASSWORD)
            for to_email in TO_EMAILS:
                msg = MIMEMultipart("alternative")
                msg["Subject"] = subject
                msg["From"] = EMAIL
                msg["To"] = to_email
                msg.attach(MIMEText("请使用支持HTML的邮件客户端查看。", "plain", "utf-8"))
                msg.attach(MIMEText(html_body, "html", "utf-8"))
                try:
                    server.sendmail(EMAIL, [to_email], msg.as_string())
                    print(f"✅ Sent to {to_email}")
                    time.sleep(1)
                except Exception as e:
                    print(f"❌ Failed to send to {to_email}: {e}")
        return True
    except Exception as e:
        print(f"❌ SMTP Error: {e}")
        return False

def main():
    existing_raw = None
    if os.path.exists(RAW_FILE):
        with open(RAW_FILE) as f:
            existing_raw = json.load(f)
        print(f"✅ Raw file exists: {len(existing_raw)} articles. Skipping fetch/translate.")
        news_items = existing_raw
    else:
        tavily_file = "/tmp/tavily_news.json"
        if not os.path.exists(tavily_file):
            print("❌ No /tmp/tavily_news.json found!")
            update_status("fetch", "failed", "No news source file")
            return
        with open(tavily_file) as f:
            raw_news = json.load(f)
        print(f"📰 Loaded {len(raw_news)} articles from Tavily. Translating...")
        update_status("translate", "in_progress", f"Translating {len(raw_news)} articles")
        news_items = []
        for i, r in enumerate(raw_news):
            print(f"  [{i+1}/{len(raw_news)}] Translating: {r['title'][:60]}...")
            trans = translate_one(r['title'], r.get('snippet', ''))
            r['trans_title'] = trans.get('title', r['title'])
            r['trans_summary'] = trans.get('summary', r.get('snippet', ''))
            r['model'] = trans.get('model', 'Unknown')
            news_items.append(r)
        os.makedirs(STATUS_DIR, exist_ok=True)
        with open(RAW_FILE, "w", encoding="utf-8") as f:
            json.dump(news_items, f, ensure_ascii=False, indent=2)
        update_status("translate", "done", f"Translated {len(news_items)} articles")

    if os.path.exists(HTML_FILE):
        with open(HTML_FILE) as f:
            html_content = f.read()
        print(f"✅ HTML file exists ({len(html_content)} bytes). Skipping generation.")
    else:
        print("📝 Generating HTML...")
        html_content = generate_html(news_items)
        with open(HTML_FILE, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✅ HTML generated: {len(html_content)} bytes")
        update_status("html", "done", f"HTML generated: {len(html_content)} bytes")

    subject = f"[2026-05-20] 高校分队 AI 新闻每日简报"
    print(f"📧 Sending email to {len(TO_EMAILS)} recipients...")
    update_status("email", "in_progress", "Sending emails")
    success = send_email(html_content, subject)
    if success:
        update_status("email", "done", f"Sent to {len(TO_EMAILS)} recipients")
        print("🎉 All done!")
    else:
        update_status("email", "failed", "SMTP error")

    print(f"\n{'='*50}")
    print(f"📊 SUMMARY:")
    if os.path.exists(RAW_FILE):
        print(f"  Raw file: {RAW_FILE} ({os.path.getsize(RAW_FILE)} bytes)")
    if os.path.exists(HTML_FILE):
        print(f"  HTML file: {HTML_FILE} ({os.path.getsize(HTML_FILE)} bytes)")
    print(f"  Articles: {len(news_items)}")
    print(f"  Recipients: {len(TO_EMAILS)}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()

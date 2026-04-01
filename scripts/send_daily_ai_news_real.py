import requests
import json
import smtplib
import ssl
import time
import subprocess
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurations
SERPAPI_KEY = "b28c2426b9015470508315f27a6782b552a5a5b39550fbc9b62ff381e67c360f"

SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587
EMAIL = "86940135@qq.com"
PASSWORD = "icxhfzuyzbhbbjie"

TO_EMAILS = [
    "liuwei44259@huawei.com",
    "tiankunyang@huawei.com",
    "qinhongyi2@huawei.com",
    "jiawei18@huawei.com",
    "jiyingguo@huawei.com",
    "linfeng67@huawei.com",
    "lvluling1@huawei.com",
    "suqi1@huawei.com",
    "susha@huawei.com",
    "wangdongxiao@huawei.com",
    "xiongguifang@huawei.com",
    "xushengsheng@huawei.com",
    "zhangqianfeng2@huawei.com",
    "zhangyexing2@huawei.com",
    "86940135@qq.com"
]

def fetch_real_news():
    print("Fetching from SerpAPI...")
    url = f"https://serpapi.com/search.json?q=AI+OR+OpenAI+OR+Anthropic+OR+Nvidia+latest+news&tbm=nws&api_key={SERPAPI_KEY}&tbs=qdr:d2&gl=us&hl=en"
    try:
        resp = requests.get(url, timeout=15)
        if resp.status_code == 200:
            return resp.json().get('news_results', [])[:6] # Top 6 articles
    except Exception as e:
        print("SerpAPI Error:", e)
    return []

def call_gemini(prompt):
    GEMINI_KEY = "AIzaSyDUXba29bf86c_pjadKWftMH6u30kEpN9s"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent?key={GEMINI_KEY}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseMimeType": "application/json"}
    }
    proxies = {"http": "http://127.0.0.1:7897", "https": "http://127.0.0.1:7897"}
    resp = requests.post(url, json=payload, timeout=60, proxies=proxies)
    if resp.status_code == 200:
        return resp.json()['candidates'][0]['content']['parts'][0]['text']
    raise Exception(f"Gemini Error: {resp.text}")

def call_minimax(prompt):
    MINIMAX_KEY = "sk-api-bS8q_8MyM1yPPp05MLY9OYxRmnt7_J-tdLTSngjfikY4B-HKrRzFDb6HigbxLusav_28ILdivTB91OiHNu73Y29ZE2ktdAB1ezfJneH80t__lnVQA0bbZrY"
    url = "https://api.minimax.chat/v1/chat/completions"
    headers = {"Authorization": f"Bearer {MINIMAX_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "MiniMax-M2.7-highspeed",
        "messages": [{"role": "user", "content": prompt}]
    }
    resp = requests.post(url, json=payload, headers=headers, timeout=60)
    if resp.status_code == 200:
        return resp.json()['choices'][0]['message']['content']
    raise Exception(f"MiniMax Error: {resp.text}")

def call_deepseek(prompt):
    DEEPSEEK_KEY = "sk-451f43ffa9764b7e91430e4d39538356"
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
    raise Exception(f"DeepSeek Error: {resp.text}")

def clean_json(text):
    text = text.strip()
    if "</think>" in text:
        text = text.split("</think>")[-1].strip()
    if text.startswith('```json'): text = text[7:]
    if text.startswith('```'): text = text[3:]
    if text.endswith('```'): text = text[:-3]
    return text.strip()

def translate_and_summarize(title, snippet):
    prompt = f"请把以下英文新闻标题和摘要翻译成中文，并写一段详细的中文内容（100字左右），说明其核心内容和影响。直接输出纯JSON格式：{{\"title\": \"中文标题\", \"summary\": \"详细的中文摘要\"}}。不要带 markdown ``` 标签。原文标题: {title}，原文摘要: {snippet}"
    model_used = "Gemini 3.1 Flash Lite"
    try:
        res_text = call_gemini(prompt)
    except Exception as e:
        print("Gemini failed, trying MiniMax...", e)
        model_used = "MiniMax M2.7"
        try:
            res_text = call_minimax(prompt)
        except Exception as e:
            print("MiniMax failed, trying DeepSeek...", e)
            model_used = "DeepSeek"
            try:
                res_text = call_deepseek(prompt)
            except Exception as e:
                print("All models failed:", e)
                return {"title": title, "summary": snippet, "model": "Failed"}
    try:
        res_json = json.loads(clean_json(res_text))
        res_json["model"] = model_used
        return res_json
    except Exception as e:
        print("JSON Parse Error:", e, res_text)
        return {"title": title, "summary": snippet, "model": model_used + " (JSON Error)"}

def generate_html_email(news_items):
    today_str = datetime.now().strftime("%Y年%m月%d日")
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>高校分队 AI 新闻每日简报 - {today_str}</title>
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
    </style>
</head>
<body>
    <div class="header">
        <h1>高校分队 AI 新闻每日简报</h1>
        <div class="date">{today_str}早间版 (内容动态抓取自权威媒体)</div>
    </div>
    <div class="section">
"""
    
    for i, item in enumerate(news_items):
        title = item.get('trans_title', item.get('title'))
        summary = item.get('trans_summary', item.get('snippet'))
        url = item.get('link', '#')
        source = item.get('source', 'Unknown')
        
        html += f"""
        <div class="news-item">
            <div class="news-title">{i+1}. {title}</div>
            <div class="news-meta">来源：{source} | 翻译模型：{item.get('model', 'Unknown')}</div>
            <div class="news-summary">{summary}</div>
            <a class="news-link" href="{url}" target="_blank">🔗 点击阅读真实原文 (指向具体文章)</a>
        </div>
        """

    html += f"""
    </div>
    <div class="footer">
        <p>本简报由旺财Jarvis自动抓取真实文章链接生成，告别假链接！</p>
        <p>生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    </div>
</body>
</html>"""
    return html

def send_emails_batch(to_emails, subject, html_body):
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=20) as server:
            server.starttls(context=context)
            server.login(EMAIL, PASSWORD)
            for to_email in to_emails:
                msg = MIMEMultipart("alternative")
                msg["Subject"] = subject
                msg["From"] = EMAIL
                msg["To"] = to_email
                plain_text = "高校分队 AI 新闻每日简报\\n请使用支持HTML的邮件客户端查看。"
                msg.attach(MIMEText(plain_text, "plain", "utf-8"))
                msg.attach(MIMEText(html_body, "html", "utf-8"))
                try:
                    server.sendmail(EMAIL, [to_email], msg.as_string())
                    print(f"Successfully sent to {to_email}")
                    time.sleep(1)
                except Exception as e:
                    print(f"Failed to send to {to_email}: {e}")
    except Exception as e:
        print(f"SMTP Connection Error: {e}")

def main():
    print("Fetching news...")
    raw_news = fetch_real_news()
    if not raw_news:
        print("Failed to fetch news.")
        return
        
    print(f"Fetched {len(raw_news)} articles. Translating...")
    processed_news = []
    for r in raw_news:
        trans = translate_and_summarize(r['title'], r.get('snippet', ''))
        r['trans_title'] = trans.get('title', r['title'])
        r['trans_summary'] = trans.get('summary', r.get('snippet', ''))
        r['model'] = trans.get('model', 'Unknown')
        processed_news.append(r)
        
    print("Generating HTML...")
    html_content = generate_html_email(processed_news)
    
    today_str = datetime.now().strftime("%Y-%m-%d")
    subject = f"[{today_str}] 高校分队 AI 新闻每日简报"
    
    print("Sending emails to all recipients...")
    send_emails_batch(TO_EMAILS, subject, html_content)

if __name__ == "__main__":
    main()

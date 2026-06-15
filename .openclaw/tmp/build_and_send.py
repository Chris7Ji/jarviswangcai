#!/usr/bin/env python3
"""Build HTML and send gaoxiao AI news email"""
import json, smtplib, ssl, time
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP config
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587
EMAIL = "86940135@qq.com"
PASSWORD = "oepkunkbmboucadg"

TO_EMAILS = [
    "liuwei44259@huawei.com", "tiankunyang@huawei.com", "qinhongyi2@huawei.com",
    "jiawei18@huawei.com", "jiyingguo@huawei.com", "linfeng67@huawei.com",
    "lvluling1@huawei.com", "suqi1@huawei.com", "susha@huawei.com",
    "wangdongxiao@huawei.com", "xiongguifang@huawei.com", "xushengsheng@huawei.com",
    "zhangqianfeng2@huawei.com", "zhangyexing2@huawei.com", "86940135@qq.com"
]

today_cn = datetime.now().strftime("%Y年%m月%d日")
today_en = datetime.now().strftime("%Y-%m-%d")

def generate_html(news_items):
    categories = {"行业动态": [], "融资动态": [], "政策标准": [], "产品发布": []}
    for item in news_items:
        cat = item.get("category", "其他")
        categories.setdefault(cat, []).append(item)

    category_icons = {"行业动态": "📊", "融资动态": "💰", "政策标准": "📋", "产品发布": "🚀", "其他": "📌"}
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>高校分队 AI 新闻每日简报 - {today_cn}</title>
    <style>
        body {{ font-family: 'Microsoft YaHei', 'PingFang SC', Arial, sans-serif; line-height: 1.6; color: #333; max-width: 750px; margin: 0 auto; padding: 20px; background-color: #f0f2f5; }}
        .header {{ background: linear-gradient(135deg, #1a237e, #283593); color: white; padding: 28px 24px; border-radius: 12px; margin-bottom: 24px; box-shadow: 0 4px 12px rgba(26,35,126,0.2); }}
        .header h1 {{ margin: 0; font-size: 22px; letter-spacing: 1px; }}
        .header .sub {{ margin-top: 8px; font-size: 13px; opacity: 0.85; }}
        .header .badge {{ display: inline-block; background: rgba(255,255,255,0.15); padding: 3px 10px; border-radius: 12px; font-size: 11px; margin-top: 8px; }}
        .section {{ background: white; margin-bottom: 18px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); overflow: hidden; }}
        .section-title {{ padding: 14px 20px; font-weight: bold; font-size: 15px; color: #1a237e; border-bottom: 1px solid #e8eaf6; }}
        .news-item {{ padding: 16px 20px; border-bottom: 1px solid #f5f5f5; }}
        .news-item:last-child {{ border-bottom: none; }}
        .news-num {{ display: inline-block; background: #1a237e; color: white; width: 22px; height: 22px; line-height: 22px; text-align: center; border-radius: 50%; font-size: 11px; margin-right: 8px; flex-shrink: 0; }}
        .news-title {{ font-weight: bold; color: #1a237e; font-size: 15px; margin-bottom: 8px; line-height: 1.4; }}
        .news-summary {{ color: #555; font-size: 13.5px; line-height: 1.7; margin-bottom: 8px; }}
        .news-link {{ color: #1976d2; text-decoration: none; font-size: 12px; }}
        .news-link:hover {{ text-decoration: underline; }}
        .footer {{ text-align: center; color: #999; font-size: 11px; margin-top: 30px; padding: 20px; border-top: 1px solid #eee; }}
        .footer a {{ color: #666; text-decoration: none; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 高校分队 AI 新闻每日简报</h1>
        <div class="sub">{today_cn} · 早间版</div>
        <div class="badge">🎯 精选 {len(news_items)} 条 AI 要闻</div>
    </div>
"""

    idx = 0
    for cat in ["行业动态", "融资动态", "产品发布", "政策标准", "其他"]:
        items = categories.get(cat, [])
        if not items:
            continue
        icon = category_icons.get(cat, "📌")
        html += f"""    <div class="section">
        <div class="section-title">{icon} {cat}</div>
"""
        for item in items:
            idx += 1
            html += f"""        <div class="news-item">
            <div class="news-title"><span class="news-num">{idx}</span>{item['title']}</div>
            <div class="news-summary">{item['summary']}</div>
            <a class="news-link" href="{item['link']}" target="_blank">🔗 阅读原文 →</a>
        </div>
"""
        html += """    </div>
"""

    html += f"""    <div class="footer">
        <p>📬 本简报由旺财Jarvis自动生成 · 内容来源为公开新闻报道</p>
        <p>🕐 生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        <p><a href="https://github.com/openclaw/openclaw">Powered by OpenClaw</a></p>
    </div>
</body>
</html>"""
    return html

def send_mail(to_emails, subject, html_body):
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=20) as server:
            server.starttls(context=context)
            server.login(EMAIL, PASSWORD)
            sent_count = 0
            fail_count = 0
            for to_email in to_emails:
                msg = MIMEMultipart("alternative")
                msg["Subject"] = subject
                msg["From"] = EMAIL
                msg["To"] = to_email
                msg.attach(MIMEText("高校分队 AI 新闻每日简报\n请使用支持HTML的邮件客户端查看。", "plain", "utf-8"))
                msg.attach(MIMEText(html_body, "html", "utf-8"))
                try:
                    server.sendmail(EMAIL, [to_email], msg.as_string())
                    print(f"✅ Sent to {to_email}")
                    sent_count += 1
                    time.sleep(0.5)
                except Exception as e:
                    print(f"❌ Failed to {to_email}: {e}")
                    fail_count += 1
            return sent_count, fail_count
    except Exception as e:
        print(f"SMTP Connection Error: {e}")
        return 0, len(to_emails)

# Load translations
with open("/Users/jiyingguo/.openclaw/workspace/.openclaw/tmp/gaoxiao_translations.json", "r") as f:
    news_items = json.load(f)

print(f"Loaded {len(news_items)} translated articles")

# Generate HTML
html_content = generate_html(news_items)
today_str = datetime.now().strftime("%Y-%m-%d")

# Save HTML
html_path = f"/Users/jiyingguo/.openclaw/workspace/news_summaries/gaoxiao_news_{today_str}.html"
with open(html_path, "w") as f:
    f.write(html_content)
print(f"HTML saved: {html_path}")

# Send email
subject = f"[{today_str}] 高校分队 AI 新闻每日简报"
print(f"\nSending email to {len(TO_EMAILS)} recipients...")
sent, failed = send_mail(TO_EMAILS, subject, html_content)

print(f"\n--- Result ---")
print(f"Sent: {sent}, Failed: {failed}")
if failed == 0:
    print("✅ All emails sent successfully!")
else:
    print(f"⚠️ {failed} emails failed")

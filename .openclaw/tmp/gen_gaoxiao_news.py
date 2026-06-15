#!/usr/bin/env python3
"""Generate translated HTML for gaoxiao news and send email."""
import json, smtplib, ssl, time, os as osmod
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

today = "2026-06-02"
today_cn = "2026\u5e746\u67082\u65e5"
raw_path = osmod.path.expanduser("~/.openclaw/workspace/news_summaries/gaoxiao_raw_2026-06-02.json")
html_path = osmod.path.expanduser("~/.openclaw/workspace/news_summaries/gaoxiao_news_2026-06-02.html")
status_path = osmod.path.expanduser("~/.openclaw/workspace/news_summaries/gaoxiao_status_2026-06-02.json")

with open(raw_path) as f:
    articles = json.load(f)

def save_status(stage, success, msg=""):
    status = {
        "date": today, "stage": stage, "success": success,
        "message": msg, "timestamp": datetime.now().isoformat()
    }
    with open(status_path, "w") as f:
        json.dump(status, f, ensure_ascii=False, indent=2)
    print(f"Status saved: stage={stage}, success={success}")

translations = [
    {"title": "\u82f1\u4f1f\u8fbe\u4e0e\u5fae\u8f6f\u91cd\u65b0\u5b9a\u4e49Windows PC\uff0c\u8fce\u63a5\u4e2a\u4ebaAI\u65f6\u4ee3", "summary": "\u82f1\u4f1f\u8fbe\u4eca\u65e5\u53d1\u5e03\u5168\u65b0RTX Spark\u2122\u8d85\u7ea7\u82af\u7247\uff0c\u91cd\u65b0\u5b9a\u4e49Windows PC\u4ee5\u8fce\u63a5\u4e2a\u4ebaAI\u4ee3\u7406\u65f6\u4ee3\u3002\u8fd9\u6b3e\u65b0\u578b\u82af\u7247\u5c06\u4e3aWindows\u7b14\u8bb0\u672c\u548c\u53f0\u5f0f\u673a\u63d0\u4f9b\u5168\u65b0\u7ea7\u522b\u7684AI\u8ba1\u7b97\u80fd\u529b\uff0c\u4f7fAI\u4ee3\u7406\u80fd\u591f\u76f4\u63a5\u5728\u4e2a\u4eba\u7535\u8111\u4e0a\u8fd0\u884c\uff0c\u65e0\u9700\u4f9d\u8d56\u4e91\u7aef\u5904\u7406\u3002"},
    {"title": "Anthropic\u63d0\u4ea4IPO\u6587\u4ef6\uff0cAI\u516c\u53f8\u4e0a\u5e02\u7ade\u8d5b\u5347\u6e29", "summary": "\u4eba\u5de5\u667a\u80fd\u516c\u53f8Anthropic\u5df2\u5411\u7f8e\u56fd\u8bc1\u5238\u4ea4\u6613\u59d4\u5458\u4f1a\u63d0\u4ea4\u673a\u5bc6IPO\u6587\u4ef6\uff0c\u5728\u4e0eOpenAI\u7684\u4e0a\u5e02\u7ade\u8d5b\u4e2d\u62a2\u5148\u4e00\u6b65\u3002\u8fc7\u53bb\u4e00\u5e74\u4e2d\uff0c\u53d7\u76ca\u4e8e\u5176\u5148\u8fdbAI\u6280\u672f\u7684\u5feb\u901f\u53d1\u5c55\uff0cAnthropic\u5b9e\u73b0\u4e86\u7206\u53d1\u5f0f\u589e\u957f\u3002"},
    {"title": "\u82f1\u4f1f\u8fbe\u53d1\u5e03\u5168\u65b0\u82af\u7247\uff0c\u5c06AI\u76f4\u63a5\u5e26\u5165\u4e2a\u4eba\u7535\u8111", "summary": "\u82f1\u4f1f\u8fbe\u53d1\u5e03\u5168\u65b0\u82af\u7247\uff0c\u5c06\u9a71\u52a8\u65b0\u6b3eWindows\u7b14\u8bb0\u672c\u548c\u53f0\u5f0f\u673a\uff0c\u771f\u6b63\u5b9e\u73b0AI\u4e2a\u4eba\u7535\u8111\u3002\u65b0\u82af\u7247\u4f7f\u5f97AI\u5904\u7406\u80fd\u529b\u4ece\u4e91\u7aef\u4e0b\u6c89\u5230\u4e2a\u4eba\u8bbe\u5907\uff0c\u7528\u6237\u53ef\u4ee5\u76f4\u63a5\u5728\u672c\u5730\u8fd0\u884cAI\u5e94\u7528\u3002"},
    {"title": "AI\u5de8\u5934Anthropic\u63a8\u8fdbIPO\uff0c\u52a0\u901f\u4e0eOpenAI\u7684\u7ade\u4e89", "summary": "AI\u5de8\u5934Anthropic\u5df2\u5411\u7f8e\u56fd\u76d1\u7ba1\u673a\u6784\u79d8\u5bc6\u63d0\u4ea4IPO\u7533\u8bf7\uff0c\u5728\u4e0e\u7ade\u4e89\u5bf9\u624bOpenAI\u7684\u4e0a\u5e02\u7ade\u8d5b\u4e2d\u53d6\u5f97\u5148\u673a\u3002\u8be5\u516c\u53f8\u5728AI\u5b89\u5168\u9886\u57df\u4eab\u6709\u76db\u8a89\uff0c\u5176Claude\u7cfb\u5217\u6a21\u578b\u5728\u4f01\u4e1a\u5e02\u573a\u83b7\u5f97\u5e7f\u6cdb\u91c7\u7528\u3002"},
    {"title": "\u82f1\u4f1f\u8fbe\u5ba3\u5e03\u4e3a\u4e2a\u4eba\u7535\u8111\u63a8\u51fa\u5168\u65b0AI\u82af\u7247", "summary": "\u82f1\u4f1f\u8fbeCEO\u9ec4\u4ec1\u52cb\u5c06\u8fd9\u4e00\u4e3e\u63aa\u79f0\u4e3a\u8ba1\u7b97\u673a\u7684\u91cd\u751f\u3002\u65b0\u82af\u7247\u5c06\u4f7f\u4e2a\u4eba\u7535\u8111\u5177\u5907\u5f3a\u5927\u7684AI\u5904\u7406\u80fd\u529b\uff0c\u7528\u6237\u53ef\u4ee5\u5728\u672c\u5730\u8fd0\u884c\u5927\u8bed\u8a00\u6a21\u578b\u548c\u5176\u4ed6AI\u5e94\u7528\u3002"},
    {"title": "AI\u9a71\u52a8\u7684\u4f5c\u6218\u4e2d\u5fc3\u6210\u4e3a\u7f51\u7edc\u5b89\u5168\u65b0\u524d\u7ebf\u7684\u6838\u5fc3", "summary": "\u51e0\u5341\u5e74\u6765\uff0c\u7f51\u7edc\u9632\u5fa1\u7684\u65f6\u95f4\u7ebf\u4ee5\u6570\u5468\u6765\u8ba1\u7b97\u3002\u501f\u52a9AI\u9a71\u52a8\u7684\u4f5c\u6218\u4e2d\u5fc3\uff0c\u5b89\u5168\u56e2\u961f\u53ef\u4ee5\u5c06\u54cd\u5e94\u65f6\u95f4\u4ece\u6570\u5468\u7f29\u77ed\u5230\u6570\u5206\u949f\u3002"}
]

processed = []
for i, art in enumerate(articles):
    tr = translations[i]
    processed.append({
        "title": art["title"], "source": art.get("source", "Unknown"),
        "link": art.get("link", "#"), "date": art.get("date", ""),
        "trans_title": tr["title"], "trans_summary": tr["summary"],
        "model": "Default Model"
    })

def generate_html(news_items):
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>\u9ad8\u6821\u5206\u961f AI \u65b0\u95fb\u6bcf\u65e5\u7b80\u62a5 - {today_cn}</title>
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
        <h1>\ud83e\udd16 \u9ad8\u6821\u5206\u961f AI \u65b0\u95fb\u6bcf\u65e5\u7b80\u62a5</h1>
        <div class="date">{today_cn}\u65e9\u95f4\u7248 (\u5185\u5bb9\u52a8\u6001\u6293\u53d6\u81ea\u6743\u5a01\u5a92\u4f53)</div>
    </div>
    <div class="section">
"""
    for item in news_items:
        html += f"""
        <div class="news-item">
            <div class="news-title">{item['trans_title']}</div>
            <div class="news-meta">\ud83d\udcf0 \u6765\u6e90\uff1a{item['source']} | \u7ffb\u8bd1\u6a21\u578b\uff1a{item['model']}</div>
            <div class="news-summary">{item['trans_summary']}</div>
            <a class="news-link" href="{item['link']}" target="_blank">\ud83d\udd17 \u9605\u8bfb\u539f\u6587</a>
        </div>
"""
    html += f"""
    </div>
    <div class="footer">
        <p>\u672c\u7b80\u62a5\u7531\u65fa\u8d22Jarvis\u81ea\u52a8\u6293\u53d6\u4e0e\u7ffb\u8bd1\u751f\u6210</p>
        <p>\u751f\u6210\u65f6\u95f4\uff1a{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    </div>
</body>
</html>"""
    return html

print("Generating HTML...")
html_content = generate_html(processed)
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)
html_size = osmod.path.getsize(html_path)
print(f"HTML generated: {html_size} bytes ({len(processed)} articles)")
save_status("translate_html", True, f"HTML generated: {html_size} bytes, {len(processed)} articles")

# Send email
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587
EMAIL = "86940135@qq.com"
PASSWORD = "oepkunkbmboucadg"

TO_EMAILS = [
    "liuwei44259@huawei.com", "tiankunyang@huawei.com",
    "qinhongyi2@huawei.com", "jiawei18@huawei.com",
    "jiyingguo@huawei.com", "linfeng67@huawei.com",
    "lvluling1@huawei.com", "suqi1@huawei.com",
    "susha@huawei.com", "wangdongxiao@huawei.com",
    "xiongguifang@huawei.com", "xushengsheng@huawei.com",
    "zhangqianfeng2@huawei.com", "zhangyexing2@huawei.com",
    "86940135@qq.com"
]

subject = f"[{today}] \u9ad8\u6821\u5206\u961f AI \u65b0\u95fb\u6bcf\u65e5\u7b80\u62a5"

print("Sending emails...")
context = ssl.create_default_context()
success_count = 0
fail_count = 0
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30) as server:
        server.starttls(context=context)
        server.login(EMAIL, PASSWORD)
        for to_email in TO_EMAILS:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject
            msg["From"] = EMAIL
            msg["To"] = to_email
            plain_text = "\u9ad8\u6821\u5206\u961f AI \u65b0\u95fb\u6bcf\u65e5\u7b80\u62a5\n\u8bf7\u4f7f\u7528\u652f\u6301HTML\u7684\u90ae\u4ef6\u5ba2\u6237\u7aef\u67e5\u770b\u3002"
            msg.attach(MIMEText(plain_text, "plain", "utf-8"))
            msg.attach(MIMEText(html_content, "html", "utf-8"))
            try:
                server.sendmail(EMAIL, [to_email], msg.as_string())
                print(f"\u2705 Sent to {to_email}")
                success_count += 1
                time.sleep(1)
            except Exception as e:
                print(f"\u274c Failed to send to {to_email}: {e}")
                fail_count += 1
except Exception as e:
    print(f"SMTP Connection Error: {e}")

result_msg = f"Emails sent: {success_count} success, {fail_count} failed"
print(result_msg)
save_status("email", fail_count == 0, result_msg)

print(f"\n=== Summary ===")
print(f"HTML file size: {html_size} bytes")
print(f"Articles translated: {len(processed)}")
print(f"Email result: {success_count}/{len(TO_EMAILS)} delivered")

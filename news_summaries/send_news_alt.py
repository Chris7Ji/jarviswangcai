#!/usr/bin/env python3
"""Send OpenClaw news directly via QQ SMTP"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

with open("/Users/jiyingguo/.openclaw/workspace/news_summaries/openclaw_news_high_quality_2026-05-21.md", "r") as f:
    md_content = f.read()

html_body = md_content.replace("\n", "<br>\n")
html_body = f"<html><body style='font-family: sans-serif; line-height: 1.6; color: #333;'>{html_body}</body></html>"

msg = MIMEMultipart('alternative')
msg['Subject'] = Header('🦞 OpenClaw日报 - 2026年05月21日', 'utf-8')
msg['From'] = '86940135@qq.com'
msg['To'] = '86940135@qq.com, jiyingguo@huawei.com'
msg.attach(MIMEText(md_content, 'plain', 'utf-8'))
msg.attach(MIMEText(html_body, 'html', 'utf-8'))

try:
    server = smtplib.SMTP("smtp.qq.com", 587, timeout=30)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("86940135@qq.com", "icxhfzuyzbhbbjie")
    server.sendmail("86940135@qq.com", ["86940135@qq.com", "jiyingguo@huawei.com"], msg.as_string())
    server.quit()
    print("✅ Email sent via SMTP:587")
except Exception as e:
    print(f"❌ Port 587 failed: {e}")
    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465, timeout=30)
        server.login("86940135@qq.com", "icxhfzuyzbhbbjie")
        server.sendmail("86940135@qq.com", ["86940135@qq.com", "jiyingguo@huawei.com"], msg.as_string())
        server.quit()
        print("✅ Email sent via SMTP_SSL:465")
    except Exception as e2:
        print(f"❌ SSL also failed: {e2}")

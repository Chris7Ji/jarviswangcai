#!/usr/bin/env python3
"""Send OpenClaw daily report via QQ email"""
import os, smtplib, sys
from email.mime.text import MIMEText
from email.header import Header

PWD = "icxhfzuyzbhbbjie"

with open(os.path.expanduser("~/.openclaw/workspace/news_summaries/openclaw_news_high_quality_2026-05-21.md")) as f:
    content = f.read()

msg = MIMEText(content, "plain", "utf-8")
msg["Subject"] = Header("🦞 OpenClaw日报 - 2026年05月21日", "utf-8")
msg["From"] = "86940135@qq.com"
msg["To"] = "86940135@qq.com, jiyingguo@huawei.com"

try:
    s = smtplib.SMTP("smtp.qq.com", 587, timeout=30)
    s.ehlo(); s.starttls(); s.ehlo()
    s.login("86940135@qq.com", PWD)
    s.sendmail("86940135@qq.com", ["86940135@qq.com", "jiyingguo@huawei.com"], msg.as_string())
    s.quit()
    print("OK")
except Exception as e:
    print(f"587: {e}")
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465, timeout=30)
        s.login("86940135@qq.com", PWD)
        s.sendmail("86940135@qq.com", ["86940135@qq.com", "jiyingguo@huawei.com"], msg.as_string())
        s.quit()
        print("OK via 465")
    except Exception as e2:
        print(f"465: {e2}")

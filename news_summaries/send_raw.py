#!/usr/bin/env python3
"""Generate raw email and pipe to himalaya"""
import subprocess, os
from email.mime.text import MIMEText
from email.header import Header

with open(os.path.expanduser("~/.openclaw/workspace/news_summaries/openclaw_news_high_quality_2026-05-21.md")) as f:
    content = f.read()

msg = MIMEText(content, "plain", "utf-8")
msg["From"] = "86940135@qq.com"
msg["To"] = "86940135@qq.com, jiyingguo@huawei.com"
msg["Subject"] = Header("🦞 OpenClaw日报 - 2026年05月21日", "utf-8")
msg["Date"] = "Thu, 21 May 2026 06:00:00 +0800"

raw = msg.as_string()
proc = subprocess.run(["himalaya", "message", "send", "--account", "qq"],
                      input=raw, capture_output=True, text=True, timeout=30)
print("STDOUT:", proc.stdout)
print("STDERR:", proc.stderr)
print("RC:", proc.returncode)

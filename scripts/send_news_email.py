#!/usr/bin/env python3
"""Send HTML email with AI news briefing."""
import sys, smtplib, ssl, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <html_file> <subject>")
    sys.exit(1)

html_file = sys.argv[1]
subject = sys.argv[2]

with open(html_file, 'r', encoding='utf-8') as f:
    html_body = f.read()

context = ssl.create_default_context()
success_count = 0
fail_count = 0

try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=20) as server:
        server.starttls(context=context)
        server.login(EMAIL, PASSWORD)
        for to_email in TO_EMAILS:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject
            msg["From"] = EMAIL
            msg["To"] = to_email
            msg.attach(MIMEText("高校分队 AI 新闻每日简报，请使用支持HTML的邮件客户端查看。", "plain", "utf-8"))
            msg.attach(MIMEText(html_body, "html", "utf-8"))
            try:
                server.sendmail(EMAIL, [to_email], msg.as_string())
                print(f"✓ Sent to {to_email}")
                success_count += 1
                time.sleep(0.5)
            except Exception as e:
                print(f"✗ Failed to {to_email}: {e}")
                fail_count += 1
except Exception as e:
    print(f"✗ SMTP Connection Error: {e}")
    sys.exit(1)

print(f"\nDone. Success: {success_count}, Failed: {fail_count}")

#!/usr/bin/env python3
"""发送高校AI新闻简报HTML邮件"""
import smtplib, ssl, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587
EMAIL = "86940135@qq.com"
PASSWORD = "oepkunkbmboucadg"

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

# Read HTML
with open("/Users/jiyingguo/.openclaw/workspace/news_summaries/gaoxiao_news_2026-06-05.html", "r", encoding="utf-8") as f:
    html_content = f.read()

subject = "[2026-06-05] 高校分队 AI 新闻每日简报"

context = ssl.create_default_context()
success_count = 0
fail_count = 0

try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(EMAIL, PASSWORD)
        print("SMTP login successful")

        for to_email in TO_EMAILS:
            try:
                msg = MIMEMultipart("alternative")
                msg["Subject"] = subject
                msg["From"] = EMAIL
                msg["To"] = to_email
                plain = "高校AI新闻简报（请使用支持HTML的邮件客户端查看）"
                msg.attach(MIMEText(plain, "plain", "utf-8"))
                msg.attach(MIMEText(html_content, "html", "utf-8"))
                server.sendmail(EMAIL, [to_email], msg.as_string())
                print(f"✅ Sent to {to_email}")
                success_count += 1
                time.sleep(0.5)
            except Exception as e:
                print(f"❌ Failed to send to {to_email}: {e}")
                fail_count += 1
except Exception as e:
    print(f"SMTP Connection Error: {e}")

print(f"\nDone! Success: {success_count}, Failed: {fail_count}")

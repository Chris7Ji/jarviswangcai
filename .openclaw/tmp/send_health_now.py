import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

password = os.environ.get("EMAIL_PASSWORD", "")
if not password:
    print("ERROR: EMAIL_PASSWORD not set")
    exit(1)

html = open("/Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai/news_health.html", encoding="utf-8").read()

msg = MIMEMultipart("alternative")
msg["Subject"] = "🔬 健康长寿科研简报 2026-06-03"
msg["From"] = "86940135@qq.com"
msg["To"] = "86940135@qq.com"
msg.attach(MIMEText("请查看HTML版本或访问在线链接", "plain", "utf-8"))
msg.attach(MIMEText(html, "html", "utf-8"))

with smtplib.SMTP_SSL("smtp.qq.com", 465) as s:
    s.login("86940135@qq.com", password)
    s.sendmail("86940135@qq.com", ["86940135@qq.com"], msg.as_string())

print("✅ Email sent to 86940135@qq.com")

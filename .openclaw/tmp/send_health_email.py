import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_host = "smtp.qq.com"
smtp_port = 587
sender = "86940135@qq.com"
password = "***"
recipient = "86940135@qq.com"

html_content = open("/Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai/news_health.html", encoding="utf-8").read()

msg = MIMEMultipart('alternative')
msg['Subject'] = "🔬 健康长寿科研简报 2026-06-03"
msg['From'] = sender
msg['To'] = recipient
msg.attach(MIMEText('请查看HTML版本', 'plain', 'utf-8'))
msg.attach(MIMEText(html_content, 'html', 'utf-8'))

with smtplib.SMTP(smtp_host, smtp_port) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, [recipient], msg.as_string())
    print("Email sent successfully!")

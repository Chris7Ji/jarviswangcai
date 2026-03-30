#!/usr/bin/env python3
"""
简化版邮件发送脚本，只发送给少数几个收件人进行测试
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587
EMAIL = "86940135@qq.com"
PASSWORD = "icxhfzuyzbhbbjie"

# 只测试发送给2个邮箱
TO_EMAILS = [
    "jiyingguo@huawei.com",
    "86940135@qq.com"
]

HTML_CONTENT = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>测试邮件</title>
</head>
<body>
    <h1>测试邮件 - AI新闻简报</h1>
    <p>这是测试邮件内容，用于验证邮件发送功能。</p>
    <p>发送时间: 2026年3月30日</p>
</body>
</html>"""

def send_email(to_email, subject, html_body):
    """发送邮件函数"""
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = EMAIL
        msg["To"] = to_email
        
        # 纯文本版本
        plain_text = "测试邮件 - AI新闻简报\n\n请使用HTML格式查看完整内容。"
        msg.attach(MIMEText(plain_text, "plain", "utf-8"))
        
        # HTML版本
        msg.attach(MIMEText(html_body, "html", "utf-8"))
        
        # 创建SSL上下文
        context = ssl.create_default_context()
        
        # 尝试连接并发送
        print(f"正在连接到 {SMTP_SERVER}:{SMTP_PORT}...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30) as server:
            print("连接成功，启动TLS...")
            server.starttls(context=context)
            print("TLS启动成功，正在登录...")
            server.login(EMAIL, PASSWORD)
            print("登录成功，正在发送邮件...")
            server.sendmail(EMAIL, [to_email], msg.as_string())
            print(f"✓ 邮件已发送到 {to_email}")
            return True
            
    except Exception as e:
        print(f"✗ 发送到 {to_email} 失败: {e}")
        return False

def main():
    print("开始发送测试邮件...")
    subject = "[测试] AI新闻简报 - 2026年3月30日"
    
    sent_count = 0
    failed = []
    
    for to_email in TO_EMAILS:
        print(f"\n--- 处理 {to_email} ---")
        try:
            if send_email(to_email, subject, HTML_CONTENT):
                sent_count += 1
            else:
                failed.append(to_email)
        except Exception as e:
            print(f"处理 {to_email} 时发生异常: {e}")
            failed.append(to_email)
        
        # 邮件之间稍微等待一下
        if to_email != TO_EMAILS[-1]:
            time.sleep(2)
    
    print(f"\n=== 发送结果 ===")
    print(f"总计: {len(TO_EMAILS)}")
    print(f"成功: {sent_count}")
    print(f"失败: {len(failed)}")
    
    if failed:
        print(f"失败的邮箱: {failed}")
    
    return sent_count > 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
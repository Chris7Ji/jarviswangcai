import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = 'smtp.qq.com'
SMTP_PORT = 587
EMAIL = '86940135@qq.com'
PASSWORD = 'icxhfzuyzbhbbjie'

# 测试发送到第一个邮箱
TO_EMAIL = 'jiyingguo@huawei.com'

def send_test_email():
    msg = MIMEMultipart('alternative')
    msg['Subject'] = '测试邮件 - AI新闻简报'
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL
    
    plain_text = '测试邮件内容'
    html_body = '<html><body><h1>测试邮件</h1><p>这是测试邮件内容</p></body></html>'
    
    msg.attach(MIMEText(plain_text, 'plain', 'utf-8'))
    msg.attach(MIMEText(html_body, 'html', 'utf-8'))
    
    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, [TO_EMAIL], msg.as_string())
        print('测试邮件发送成功')

try:
    send_test_email()
    print('测试成功')
except Exception as e:
    print(f'测试失败: {e}')
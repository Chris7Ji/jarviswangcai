import smtplib
import ssl

SMTP_SERVER = 'smtp.qq.com'
SMTP_PORT = 465  # SSL端口
EMAIL = '86940135@qq.com'
PASSWORD = 'icxhfzuyzbhbbjie'

try:
    print("尝试使用SSL连接到SMTP服务器...")
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context, timeout=10)
    print("SSL连接成功")
    
    print("尝试登录...")
    server.login(EMAIL, PASSWORD)
    print("登录成功")
    
    server.quit()
    print("SMTP SSL测试成功")
    
except Exception as e:
    print(f"SMTP SSL测试失败: {e}")
    import traceback
    traceback.print_exc()
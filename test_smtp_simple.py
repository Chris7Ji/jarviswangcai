import smtplib
import ssl

SMTP_SERVER = 'smtp.qq.com'
SMTP_PORT = 587
EMAIL = '86940135@qq.com'
PASSWORD = 'icxhfzuyzbhbbjie'

try:
    print("尝试连接到SMTP服务器...")
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10)
    print("连接成功")
    
    print("启动TLS...")
    server.starttls(context=ssl.create_default_context())
    print("TLS启动成功")
    
    print("尝试登录...")
    server.login(EMAIL, PASSWORD)
    print("登录成功")
    
    server.quit()
    print("SMTP测试成功")
    
except Exception as e:
    print(f"SMTP测试失败: {e}")
    import traceback
    traceback.print_exc()
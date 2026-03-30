#!/usr/bin/env python3
"""
详细的SMTP测试
"""

import smtplib
import ssl
import socket

SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587
EMAIL = "86940135@qq.com"
PASSWORD = "icxhfzuyzbhbbjie"

def test_smtp_connection():
    print("=== 详细SMTP连接测试 ===")
    
    try:
        # 1. 创建socket连接
        print("1. 创建socket连接...")
        sock = socket.create_connection((SMTP_SERVER, SMTP_PORT), timeout=10)
        print(f"   ✓ Socket连接成功")
        
        # 2. 创建SMTP对象
        print("2. 创建SMTP对象...")
        server = smtplib.SMTP()
        server.sock = sock
        server.file = None  # 让SMTP自己创建file对象
        
        # 3. 获取欢迎消息
        print("3. 获取欢迎消息...")
        try:
            code, message = server.getreply()
            print(f"   ✓ 服务器响应: {code} {message}")
        except Exception as e:
            print(f"   ✗ 获取欢迎消息失败: {e}")
            # 继续尝试
        
        # 4. 启动TLS
        print("4. 启动TLS...")
        try:
            # 创建自定义SSL上下文
            context = ssl.create_default_context()
            context.minimum_version = ssl.TLSVersion.TLSv1_2
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE  # 暂时不验证证书
            
            server.starttls(context=context)
            print(f"   ✓ TLS启动成功")
        except Exception as e:
            print(f"   ✗ TLS启动失败: {e}")
            server.quit()
            return False
        
        # 5. 登录
        print("5. 尝试登录...")
        try:
            server.login(EMAIL, PASSWORD)
            print(f"   ✓ 登录成功")
        except Exception as e:
            print(f"   ✗ 登录失败: {e}")
            server.quit()
            return False
        
        # 6. 退出
        print("6. 退出...")
        server.quit()
        print(f"   ✓ 退出成功")
        
        print("\n✓ SMTP连接测试完全成功!")
        return True
        
    except Exception as e:
        print(f"\n✗ SMTP连接测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_smtplib_simple():
    print("\n=== 简单smtplib测试 ===")
    
    try:
        # 使用更长的超时时间
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30)
        print("1. SMTP对象创建成功")
        
        # 获取欢迎消息
        code, message = server.getreply()
        print(f"2. 服务器欢迎消息: {code} {message}")
        
        # 启动TLS
        context = ssl.create_default_context()
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        server.starttls(context=context)
        print("3. TLS启动成功")
        
        # 登录
        server.login(EMAIL, PASSWORD)
        print("4. 登录成功")
        
        server.quit()
        print("5. 退出成功")
        
        print("\n✓ 简单smtplib测试成功!")
        return True
        
    except Exception as e:
        print(f"\n✗ 简单smtplib测试失败: {e}")
        return False

if __name__ == "__main__":
    print(f"测试配置:")
    print(f"  SMTP服务器: {SMTP_SERVER}:{SMTP_PORT}")
    print(f"  邮箱: {EMAIL}")
    print(f"  密码: {'*' * len(PASSWORD)}")
    print()
    
    # 先测试详细版本
    if test_smtp_connection():
        print("\n✓ 所有测试通过!")
    else:
        print("\n尝试简单版本测试...")
        test_smtplib_simple()
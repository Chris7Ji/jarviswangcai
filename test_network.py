#!/usr/bin/env python3
"""
测试网络连接
"""

import socket
import ssl
import time

def test_connection(host, port, use_ssl=False):
    print(f"\n测试连接到 {host}:{port} (SSL: {use_ssl})...")
    
    try:
        start_time = time.time()
        
        if use_ssl:
            # 创建SSL上下文
            context = ssl.create_default_context()
            # 设置更兼容的TLS版本
            context.minimum_version = ssl.TLSVersion.TLSv1_2
            context.maximum_version = ssl.TLSVersion.TLSv1_3
            
            # 创建SSL socket
            with socket.create_connection((host, port), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    print(f"✓ SSL连接成功")
                    print(f"  SSL版本: {ssock.version()}")
                    print(f"  连接时间: {time.time() - start_time:.2f}秒")
                    return True
        else:
            # 普通TCP连接
            with socket.create_connection((host, port), timeout=10) as sock:
                print(f"✓ TCP连接成功")
                print(f"  连接时间: {time.time() - start_time:.2f}秒")
                
                # 尝试读取SMTP欢迎消息
                try:
                    sock.settimeout(5)
                    welcome = sock.recv(1024)
                    if welcome:
                        print(f"  服务器响应: {welcome.decode('utf-8', errors='ignore')[:100]}")
                except:
                    print(f"  无法读取服务器响应")
                
                return True
                
    except Exception as e:
        print(f"✗ 连接失败: {e}")
        return False

def main():
    print("=== 网络连接测试 ===")
    
    # 测试QQ邮箱SMTP
    test_connection("smtp.qq.com", 587, use_ssl=False)
    test_connection("smtp.qq.com", 465, use_ssl=True)
    
    # 测试其他常见服务
    test_connection("google.com", 443, use_ssl=True)
    test_connection("baidu.com", 443, use_ssl=True)
    
    print("\n=== 测试完成 ===")

if __name__ == "__main__":
    main()
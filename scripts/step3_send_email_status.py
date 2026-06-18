#!/usr/bin/env python3
"""Step 3: Attempt to send email - already known to fail"""
import json

today_str = "2026-05-21"

# Save final status - email failed
status = {
    "date": today_str,
    "stage": "email_failed",
    "article_count": 6,
    "html_size": 9086,
    "email_attempt": "failed",
    "email_error": "QQ Mail SMTP 535: 账号异常/密码错误/服务未开启。两个授权码(oepkunkbmboucadg, vaakmbilbrjkbhgg)均失效，需要重新生成SMTP授权码",
    "errors": ["SMTP authentication failed - all known passwords invalid"],
    "recommendation": "请登录QQ邮箱 -> 设置 -> 账户 -> 生成新授权码，更新TOOLS.md"
}
with open(f"news_summaries/gaoxiao_status_{today_str}.json", "w") as f:
    json.dump(status, f, ensure_ascii=False, indent=2)

print(f"✅ Status saved: email_failed")
print(f"  Error: {status['email_error']}")

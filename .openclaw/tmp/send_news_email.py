#!/usr/bin/env python3
import json
import smtplib
import ssl
import time
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 翻译后的新闻数据（由默认大模型翻译完成）
translated_news = [
    {
        "title": "10万美元签证费挡不住OpenAI、Anthropic和Nvidia争夺AI人才",
        "summary": "联邦数据显示，Anthropic、OpenAI和Nvidia在2026财年第二季度提交的H-1B签证新聘和续签申请数量较去年同期有所增加，而其他科技巨头则缩减了该计划。这表明即便面临高额签证费用，AI头部企业仍在激烈争夺全球顶尖AI人才，H-1B签证成为它们获取国际人才的关键通道。",
        "link": "https://www.businessinsider.com/h-1b-visa-filings-rise-for-anthropic-openai-nvidia-2026-6",
        "source": "Business Insider"
    },
    {
        "title": "Anthropic与Nvidia说服法官拆分作者AI版权诉讼案",
        "summary": "一群大型科技公司成功说服联邦法官，拆分了一桩指控它们盗版书籍用于构建AI模型的作者版权诉讼。法官认为，仅凭Anthropic、Google、Apple、Nvidia、Perplexity和xAI等公司使用相同的盗版书籍库这一指控，不足以将所有公司合并为同一诉讼。Meta和OpenAI最初也被列为被告，但相关索赔已被拆分处理。这一裁定对大型AI公司的版权纠纷策略有重要影响。",
        "link": "https://news.bloomberglaw.com/ip-law/anthropic-nvidia-sway-judge-to-split-authors-ai-copyright-suit",
        "source": "Bloomberg Law News"
    },
    {
        "title": "OpenAI紧随Anthropic提交美国IPO申请，AI巨头进军公开市场",
        "summary": "ChatGPT开发商OpenAI于周一秘密提交了美国首次公开募股（IPO）申请，紧随竞争对手Anthropic进军股票市场。OpenAI此前宣布以8400亿美元估值融资1100亿美元，投资方包括软银、亚马逊和Nvidia。IPO前OpenAI刚与微软重新谈判了合作伙伴关系，获准与亚马逊和Google等新伙伴建立合作。AI公司上市潮标志着行业进入新阶段。",
        "link": "https://www.reuters.com/technology/openai-files-us-ipo-after-anthropic-ai-giants-head-public-markets-2026-06-08/",
        "source": "Reuters"
    },
    {
        "title": "Anthropic发布Claude Fable 5：AI技术新突破",
        "summary": "Anthropic推出了目前最先进的AI模型Claude Fable 5，现已向公众开放。该模型基于受限版Mythos 5相同的技术基础，在性能上接近最强大的Claude Mythos模型，同时增强了安全特性。Fable 5内置了防止用户诱导其执行网络攻击或详细说明生物武器制造方法的安全防护措施，体现了Anthropic在AI安全领域的一贯重视。",
        "link": "https://www.startupecosystem.ca/news/anthropic-unveils-claude-fable-5-a-breakthrough-in-ai-technology/",
        "source": "Startup Ecosystem Canada"
    },
    {
        "title": "Perplexity计划2028年IPO，不受Anthropic和OpenAI影响",
        "summary": "AI搜索公司Perplexity计划在2028年上市，无论Anthropic和OpenAI的上市情况如何。CEO Aravind Srinivas接受CNBC采访时表示，Perplexity的IPO计划与这两家公司无关。他指出SpaceX本周的IPO将是Anthropic和OpenAI上市表现的重要先行指标。Perplexity此前已表示公司资金充裕，没有急于上市的计划。",
        "link": "https://www.reuters.com/business/perplexity-planning-ipo-2028-regardless-what-happens-anthropic-or-openai-ceo-2026-06-09/",
        "source": "Reuters"
    },
    {
        "title": "Anthropic发布最先进模型的降级安全版Fable 5",
        "summary": "Anthropic周二推出了一款面向普通用户的新型"Mythos级别"模型Fable 5。其表现与最先进的Claude Mythos模型水平相当，但内置了安全防护措施，防止用户诱导其执行网络攻击或详细说明生物武器制造方法。Mythos和OpenAI的GPT-5.5-Cyber等类似模型近期已推动美国政府采取行动，确保关键网络加强防御能力。",
        "link": "https://www.politico.com/news/2026/06/09/anthropic-makes-mythos-level-ai-model-available-to-the-public-00954829",
        "source": "Politico"
    }
]

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

SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587
EMAIL = "86940135@qq.com"
PASSWORD = "oepkunkbmboucadg"


def generate_html_email(news_items):
    today_str = datetime.now().strftime("%Y年%m月%d日")
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>高校分队 AI 新闻每日简报 - {today_str}</title>
    <style>
        body {{ font-family: 'Microsoft YaHei', Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f5f5f5; }}
        .header {{ background-color: #1a237e; color: white; padding: 20px; border-radius: 5px; margin-bottom: 20px; }}
        .header h1 {{ margin: 0; font-size: 24px; }}
        .header .date {{ margin-top: 5px; font-size: 14px; opacity: 0.9; }}
        .section {{ background-color: white; padding: 20px; margin-bottom: 20px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .news-item {{ margin-bottom: 20px; padding-bottom: 20px; border-bottom: 1px solid #eee; }}
        .news-item:last-child {{ border-bottom: none; }}
        .news-title {{ font-weight: bold; color: #1a237e; margin-bottom: 8px; font-size: 16px; }}
        .news-summary {{ color: #555; margin-bottom: 8px; font-size: 14px; line-height: 1.5; }}
        .news-link {{ color: #1976d2; text-decoration: none; font-size: 13px; font-weight: bold; }}
        .news-meta {{ color: #888; font-size: 12px; margin-bottom: 5px; }}
        .footer {{ text-align: center; color: #666; font-size: 12px; margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📡 高校分队 AI 新闻每日简报</h1>
        <div class="date">{today_str}早间版（内容由Tavily抓取，默认大模型翻译）</div>
    </div>
    <div class="section">
"""
    
    for i, item in enumerate(news_items):
        html += f"""
        <div class="news-item">
            <div class="news-title">{i+1}. {item['title']}</div>
            <div class="news-meta">来源：{item['source']}</div>
            <div class="news-summary">{item['summary']}</div>
            <a class="news-link" href="{item['link']}" target="_blank">🔗 点击阅读原文</a>
        </div>
        """

    html += f"""
    </div>
    <div class="footer">
        <p>本简报由旺财Jarvis自动抓取翻译生成</p>
        <p>生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        <p>⚠️ 注意：原脚本的翻译API（Gemini代理不通 / MiniMax余额不足 / DeepSeek key失效）均已不可用，已改用默认大模型翻译</p>
    </div>
</body>
</html>"""
    return html


def send_emails(to_emails, subject, html_body):
    context = ssl.create_default_context()
    success_count = 0
    fail_count = 0
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=20) as server:
            server.starttls(context=context)
            server.login(EMAIL, PASSWORD)
            
            for to_email in to_emails:
                msg = MIMEMultipart("alternative")
                msg["Subject"] = subject
                msg["From"] = EMAIL
                msg["To"] = to_email
                plain_text = "高校分队 AI 新闻每日简报\n请使用支持HTML的邮件客户端查看。"
                msg.attach(MIMEText(plain_text, "plain", "utf-8"))
                msg.attach(MIMEText(html_body, "html", "utf-8"))
                
                try:
                    server.sendmail(EMAIL, [to_email], msg.as_string())
                    print(f"✅ Sent to {to_email}")
                    success_count += 1
                    time.sleep(1)
                except Exception as e:
                    print(f"❌ Failed to send to {to_email}: {e}")
                    fail_count += 1
                    
    except Exception as e:
        print(f"❌ SMTP Connection Error: {e}")
        return 0, len(to_emails)
    
    return success_count, fail_count


def main():
    print(f"📰 准备发送 {len(translated_news)} 条翻译后的AI新闻...")
    
    print("📝 生成HTML邮件...")
    html_content = generate_html_email(translated_news)
    
    today_str = datetime.now().strftime("%Y-%m-%d")
    subject = f"[{today_str}] 高校分队 AI 新闻每日简报"
    
    print(f"📧 发送邮件到 {len(TO_EMAILS)} 位收件人...")
    success, fail = send_emails(TO_EMAILS, subject, html_content)
    
    print(f"\n📊 发送完成：成功 {success}，失败 {fail}")
    return success, fail


if __name__ == "__main__":
    main()

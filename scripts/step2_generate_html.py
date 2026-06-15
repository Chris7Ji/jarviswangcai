#!/usr/bin/env python3
"""
Step 2+3: Generate HTML with translations and send email
"""
import json
from datetime import datetime
import smtplib
import ssl
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

today_str = "2026-05-21"

# Load raw news
with open(f"news_summaries/gaoxiao_raw_{today_str}.json", "r") as f:
    raw_news = json.load(f)

# Pre-translated articles (using my own translation capability)
translations = [
    {
        "zh_title": "英伟达：最新动态与深度洞察",
        "zh_summary": "本文汇总了AI与处理器巨头英伟达的最新产品和公司动态。作为全球GPU市场的主导者，英伟达持续在AI算力领域发力，其Blackwell架构新品的推出进一步巩固了其在数据中心和AI训练市场的领先地位。投资者和开发者可以从中了解英伟达在深度学习、自动驾驶、高性能计算等领域的战略布局。"
    },
    {
        "zh_title": "OpenAI准备在未来数周内提交IPO申请",
        "zh_summary": "据《纽约时报》报道，OpenAI正准备在未来几周内提交首次公开募股（IPO）申请。这将是硅谷多年来最受期待的IPO之一，也是AI行业商业化的标志性事件。OpenAI作为ChatGPT的母公司，其上市将吸引全球资本关注，并可能带动整个AI赛道的估值重估。2026年预计将成为硅谷IPO大年，OpenAI无疑是其中最重要的玩家之一。"
    },
    {
        "zh_title": "OpenAI领跑AI公司IPO竞赛：抢先上市至关重要",
        "zh_summary": "CNBC报道指出，在多家AI公司争相上市的竞赛中，OpenAI已占据领先地位。据悉，这家AI巨头和ChatGPT的所有者最早可能于本周提交机密IPO文件。业内人士分析认为，'抢先登陆公开市场'对于AI公司而言至关重要，不仅是融资需求，更是在品牌影响力、人才吸引和行业标准制定方面的战略制高点。"
    },
    {
        "zh_title": "康奈尔法学院通过与AI公司合作扩大法律AI领导地位",
        "zh_summary": "康奈尔法学院正在通过跟Harvey和Legora两家快速增长的AI公司建立新合作伙伴关系，进一步扩展其在法律科技教育领域的领导地位。这标志着AI在法律行业的应用正从简单的文档处理向更复杂的法律推理和案件分析迈进，高校法学院也在积极拥抱这一变革，培养具备AI素养的新一代法律人才。"
    },
    {
        "zh_title": "谷歌为搜索的AI时代推出新一代广告格式",
        "zh_summary": "谷歌宣布在搜索中推出基于Gemini模型构建的新广告格式，并扩大面向购物者的Direct Offers试点项目。这意味着AI将重塑在线广告的呈现方式和用户体验，广告将更加智能化、个性化。Gemini模型的引入让谷歌能够更精准地理解用户搜索意图，从而展示更具相关性的广告内容，可能改变数字广告产业的格局。"
    },
    {
        "zh_title": "Meta裁员8000人，战略重心全面转向AI",
        "zh_summary": "据NPR报道，Facebook和Instagram的母公司Meta已裁减8000个工作岗位，以全力向人工智能转型。尽管Meta在AI领域投入了巨额资金，但在与OpenAI、谷歌等竞争对手的较量中仍处于追赶状态。此次大规模裁员反映了硅谷科技巨头在AI时代的洗牌趋势——企业纷纷削减传统业务部门，将资源集中投入到AI这一决定了未来竞争力的关键技术领域。"
    }
]

# Build processed news
processed_news = []
for i, (item, trans) in enumerate(zip(raw_news, translations)):
    processed = {
        "title": item["title"],
        "snippet": item.get("snippet", ""),
        "link": item["link"],
        "source": item.get("source", "Unknown"),
        "date": item.get("date", ""),
        "published_at": item.get("published_at", ""),
        "trans_title": trans["zh_title"],
        "trans_summary": trans["zh_summary"],
        "model": "DeepSeek V4 Flash (旺财Jarvis)"
    }
    processed_news.append(processed)

# Save translated JSON
with open(f"news_summaries/gaoxiao_translated_{today_str}.json", "w") as f:
    json.dump(processed_news, f, ensure_ascii=False, indent=2)

print(f"✅ Translated and saved {len(processed_news)} articles")

# Generate HTML
today_display = datetime.now().strftime("%Y年%m月%d日")

html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>高校分队 AI 新闻每日简报 - {today_display}</title>
    <style>
        body {{ font-family: 'Microsoft YaHei', Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f5f5f5; }}
        .header {{ background: linear-gradient(135deg, #1a237e 0%, #283593 100%); color: white; padding: 25px 20px; border-radius: 8px; margin-bottom: 20px; }}
        .header h1 {{ margin: 0; font-size: 24px; }}
        .header .sub {{ margin-top: 5px; font-size: 14px; opacity: 0.9; }}
        .header .badge {{ display: inline-block; background: #ffd740; color: #1a237e; padding: 2px 10px; border-radius: 10px; font-size: 12px; font-weight: bold; margin-top: 8px; }}
        .section {{ background-color: white; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
        .news-item {{ margin-bottom: 22px; padding-bottom: 22px; border-bottom: 1px solid #e0e0e0; }}
        .news-item:last-child {{ border-bottom: none; margin-bottom: 0; padding-bottom: 0; }}
        .news-title {{ font-weight: bold; color: #1a237e; margin-bottom: 8px; font-size: 16px; line-height: 1.4; }}
        .news-summary {{ color: #444; margin-bottom: 8px; font-size: 14px; line-height: 1.6; }}
        .news-link {{ color: #1976d2; text-decoration: none; font-size: 13px; font-weight: bold; }}
        .news-link:hover {{ text-decoration: underline; }}
        .news-meta {{ color: #888; font-size: 12px; }}
        .news-meta span {{ margin-right: 12px; }}
        .footer {{ text-align: center; color: #999; font-size: 11px; margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; }}
        .footer .powered {{ color: #1a237e; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📡 高校分队 AI 新闻每日简报</h1>
        <div class="sub">{today_display} · 早间版</div>
        <div class="badge">🔍 真实文章链接 · 告别假链接</div>
    </div>
    <div class="section">
"""

news_titles_en = [
    "Nvidia: Latest news and insights",
    "OpenAI Prepares to File to Go Public in Coming Weeks",
    "OpenAI takes the lead in AI IPO horse race",
    "Cornell Law Expands Leadership in Legal AI",
    "A new generation of ads for the AI era of Search",
    "Meta slashes 8,000 jobs as it pivots towards AI"
]

for i, item in enumerate(processed_news):
    html += f"""
        <div class="news-item">
            <div class="news-title">📌 {i+1}. {item['trans_title']}</div>
            <div class="news-meta">
                <span>📰 来源：{item['source']}</span>
                <span>🤖 翻译：{item['model']}</span>
                <span>🕐 {item['date']}</span>
            </div>
            <div class="news-summary">{item['trans_summary']}</div>
            <a class="news-link" href="{item['link']}" target="_blank">🔗 阅读原文 →</a>
            <div style="color:#aaa;font-size:11px;margin-top:4px;">EN: {news_titles_en[i]}</div>
        </div>
        """

html += f"""
    </div>
    <div class="footer">
        <p>本简报由 <span class="powered">旺财Jarvis 🤖🐶</span> 自动抓取真实文章链接生成</p>
        <p>数据来源：SerpAPI / 各新闻媒体 | 生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    </div>
</body>
</html>"""

# Save HTML
html_path = f"news_summaries/gaoxiao_news_{today_str}.html"
with open(html_path, "w") as f:
    f.write(html)
html_size = len(html.encode())
print(f"✅ HTML generated: {html_size} bytes ({len(processed_news)} articles)")
print(f"   Saved to: {html_path}")

# Save status
status = {
    "date": today_str,
    "stage": "html_generated",
    "article_count": len(processed_news),
    "html_size": html_size,
    "errors": []
}
with open(f"news_summaries/gaoxiao_status_{today_str}.json", "w") as f:
    json.dump(status, f, ensure_ascii=False, indent=2)
print(f"✅ Status updated to html_generated")

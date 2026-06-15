#!/usr/bin/env python3
"""Update today's news with Chinese translations and regenerate HTML."""
import json
import subprocess
import sys
import os
from datetime import datetime

WORKSPACE = "/Users/jiyingguo/.openclaw/workspace"
DB_PATH = f"{WORKSPACE}/news_data/news_db.json"
REPO_DIR = f"{WORKSPACE}/jiaviswangcai.ai"

# Chinese translations for today's 9 articles
translations = [
    {
        "title": "SpaceX、OpenAI和Anthropic争相冲刺上市",
        "summary": "SpaceX、OpenAI和Anthropic这三家AI领域巨头正争相测试投资者对股票市场的兴趣。它们各自准备首次公开募股（IPO），标志着AI行业从私募市场向公开资本市场的重大转变。"
    },
    {
        "title": "Gemini for Science：AI实验工具开启科学探索新时代",
        "summary": "Google推出全新Gemini for Science计划，发布多项AI实验工具帮助科研人员进行科学发现。包括Google Antigravity中的科学技能以及Google Labs上的三个实验性工具，旨在加速科学研究进程。"
    },
    {
        "title": "Anthropic新咨询部门完成首次收购",
        "summary": "由Blackstone、Anthropic PBC和Hellman & Friedman联合投资的新AI企业服务公司，完成了对旧金山一家公司的首次收购。这标志着Anthropic从模型开发商向企业服务生态的扩展迈出重要一步。"
    },
    {
        "title": "英伟达公布创纪录利润583亿美元，AI芯片需求持续火爆",
        "summary": "芯片巨头英伟达宣布800亿美元股票回购计划和股息上调，为股东带来丰厚回报。受AI芯片需求持续增长的推动，公司营收和利润均创下历史新高。"
    },
    {
        "title": "英伟达发布2027财年第一季度财报：营收816亿美元",
        "summary": "英伟达（NASDAQ: NVDA）公布截至2026年4月26日的第一季度财报，创下816亿美元的季度营收纪录，环比增长20%，同比增长显著。AI训练和推理芯片需求是主要增长驱动力。"
    },
    {
        "title": "AI缩放定律新方法有望改变模型训练方式",
        "summary": "斯坦福HAI研究院的研究人员借鉴测量科学和教育领域的统计学概念，大幅降低了预测模型性能扩展规律所需的计算资源需求。这一突破可能改变未来AI模型的训练策略和资源配置。"
    },
    {
        "title": "英伟达最新动态：产品与公司新闻概览",
        "summary": "本文汇总了AI和处理器巨头英伟达的最新产品发布和公司新闻，帮助投资者和技术爱好者全面了解这家芯片巨头的最近动向。"
    },
    {
        "title": "五角大楼据报计划采用并武器化最新AI模型",
        "summary": "报道称，五角大楼计划将具备网络攻击能力的最新AI模型用于军事目的，其中可能涉及Anthropic的Claude Mythos Preview模型，尽管该公司已被标记为供应链风险。"
    },
    {
        "title": "英伟达财报后值得买入吗？分析师深度解读",
        "summary": "英伟达预计本季度销售额同比增长高达95%，而且这还不包括中国市场的收入。投资者正在评估在创纪录的财报发布后，英伟达股票是否仍然值得买入。"
    }
]

# Load DB
with open(DB_PATH, 'r', encoding='utf-8') as f:
    db = json.load(f)

today = "2026-05-21"
if today not in db["news_by_date"]:
    print(f"ERROR: {today} not in news_by_date!")
    sys.exit(1)

items = db["news_by_date"][today]
print(f"Updating {len(items)} items with Chinese translations...")

for i, item in enumerate(items):
    if i < len(translations):
        item["title"] = translations[i]["title"]
        item["summary"] = translations[i]["summary"]

# Save updated DB
with open(DB_PATH, 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print(f"DB updated. File size: {os.path.getsize(DB_PATH)} bytes")

# Generate HTML
sys.path.insert(0, f"{WORKSPACE}/news_data")
from auto_news_v2 import generate_html

dates = sorted(db.get("news_by_date", {}).keys(), reverse=True)
dates = dates[:15]
for date_str in dates:
    day_items = db["news_by_date"][date_str]
    generate_html(date_str, day_items)

print("HTML regenerated.")
print("DONE")

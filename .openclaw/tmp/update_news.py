#!/usr/bin/env python3
"""Update news_db.json with Chinese translations for 2026-05-29, then regenerate HTML"""
import json, sys

db_path = "/Users/jiyingguo/.openclaw/workspace/news_data/news_db.json"

with open(db_path, 'r') as f:
    db = json.load(f)

today = db['news_by_date']['2026-05-29']

translations = {
    0: {
        "title": "Anthropic超越OpenAI成为最具价值AI初创公司，估值逼近万亿美元",
        "summary": "Anthropic在最新一轮650亿美元融资后估值接近1万亿美元，超越OpenAI成为硅谷最具价值的AI初创公司，标志着AI行业竞争格局的重大转变。"
    },
    1: {
        "title": "部分日本银行获准使用OpenAI最新模型",
        "summary": "部分日本金融机构将获得OpenAI最新AI模型的使用权限，以加强网络安全防御能力，应对日益增长的网络威胁和金融安全挑战。"
    },
    2: {
        "title": "Anthropic超越OpenAI，成为全球最有价值的AI初创公司",
        "summary": "Anthropic通过新一轮650亿美元融资，估值达9000亿美元，超过OpenAI的7300亿美元估值。两家AI巨头之间的竞争日趋白热化，行业格局正在重塑。"
    },
    3: {
        "title": "AI芯片最新动态：AI通过数字劳动力转型工业维护",
        "summary": "Ultimo推出扩展版数字工人套件，利用AI技术彻底改变工业维护领域，为企业提供更智能的资产管理解决方案，标志着AI在工业领域的深入应用。"
    },
    4: {
        "title": "OpenAI新模型获准向部分日本银行开放",
        "summary": "部分日本金融机构已获得OpenAI GPT-5.5模型的访问权限，用于防御网络攻击和提升金融安全防御能力，这是AI在金融安全领域的重要应用。"
    },
    5: {
        "title": "AI驱动的营销技术最新动态与产品发布",
        "summary": "Quattr发布AI落地页生成器，弥合付费广告与搜索可见性之间的差距，创建与用户意图高度匹配的内容，为营销技术领域带来新变革。"
    },
    6: {
        "title": "Anthropic最新融资估值达9650亿美元，超越OpenAI",
        "summary": "Anthropic完成650亿美元融资后估值达9650亿美元，超越OpenAI。其新推出的Mythos模型在引发市场关注的同时，也带来了网络安全方面的担忧。"
    },
    7: {
        "title": "Anthropic估值达9650亿美元，超越OpenAI成为全球最有价值AI公司",
        "summary": "Claude母公司Anthropic最新一轮融资650亿美元，估值达9650亿美元，超越OpenAI成为全球最有价值AI公司，彰显AI行业仍有巨额资金持续涌入。"
    }
}

for i, article in enumerate(today):
    if i in translations:
        article['title'] = translations[i]['title']
        article['summary'] = translations[i]['summary']

# Also ensure article_date is clean
for a in today:
    a['date'] = '2026-05-29'

with open(db_path, 'w') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print(f"✅ Updated {len(today)} articles with Chinese translations")
print(f"✅ news_db.json saved ({len(json.dumps(db, ensure_ascii=False))} bytes)")

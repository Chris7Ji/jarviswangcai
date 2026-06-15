import json
from datetime import datetime

# Read raw news
with open('/Users/jiyingguo/.openclaw/workspace/news_data/raw_news_2026-05-31.json', 'r', encoding='utf-8') as f:
    raw_news = json.load(f)

# Translated and summarized articles (done by my default model)
translations = [
    {
        "title": "英伟达（NVDA）股价报价与市场预测",
        "summary": "CNN提供英伟达公司（NVDA）股票报价、财务信息、实时预测及公司新闻。随着AI芯片需求持续旺盛，英伟达作为AI算力核心供应商，其股价表现成为市场关注焦点，投资者密切关注其增长潜力。"
    },
    {
        "title": "英伟达最新产品或颠覆行业格局",
        "summary": "截至5月29日，英伟达（NVDA）股价年内已上涨约15.44%，大幅跑赢标普500指数。分析师指出，英伟达即将推出的重磅新品有望进一步巩固其在AI芯片领域的领导地位，推动股价继续走高。"
    },
    {
        "title": "迈克尔·伯里称Adobe为绝佳机会，看好Firefly与AI合作",
        "summary": "《大空头》主角迈克尔·伯里分析认为，尽管市场担忧AI可能颠覆Adobe的核心创意软件业务，但其未来前景比市场预期更强劲。他特别看好Adobe Firefly与OpenAI、Google的AI合作战略布局。"
    },
    {
        "title": "首款搭载英伟达芯片的Windows PC将于下周亮相",
        "summary": "据Axios报道，英伟达与微软预计下周联合推出首款搭载英伟达芯片的Windows PC，这标志着英伟达正式进入PC处理器市场，有望打破英特尔和AMD在PC芯片领域的长期垄断格局。"
    },
    {
        "title": "AI已来，你希望它为你做什么？",
        "summary": "《金融时报》向全球读者发出邀请，呼吁公众分享对AI未来的愿景与期待。这反映了AI技术的发展已进入全民参与阶段，社会各界对AI方向的讨论变得越来越重要。"
    },
    {
        "title": "Anthropic为亚马逊和谷歌带来重磅利好",
        "summary": "AI初创公司Anthropic完成650亿美元融资，估值达9650亿美元，同时发布新一代模型Claude Opus 4.8。作为亚马逊和Alphabet的重要投资标的，Anthropic的强劲表现验证了两大巨头在AI领域的战略布局。"
    },
    {
        "title": "美国首所AI高中：出人意料地充满人文关怀",
        "summary": "评论文章指出，学校不应像创业公司般运作，孩子的思维不应受市场波动左右。美国首所AI高中的实践表明，在融入人工智能教育的同时，仍然可以保持对学生人文素养和独立思考能力的重视。"
    },
    {
        "title": "Jabil借助AI基础设施增长，股价超越预期目标",
        "summary": "Jabil智能基础设施部门营收同比增长52%，AI数据中心和网络设备需求成为主要驱动力。AI基础设施建设热潮推动公司业绩超预期，股价表现强劲，反映了AI硬件市场的持续繁荣。"
    },
    {
        "title": "AI助力帕金森症音乐家完成新专辑创作",
        "summary": "一位伦敦唱作人因帕金森病无法再弹吉他，借助AI音乐生成技术继续创作和录制音乐。这一感人故事展示了AI在医疗辅助和艺术创作中的温暖应用，让人看到技术的人文关怀。"
    },
    {
        "title": "AI不必然导致裁员，人机协作才是未来",
        "summary": "法国跨国企业施耐德电气在制造业中采用AI的主要目的是提升工人效率而非替代人力。这一案例表明AI与就业并非零和博弈，企业可选择人机协作之路，让AI成为生产力倍增器。"
    }
]

# Build today's entries
today = "2026-05-31"
entries = []
for i, r in enumerate(raw_news):
    t = translations[i]
    entries.append({
        "title": t["title"],
        "summary": t["summary"],
        "url": r["url"],
        "source": r["source"],
        "date": today,
        "article_date": r.get("date", "")
    })

# Read existing db
with open('/Users/jiyingguo/.openclaw/workspace/news_data/news_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# Update today's entries
db["news_by_date"][today] = entries
db["last_updated"] = datetime.now().isoformat()

# Write back
with open('/Users/jiyingguo/.openclaw/workspace/news_data/news_db.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print(f"✅ Updated {len(entries)} translated entries for {today}")
print(f"✅ news_db.json saved ({len(db['news_by_date'])} dates total)")

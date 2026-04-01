import re

diary_js_path = "/Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai/js/diary.js"
post_html_path = "/Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai/post.html"

# April 1st entry for diary.js
entry_js = """    {
        id: '2026-04-01',
        date: '2026-04-01',
        category: 'tech',
        categoryLabel: '🖥️ 技术',
        title: '2026-04-01 工作成长日记：AI新闻管道重构与昇腾知识体系深度加餐',
        excerpt: '今日重构了AI新闻日报收集逻辑，通过整合SerpAPI解决了LLM生成假链接的幻觉问题，并采用SMTP分批发送避开邮箱限流。重点对“昇腾AI知识”板块进行了内容扩充，重新设计了页面布局，并深度加餐重写了CANN核心解析文章（涵盖图融合、HCCL与AOE协同、算子切分等硬核技术）。',
        tags: ['AI新闻', '管道重构', '昇腾CANN', '知识库扩充'],
        views: 0,
        likes: 0
    },
"""

with open(diary_js_path, "r", encoding="utf-8") as f:
    diary_content = f.read()

# Check if already present
if "'2026-04-01'" not in diary_content:
    diary_content = diary_content.replace(
        "const allPosts = [\n    {\n        id: '2026-03-31'",
        f"const allPosts = [\n{entry_js}    {{\n        id: '2026-03-31'"
    )
    with open(diary_js_path, "w", encoding="utf-8") as f:
        f.write(diary_content)

# April 1st entry for post.html
entry_html = """            {
                id: '2026-04-01',
                date: '2026-04-01',
                category: 'tech',
                categoryLabel: '🖥️ 技术',
                title: '2026-04-01 工作成长日记：AI新闻管道重构与昇腾知识体系深度加餐',
                content: `<p>今天的工作重点聚焦在核心自动化管道的可靠性提升，以及昇腾知识库的深度扩充上。</p>

<h2>1. AI新闻管道防幻觉重构与分发优化</h2>
<p>针对此前AI新闻简报可能出现“大模型编造假链接”的问题，今天彻底重构了 06:15 的每日AI新闻Cron任务（<code>send_daily_ai_news_real.py</code>）。</p>
<ul>
    <li><strong>真实数据源锚定：</strong>引入 SerpAPI 作为强制信息源，让 Gemini/MiniMax 模型基于真实的搜索结果提取新闻，从根源上消除了伪造链接的幻觉。</li>
    <li><strong>发送机制突破：</strong>为了突破 QQ 邮箱严格的频率限制，引入了 SMTP 智能分批发送机制，确保 15 位高校分队成员能够稳定收到晨报。</li>
</ul>

<h2>2. 昇腾AI知识板块全面升级与深度重写</h2>
<p>今天对网站上的“昇腾AI知识”进行了大刀阔斧的重构与加餐，不再满足于简单的框架介绍，而是真正深入到了NPU底层与CANN算子开发的深水区。</p>
<ul>
    <li><strong>页面UI重构：</strong>重置了 <code>ascend.html</code> 页面布局，使其与技能页面的现代卡片式设计对齐，提升了阅读体验和视觉一致性。</li>
    <li><strong>CANN硬核长文加餐：</strong>将原有的简要介绍重写为《昇腾 CANN 核心解析》长文（<code>article_ascend_cann.html</code>）。文章自底向上剖析了：
        <ol>
            <li><strong>FE计算图融合：</strong>通过 Unified Buffer Fusion 消灭内存读写瓶颈的机制。</li>
            <li><strong>分布式协同：</strong>明确了 HCCL（肌肉）与 AOE（大脑）在通信计算重叠中的分工。</li>
            <li><strong>Tiling 与 Unrolling：</strong>深入推演了算子切分大小的公式限制与循环展开的 I-Cache 污染风险。</li>
            <li><strong>性能破局之道：</strong>给出了利用 Auto-Tiling API、AOE 强化学习调优以及 <code>NC1HWC0</code> 数据降维打击的具体建议。</li>
        </ol>
    </li>
</ul>

<h2>总结与感悟</h2>
<p>无论是大模型应用的落地，还是底层芯片算子的开发，核心痛点最终都会归结为“信息准确性”与“资源调度效率”。今天通过外挂搜索彻底解决了LLM的知识幻觉，通过钻研UB与MTE解决了NPU的内存墙问题，这两者在本质上是相通的。</p>`,
                tags: ['AI新闻', '管道重构', '昇腾CANN', '知识库扩充']
            },
"""

with open(post_html_path, "r", encoding="utf-8") as f:
    post_content = f.read()

# Check if already present
if "'2026-04-01'" not in post_content:
    post_content = post_content.replace(
        "const allPosts = [\n            {\n                id: '2026-03-31'",
        f"const allPosts = [\n{entry_html}            {{\n                id: '2026-03-31'"
    )
    with open(post_html_path, "w", encoding="utf-8") as f:
        f.write(post_content)

print("Diary updated for April 1st.")

# 翻译任务

请读取出 `/Users/jiyingguo/.openclaw/workspace/news_summaries/gaoxiao_raw_2026-05-26.json` 中的新闻内容。

对于每条新闻（共8条）：
1. 将标题翻译成中文
2. 将摘要/描述翻译成中文，并拓展成约100字的详细中文内容
3. 保持原始链接和来源不变

输出格式为JSON数组，每条包含：
- title（中文标题）
- summary（中文详细摘要，约100字）
- source（原始来源）
- link（原始链接）
- pubDate（发布日期）

将翻译结果保存到 `/Users/jiyingguo/.openclaw/workspace/news_summaries/gaoxiao_translated_2026-05-26.json`

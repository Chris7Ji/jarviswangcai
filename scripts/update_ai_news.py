#!/usr/bin/env python3
"""
自动更新 AI 新闻日报 (news.html) 脚本
每天运行：搜索最新 AI 新闻 → 格式化 → 合并到 news.html → Git 提交推送

用法：
    python3 update_ai_news.py                    # 正常模式（搜索+合并）
    python3 update_ai_news.py --no-push          # 搜索+生成，不推送
"""

import json, os, re, sys, shutil, subprocess
from datetime import datetime, timedelta
from urllib.parse import quote
import urllib.request, urllib.error

# ── 路径 ──
WORKSPACE = os.path.expanduser("~/.openclaw/workspace")
NEWS_HTML = os.path.join(WORKSPACE, "jiaviswangcai.ai", "news.html")
SITE_DIR = os.path.join(WORKSPACE, "jiaviswangcai.ai")
NEWS_DIR = os.path.join(WORKSPACE, "news_summaries")
os.makedirs(NEWS_DIR, exist_ok=True)

# ── API Keys ──
SERPAPI_KEY = "b28c2426b9015470508315f27a6782b552a5a5b39550fbc9b62ff381e67c360f"
TAVILY_KEY = "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"

# ── 配置 ──
MAX_DAYS = 14          # 保留最近天数
MAX_ARTICLES = 8       # 每天最多展示条数

# ── 搜索关键词 ──
SEARCH_QUERIES = [
    "AI technology latest news 2026",
    "artificial intelligence breakthrough",
    "large language model update",
    "NVIDIA AI GPU news",
    "OpenAI Anthropic Google AI",
]


def search_tavily(query, max_results=6):
    """Tavily 搜索（主力）"""
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": TAVILY_KEY,
        "query": query,
        "search_depth": "basic",
        "max_results": max_results,
        "include_answer": False,
    }
    try:
        data = json.dumps(payload).encode()
        req = urllib.request.Request(url, data=data,
            headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read())
        return [{
            "title": r.get("title", ""),
            "content": r.get("content", ""),
            "url": r.get("url", ""),
            "source": r.get("source", r.get("domain", "AI News")),
        } for r in result.get("results", [])[:max_results]]
    except Exception as e:
        print(f"  ⚠️ Tavily: {e}")
        return []


def search_serpapi(query, num=8):
    """SerpAPI 搜索（备用）"""
    params = {
        "q": query, "api_key": SERPAPI_KEY,
        "engine": "google", "tbm": "nws",
        "num": num, "hl": "en", "gl": "us",
    }
    url = "https://serpapi.com/search?" + "&".join(
        f"{k}={quote(str(v))}" for k, v in params.items()
    )
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        results = data.get("news_results", data.get("organic_results", []))
        return [{
            "title": r.get("title", ""),
            "content": r.get("snippet", ""),
            "url": r.get("link", ""),
            "source": r.get("source", r.get("publication", "")),
        } for r in results[:num]]
    except Exception as e:
        print(f"  ⚠️ SerpAPI: {e}")
        return []


def fetch_news():
    """多引擎搜新闻，去重后返回"""
    seen = set()
    all_articles = []

    for query in SEARCH_QUERIES:
        articles = search_tavily(query)
        if not articles:
            articles = search_serpapi(query)

        for a in articles:
            url = a.get("url", "")
            if url and url not in seen:
                seen.add(url)
                all_articles.append({
                    "title": a["title"],
                    "summary": a.get("content", ""),
                    "link": url,
                    "source": str(a.get("source", "AI News")),
                    "date": datetime.now().strftime("%Y-%m-%d"),
                })

    print(f"  ✅ 搜索到 {len(all_articles)} 条唯一新闻")
    return all_articles[:MAX_ARTICLES]


def escape(s):
    """HTML 转义"""
    if not s: return ""
    return (s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
            .replace('"',"&quot;").replace("'","&#39;"))


def make_pill(date_str, first=False):
    """生成日期按钮"""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    label = f"{dt.month}月{dt.day}日" + (" (最新)" if first else "")
    active = " active" if first else ""
    return f'<button class="date-pill{active}" data-date="{date_str}" onclick="showDate(\'{date_str}\')">{label}</button>'


def make_container(date_str, articles, first=False):
    """生成单日新闻 HTML"""
    active = " active" if first else ""
    parts = [
        f'<div id="news-{date_str}" class="day-news-container{active}">',
        f'<div class="update-info"><p>📅 日报日期: {date_str} · 共 {len(articles)} 条资讯</p></div>']

    if articles:
        a = articles[0]
        parts += [
            '<div class="featured-news">',
            '<span class="tag">🔥 重点头条</span>',
            f'<h2>{escape(a["title"])}</h2>',
            f'<p class="summary">{escape(a["summary"])}</p>',
            '<div class="meta" style="margin-top:1rem;font-size:0.9rem;">',
            f'<div><span class="source">{escape(a["source"])}</span></div>',
            f'<a href="{escape(a["link"])}" target="_blank" '
            f'style="color:#667eea;font-weight:bold;">阅读原文 →</a>',
            '</div></div>']

    rest = articles[1:]
    if rest:
        parts += ['<h3 class="news-section-title">📰 更多资讯</h3>',
                  '<div class="news-grid">']
        for a in rest:
            parts += [
                f'<a href="{escape(a["link"])}" target="_blank" class="news-item">',
                f'<h3>{escape(a["title"])}</h3>',
                f'<p>{escape(a["summary"])}</p>',
                '<div class="meta">',
                f'<div><span class="source">{escape(a["source"])}</span></div>',
                '<span>阅读原文 &rarr;</span>',
                '</div></a>']
        parts.append('</div>')

    parts.append('</div>')
    return "\n".join(parts)


def rebuild_html(today, new_container_html):
    """重建 news.html：合并新数据 + 保留最近 MAX_DAYS 天"""
    with open(NEWS_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # ── 解析已有容器 ──
    containers = {}
    for m in re.finditer(
        r'<div id="news-(\d{4}-\d{2}-\d{2})" class="day-news-container[^"]*">',
        html
    ):
        date_s = m.group(1)
        start = m.start()
        # 找结束位置：下一个容器或 footer
        next_m = re.search(
            r'<div id="news-\d{4}-\d{2}-\d{2}" class="day-news-container[^"]*">',
            html[m.end():]
        )
        end = m.end() + next_m.start() if next_m else html.find("<footer>", m.end())
        if end < 0: end = len(html)
        containers[date_s] = html[start:end].rstrip()

    # ── 合并 ──
    containers[today] = new_container_html

    # 排序：最新在前
    sorted_dates = sorted(containers.keys(), reverse=True)[:MAX_DAYS]

    # ── 重构 date-pills ──
    pills = '\n'.join(
        "        " + make_pill(d, first=(i == 0))
        for i, d in enumerate(sorted_dates)
    )
    pills_block = f'        <div class="date-pills" id="datePillsContainer">\n{pills}\n            \n        </div>'

    # ── 重构新闻主体 ──
    middle = "\n\n".join(
        re.sub(
            r'class="day-news-container[^"]*"',
            f'class="day-news-container{" active" if d == sorted_dates[0] else ""}"',
            containers[d]
        )
        for d in sorted_dates
    )

    # ── 找到插入点并组装 ──
    pills_start = html.find('<div class="date-pills"')
    pills_end = html.find("</div>", pills_start)
    pills_end = html.find("</div>", pills_end + 6) + 6  # 嵌套

    main_start = html.find('<main class="news-container">')
    footer_start = html.find("<footer>")

    if any(x < 0 for x in (pills_start, pills_end, main_start, footer_start)):
        print("❌ 无法解析 news.html 结构")
        return False

    # 组装
    new_html = (
        html[:pills_start] +
        pills_block + "\n" +
        html[pills_end:main_start] +
        f'    <main class="news-container">\n{middle}\n    </main>\n' +
        html[footer_start:]
    )

    # 备份
    shutil.copy2(NEWS_HTML, NEWS_HTML + ".bak")
    with open(NEWS_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)

    print(f"  ✅ 合并完成: {len(sorted_dates)} 天, 最新: {sorted_dates[0]}")
    return True


def git_push(today):
    """Git 提交推送"""
    cmds = [
        ["git", "-C", SITE_DIR, "add", "news.html"],
        ["git", "-C", SITE_DIR, "commit", "-m", f"🚀 AI新闻日报自动更新 {today}"],
        ["git", "-C", SITE_DIR, "push"],
    ]
    for cmd in cmds:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        ok = r.returncode == 0
        print(f"  {'✅' if ok else 'ℹ️'} git {' '.join(cmd[2:])}"
              f"{' ✓' if ok else ' (无变更)'}")
        if not ok and r.stderr.strip():
            # 只有非预期错误才显示
            if "nothing to commit" not in r.stderr and "Everything up-to-date" not in r.stderr:
                print(f"    ⚠️ {r.stderr[:200]}")


def main():
    no_push = "--no-push" in sys.argv

    today = datetime.now().strftime("%Y-%m-%d")
    print(f"🔄 AI 新闻日报更新 [{today}]")

    # ── 1. 搜索新闻 ──
    print("🔍 搜索最新 AI 新闻...")
    articles = fetch_news()

    if not articles:
        print("  ⚠️ 搜索全部失败，今天的页面将保留旧数据不变")
        print("  ℹ️ 当前 news.html 已有数据不会丢失")
        return

    # 缓存
    cache_path = os.path.join(NEWS_DIR, f"raw_news_{today}.json")
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

    # ── 2. 生成今日 HTML ──
    container_html = make_container(today, articles, first=True)

    # ── 3. 合并到 news.html ──
    if not os.path.exists(NEWS_HTML):
        print(f"❌ 文件不存在: {NEWS_HTML}")
        return

    if not rebuild_html(today, container_html):
        return

    # ── 4. Git 推送 ──
    if not no_push:
        git_push(today)

    print(f"\n🎉 完成! 访问 https://www.jarviswangcai.top/news.html 查看")


if __name__ == "__main__":
    main()

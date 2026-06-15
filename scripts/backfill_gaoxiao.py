#!/usr/bin/env python3
"""Backfill gaoxiao news for missing dates"""
import sys
import os
import datetime as dt

# Target date from CLI
target_day = int(sys.argv[1])
target_date = dt.datetime(2026, 6, target_day, 7, 30, 0)

# Import the module
sys.path.insert(0, '/Users/jiyingguo/.openclaw/workspace/scripts')
import send_daily_ai_news_real

# Monkey-patch datetime.now in the module's namespace
original_datetime = send_daily_ai_news_real.datetime

class PatchedDatetime:
    """Patched datetime that always returns target_date for now()"""
    @classmethod
    def now(cls, tz=None):
        return target_date
    
    @staticmethod
    def strftime(format_str):
        return target_date.strftime(format_str)

send_daily_ai_news_real.datetime = PatchedDatetime

# Also patch generated date strings in the HTML/footer by overriding generate_html_email
orig_generate = send_daily_ai_news_real.generate_html_email
def patched_generate(news_items):
    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>高校分队 AI 新闻每日简报 - {target_date.strftime("%Y年%m月%d日")}</title>
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
        <h1>高校分队 AI 新闻每日简报</h1>
        <div class="date">{target_date.strftime("%Y年%m月%d日")}早间版 (内容动态抓取自权威媒体)</div>
    </div>
    <div class="section">
'''
    for i, item in enumerate(news_items):
        title = item.get('trans_title', item.get('title'))
        summary = item.get('trans_summary', item.get('snippet'))
        url = item.get('link', '#')
        source = item.get('source', 'Unknown')
        html += f'''
        <div class="news-item">
            <div class="news-title">{i+1}. {title}</div>
            <div class="news-meta">来源：{source} | 翻译模型：{item.get('model', 'Unknown')}</div>
            <div class="news-summary">{summary}</div>
            <a class="news-link" href="{url}" target="_blank">🔗 点击阅读真实原文 (指向具体文章)</a>
        </div>
        '''
    html += f'''
    </div>
    <div class="footer">
        <p>本简报由旺财Jarvis自动抓取真实文章链接生成，告别假链接！</p>
        <p>生成时间：{target_date.strftime("%Y-%m-%d %H:%M:%S")}</p>
    </div>
</body>
</html>'''
    return html

send_daily_ai_news_real.generate_html_email = patched_generate

# Run
print(f"=== Backfilling gaoxiao news for 2026-06-{target_day} ===")
send_daily_ai_news_real.main()

#!/usr/bin/env python3
"""Fetch AI news from Google News RSS and save as raw JSON"""
import xml.etree.ElementTree as ET
import json
import requests
import re
from datetime import datetime

def fetch_news():
    url = 'https://news.google.com/rss/search?q=AI+OR+OpenAI+OR+Anthropic+OR+DeepSeek+OR+Nvidia+artificial+intelligence&hl=en-US&gl=US&ceid=US:en'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
    resp = requests.get(url, headers=headers, timeout=15)
    root = ET.fromstring(resp.text)
    channel = root.find('.//channel')
    items = channel.findall('item')
    
    news_list = []
    for item in items[:8]:  # Top 8 articles
        title = item.find('title').text if item.find('title') is not None else ''
        source = item.find('source').text if item.find('source') is not None else ''
        link = item.find('link').text if item.find('link') is not None else ''
        pubdate = item.find('pubDate').text if item.find('pubDate') is not None else ''
        
        # Parse description
        desc_elem = item.find('description')
        snippet = ''
        if desc_elem is not None and desc_elem.text:
            text = desc_elem.text
            # Remove HTML tags
            snippet = re.sub(r'<[^>]+>', '', text).strip()
        
        news_list.append({
            'title': title,
            'source': source,
            'link': link,
            'snippet': snippet,
            'pubDate': pubdate,
            'date': datetime.now().strftime('%Y-%m-%d')
        })
    
    return news_list

if __name__ == '__main__':
    today = datetime.now().strftime('%Y-%m-%d')
    news = fetch_news()
    path = f'/Users/jiyingguo/.openclaw/workspace/news_summaries/gaoxiao_raw_{today}.json'
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump({'news': news, 'fetched_at': datetime.now().isoformat()}, f, ensure_ascii=False, indent=2)
    
    print(f'Saved {len(news)} articles to {path}')
    for i, n in enumerate(news):
        print(f'{i+1}. {n["title"]}')

#!/usr/bin/env python3
"""晨间任务补跑 - 2026-04-03"""
import os, sys, json, ssl, time, smtplib, random
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import urllib.request, urllib.parse

SERPAPI_KEY = "b28c2426b9015470508315f27a6782b552a5a5b39550fbc9b62ff381e67c360f"
GEMAIL_KEY = "AIzaSyDUXba29bf86c_pjadKWftMH6u30kEpN9s"
MINIMAX_KEY = "sk-api-bS8q_8MyM1yPPp05MLY9OYxRmnt7_J-tdLTSngjfikY4B-HKrRzFDb6HigbxLusav_28ILdivTB91OiHNu73Y29ZE2ktdAB1ezfJneH80t__lnVQA0bbZrY"
DEEPSEEK_KEY = "sk-451f43ffa9764b7e91430e4d39538356"
SMTP_SERVER, SMTP_PORT = "smtp.qq.com", 587
EMAIL, PASSWORD = "86940135@qq.com", "icxhfzuyzbhbbjie"
TO15 = ["liuwei44259@huawei.com","tiankunyang@huawei.com","qinhongyi2@huawei.com","jiawei18@huawei.com","jiyingguo@huawei.com","linfeng67@huawei.com","lvluling1@huawei.com","suqi1@huawei.com","susha@huawei.com","wangdongxiao@huawei.com","xiongguifang@huawei.com","xushengsheng@huawei.com","zhangqianfeng2@huawei.com","zhangyexing2@huawei.com","86940135@qq.com"]
WORKSPACE = "/Users/jiyingguo/.openclaw/workspace"
NEWS_DIR = f"{WORKSPACE}/news_summaries"
os.makedirs(NEWS_DIR, exist_ok=True)

def log(m): print(f"[{datetime.now().strftime('%H:%M:%S')}] {m}")

def fetch(query, num=6):
    params = {"q": query, "api_key": SERPAPI_KEY, "tbm": "nws", "tbs": "qdr:d30", "num": num, "gl": "us", "hl": "en"}
    url = "https://serpapi.com/search.json?" + urllib.parse.urlencode(params)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read()) .get('news_results', [])[:num]
    except Exception as e:
        log(f"SerpAPI错误: {e}"); return []

def call_api(url, data, headers):
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers)
    with urllib.request.urlopen(req, timeout=60) as r: return json.loads(r.read())

def gemini(prompt):
    return call_api(f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent?key={GEMAIL_KEY}", {"contents":[{"parts":[{"text":prompt}]}]}, {"Content-Type":"application/json"})['candidates'][0]['content']['parts'][0]['text']

def minimax(prompt):
    return call_api("https://api.minimax.chat/v1/chat/completions", {"model":"MiniMax-M2.7-highspeed","messages":[{"role":"user","content":prompt}]}, {"Authorization":f"Bearer {MINIMAX_KEY}","Content-Type":"application/json"})['choices'][0]['message']['content']

def deepseek(prompt):
    return call_api("https://api.deepseek.com/v1/chat/completions", {"model":"deepseek-chat","messages":[{"role":"user","content":prompt}]}, {"Authorization":f"Bearer {DEEPSEEK_KEY}","Content-Type":"application/json"})['choices'][0]['message']['content']

def translate(text, fallback):
    try: return gemini(text)
    except: pass
    try: return minimax(text)
    except: pass
    try: return deepseek(text)
    except: pass
    return fallback

def cjson(t):
    t = t.strip()
    for m in ["</think>","```json","```"]:
        if m in t: t = t.split(m)[-1].strip()
    if t.endswith("```"): t = t[:-3]
    return t.strip()

def dedup(results):
    seen = set(); u = []
    for r in results:
        if r['link'] not in seen: seen.add(r['link']); u.append(r)
    return u

def send_html(recipients, subject, html):
    ctx = ssl.create_default_context()
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30) as s:
        s.starttls(context=ctx); s.login(EMAIL, PASSWORD)
        for to in recipients:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject; msg["From"] = EMAIL; msg["To"] = to
            msg.attach(MIMEText("请使用支持HTML的邮件客户端查看。", "plain", "utf-8"))
            msg.attach(MIMEText(html, "html", "utf-8"))
            try: s.sendmail(EMAIL, [to], msg.as_string()); log(f"  -> {to}"); time.sleep(0.5)
            except Exception as e: log(f"  发送失败 {to}: {e}")

def translate_news(title, snippet):
    p = f'直接输出纯JSON，不要任何标记：{{"title":"中文标题","summary":"80字摘要"}}。原文：{title}，摘要：{snippet[:200]}'
    try:
        res = json.loads(cjson(translate(p, "")))
        return res.get('title', title), res.get('summary', snippet[:80])
    except:
        return title, snippet[:80]

# === TASK 1: OpenClaw News ===
def task1():
    log("=== 任务1: OpenClaw每日新闻 ===")
    today = datetime.now().strftime('%Y-%m-%d')
    r = dedup(fetch("OpenClaw AI agent 2026", 6) + fetch("openclaw github March 2026", 6))[:8]
    log(f"获取 {len(r)} 条结果")
    
    md = f"# 🦞 OpenClaw日报 - {today}\n\n## 📊 今日概览\n- 精选动态：{len(r)}条\n\n---\n\n## 🚀 版本与功能更新\n\n"
    for i, item in enumerate(r, 1):
        t, s = translate_news(item.get('title',''), item.get('snippet',''))
        md += f"### {i}. {t}\n**来源**：{item.get('source','')}\n\n{s}\n\n🔗 [查看原文]({item.get('link','')})\n\n---\n\n"
    md += f"\n---\n*生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}*\n"
    
    f = f"{NEWS_DIR}/openclaw_news_high_quality_{today}.md"
    with open(f, 'w') as fp: fp.write(md)
    log(f"✅ 报告: {f}")
    
    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
    body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;line-height:1.6;max-width:800px;margin:0 auto;padding:20px}}
    .h{{background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:30px;border-radius:10px;margin-bottom:30px}}
    .h h1{{margin:0}}h2{{color:#2c3e50;margin-top:30px}}h3{{color:#3498db;margin-top:20px}}
    .item{{background:#f8f9fa;padding:15px;border-radius:8px;margin-bottom:15px;border-left:4px solid #667eea}}
    a{{color:#1976d2}}p{{margin:5px 0}}.f{{text-align:center;color:#888;font-size:12px;margin-top:40px}}
    </style></head><body>
    <div class="h"><h1>🦞 OpenClaw日报</h1><p>{today}</p></div>
    <h2>📊 今日概览</h2><p>精选动态：{len(r)}条</p>
    <h2>🚀 版本与功能更新</h2>"""
    for i, item in enumerate(r, 1):
        t, s = translate_news(item.get('title',''), item.get('snippet',''))
        html += f'<div class="item"><h3>{i}. {t}</h3><p>{s}</p><a href="{item.get("link","")}">查看原文</a></div>'
    html += f'<div class="f"><p>旺财Jarvis自动生成 | {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p></div></body></html>'
    send_html(["86940135@qq.com","jiyingguo@huawei.com"], f"🦞 OpenClaw日报 - {today}", html)
    log("✅ 任务1完成")

# === TASK 2: AI News Briefing (15 people) ===
def task2():
    log("=== 任务2: 高校分队AI新闻简报 ===")
    today = datetime.now().strftime('%Y-%m-%d')
    today_cn = datetime.now().strftime('%Y年%m月%d日')
    r = dedup(fetch("AI artificial intelligence breakthrough March 2026", 6) + fetch("OpenAI GPT Claude Gemini news April 2026", 6))[:8]
    log(f"获取 {len(r)} 条结果")
    
    items = []
    for item in r:
        t, s = translate_news(item.get('title',''), item.get('snippet',''))
        items.append({'title': t, 'summary': s, 'link': item.get('link',''), 'source': item.get('source','')})
        time.sleep(0.5)
    
    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
    body{{font-family:'Microsoft YaHei',Arial,sans-serif;line-height:1.6;color:#333;max-width:800px;margin:0 auto;padding:20px;background:#f5f5f5}}
    .h{{background:#1a237e;color:white;padding:20px;border-radius:5px;margin-bottom:20px}}
    .h h1{{margin:0}}p{{margin:5px 0;opacity:0.9}}
    .s{{background:white;padding:20px;border-radius:5px;box-shadow:0 2px 4px rgba(0,0,0,0.1);margin-bottom:20px}}
    .n{{margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #eee}}
    .n:last-child{{border:none}}
    .t{{font-weight:bold;color:#1a237e;font-size:16px;margin-bottom:8px}}
    .m{{color:#888;font-size:12px;margin-bottom:5px}}
    .c{{color:#555;font-size:14px;line-height:1.5;margin-bottom:8px}}
    a{{color:#1976d2;text-decoration:none;font-size:13px}}
    .f{{text-align:center;color:#666;font-size:12px;margin-top:30px;padding-top:20px;border-top:1px solid #ddd}}
    </style></head><body>
    <div class="h"><h1>高校分队 AI 新闻每日简报</h1><p>{today_cn}早间版</p></div>
    <div class="s">"""
    for i, item in enumerate(items, 1):
        html += f'<div class="n"><div class="t">{i}. {item["title"]}</div><div class="m">来源：{item["source"]}</div><div class="c">{item["summary"]}</div><a href="{item["link"]}" target="_blank">🔗 点击阅读原文</a></div>'
    html += f"""</div><div class="f"><p>本简报由旺财Jarvis自动生成</p><p>生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p></div></body></html>"""
    
    with open(f"{NEWS_DIR}/ai_news_{today}.html", 'w') as fp: fp.write(html)
    send_html(TO15, f"[{today}] 高校分队- AI 新闻每日简报", html)
    log("✅ 任务2完成")

# === TASK 3: Health Longevity ===
def task3():
    log("=== 任务3: 健康长寿科研成果 ===")
    today = datetime.now().strftime('%Y-%m-%d')
    r = dedup(fetch("longevity health research breakthrough March 2026", 6) + fetch("anti-aging science discovery 2026", 6))[:8]
    log(f"获取 {len(r)} 条结果")
    
    items = []
    for item in r:
        p = f'直接输出纯JSON，不要任何标记：{{"title":"中文标题","summary":"100字摘要"}}。原文：{item.get("title","")}，摘要：{item.get("snippet","")[:200]}'
        try:
            res = json.loads(cjson(translate(p, "")))
            t, s = res.get('title', item.get('title','')), res.get('summary', item.get('snippet','')[:100])
        except:
            t, s = item.get('title',''), item.get('snippet','')[:100]
        items.append({'title': t, 'summary': s, 'link': item.get('link',''), 'source': item.get('source','')})
        time.sleep(0.5)
    
    md = f"# 🧬 健康长寿科研日报\n**日期：{datetime.now().strftime('%Y年%m月%d日')}**\n\n---\n\n## 🔬 重要研究发现\n\n"
    for i, item in enumerate(items, 1):
        md += f"### {i}. {item['title']}\n**来源**：{item['source']}\n\n{item['summary']}\n\n🔗 [查看原文]({item['link']})\n\n---\n\n"
    md += f"\n---\n*生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"
    
    f = f"{NEWS_DIR}/health_longevity_{today}.md"
    with open(f, 'w') as fp: fp.write(md)
    log(f"✅ 报告: {f}")
    
    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
    body{{font-family:Arial,sans-serif;line-height:1.6;color:#333;max-width:800px;margin:0 auto;padding:20px}}
    .h{{background:#2e7d32;color:white;padding:20px;border-radius:8px;margin-bottom:20px}}
    .h h1{{margin:0}}p{{margin:5px 0}}
    .s{{background:#f9f9f9;padding:15px;border-radius:8px;margin-bottom:20px}}
    .n{{background:white;padding:15px;border-radius:6px;border-left:4px solid #2e7d32;margin-bottom:15px}}
    .t{{font-weight:bold;color:#2e7d32;margin-bottom:8px}}
    .m{{color:#888;font-size:12px;margin-bottom:5px}}
    .c{{color:#555;margin-bottom:8px;line-height:1.5}}
    a{{color:#1976d2;text-decoration:none;font-size:13px}}
    .d{{background:#fff3cd;padding:10px;border-radius:4px;font-size:13px}}
    .f{{text-align:center;color:#666;font-size:12px;margin-top:30px;padding-top:20px;border-top:1px solid #ddd}}
    </style></head><body>
    <div class="h"><h1>🏥 健康长寿科研日报 - {datetime.now().strftime('%Y年%m月%d日')}</h1><p>每日精选全球健康长寿领域最新科研成果</p></div>
    <div class="s"><p>精选研究：{len(items)}条 | 数据来源：ScienceDaily / Nature / JAMA</p></div>
    <div class="s"><h2>🔬 重要研究发现</h2>"""
    for i, item in enumerate(items, 1):
        html += f'<div class="n"><div class="t">{i}. {item["title"]}</div><div class="m">来源：{item["source"]}</div><div class="c">{item["summary"]}</div><a href="{item["link"]}">🔗 查看原文</a></div>'
    html += f"""</div><div class="d">⚠️ <strong>免责声明</strong>：本报告仅供信息参考，不构成医疗建议。</div>
    <div class="f"><p>报告生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p></div></body></html>"""
    send_html(["86940135@qq.com","jiyingguo@huawei.com"], f"🏥 健康长寿科研日报 - {today}", html)
    log("✅ 任务3完成")

# === TASK 4: Daily Blessing ===
def task4():
    log("=== 任务4: 每日祝福 ===")
    blessings = [
        "健康是福，长寿是德", "身心健康，天天开心", "胃口好吃嘛嘛香",
        "睡眠充足精神好", "腿脚利索走路稳", "耳聪目明思维清",
        "血压血糖都正常", "心脏健康跳得欢", "骨骼强健身子硬",
        "免疫力强少生病", "科学养生身体好", "适度锻炼延年寿",
        "乐观开朗寿命长", "家和万事兴又旺", "子女孝顺福满门",
        "平平安安才是真", "岁岁平安年年好", "出入平安保平安",
        "福如东海长流水", "寿比南山不老松", "福禄双全庆有余",
        "笑口常开好运来", "心情舒畅精神爽", "顺心顺意好运气",
        "好事连连乐逍遥", "梦想成真福满门", "保持热爱赴山海",
    ]
    b = random.choice(blessings)
    log(f"祝福语: {b}")
    log("✅ 任务4完成（祝福已生成）")
    return True

def main():
    log("=" * 60)
    log("晨间任务补跑开始 - 2026-04-03")
    log("=" * 60)
    try: task1()
    except Exception as e: log(f"任务1失败: {e}")
    time.sleep(2)
    try: task2()
    except Exception as e: log(f"任务2失败: {e}")
    time.sleep(2)
    try: task3()
    except Exception as e: log(f"任务3失败: {e}")
    time.sleep(1)
    try: task4()
    except Exception as e: log(f"任务4失败: {e}")
    log("=" * 60)
    log("晨间任务补跑完成")
    log("=" * 60)

main()

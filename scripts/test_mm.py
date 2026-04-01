import sys
sys.path.append('/Users/jiyingguo/.openclaw/workspace/scripts')
from send_daily_ai_news_real import call_minimax, clean_json, json
prompt = '请把以下英文新闻标题和摘要翻译成中文，并写一段详细的中文内容（100字左右），说明其核心内容和影响。直接输出纯JSON格式：{"title": "中文标题", "summary": "详细的中文摘要"}。不要带 markdown ``` 标签。原文标题: OpenAI announces new model，原文摘要: OpenAI has released a new language model that outperforms its predecessors.'
res = call_minimax(prompt)
print(json.loads(clean_json(res)))

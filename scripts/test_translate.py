import sys
sys.path.append("/Users/jiyingguo/.openclaw/workspace/scripts")
from send_daily_ai_news_real import translate_and_summarize

res = translate_and_summarize("OpenAI announces new model", "OpenAI has released a new language model that outperforms its predecessors.")
print(res)

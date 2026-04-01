import requests
import json

MINIMAX_KEY = "sk-api-bS8q_8MyM1yPPp05MLY9OYxRmnt7_J-tdLTSngjfikY4B-HKrRzFDb6HigbxLusav_28ILdivTB91OiHNu73Y29ZE2ktdAB1ezfJneH80t__lnVQA0bbZrY"
url = "https://api.minimaxi.com/anthropic/v1/messages"
headers = {
    "x-api-key": MINIMAX_KEY,
    "Content-Type": "application/json",
    "anthropic-version": "2023-06-01"
}
prompt = "请把以下英文新闻标题和摘要翻译成中文，并写一段详细的中文内容（100字左右），说明其核心内容和影响。直接输出纯JSON格式：{\"title\": \"中文标题\", \"summary\": \"详细的中文摘要\"}。不要带 markdown ``` 标签。原文标题: OpenAI announces new model，原文摘要: OpenAI has released a new language model that outperforms its predecessors."

payload = {
    "model": "MiniMax-M2.7-highspeed",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": prompt}]
}
try:
    resp = requests.post(url, json=payload, headers=headers, timeout=30)
    print("MiniMax Anthropic API:", resp.status_code, resp.text)
except Exception as e:
    print("Error:", e)

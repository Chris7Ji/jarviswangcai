import requests

DEEPSEEK_KEY = "sk-451f43ffa9764b7e91430e4d39538356"

url = "https://api.deepseek.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {DEEPSEEK_KEY}",
    "Content-Type": "application/json"
}
payload = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Hello"}]
}
try:
    resp = requests.post(url, json=payload, headers=headers, timeout=10)
    print("DeepSeek API:", resp.status_code, resp.text[:100])
except Exception as e:
    print("Error:", e)

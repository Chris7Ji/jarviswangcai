import requests

MINIMAX_KEY = "sk-api-bS8q_8MyM1yPPp05MLY9OYxRmnt7_J-tdLTSngjfikY4B-HKrRzFDb6HigbxLusav_28ILdivTB91OiHNu73Y29ZE2ktdAB1ezfJneH80t__lnVQA0bbZrY"

url = "https://api.minimax.chat/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {MINIMAX_KEY}",
    "Content-Type": "application/json"
}
payload = {
    "model": "MiniMax-Text-01",
    "messages": [{"role": "user", "content": "Hello"}]
}
try:
    resp = requests.post(url, json=payload, headers=headers, timeout=10)
    print("MiniMax API:", resp.status_code, resp.text[:100])
except Exception as e:
    print("Error:", e)

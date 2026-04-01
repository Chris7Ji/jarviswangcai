import os
import json
import time
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

WORKSPACE = "/Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai"
MESSAGES_FILE = os.path.join(WORKSPACE, "data", "messages.json")
DEEPSEEK_API_KEY = "sk-451f43ffa9764b7e91430e4d39538356" 

def load_messages():
    if os.path.exists(MESSAGES_FILE):
        try:
            with open(MESSAGES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return []

def save_messages(msgs):
    with open(MESSAGES_FILE, 'w', encoding='utf-8') as f:
        json.dump(msgs, f, ensure_ascii=False, indent=2)

def moderate_content(content):
    try:
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "你是一个严格的内容安全审核员。请检查以下留言是否包含：涉政、暴恐、色情、辱骂、违禁品、种族歧视或极其恶劣的言论。如果内容非常安全友好，请仅回复 PASS；如果有任何违规风险或低俗内容，请仅回复 REJECT。不要做任何解释。"},
                {"role": "user", "content": content}
            ],
            "temperature": 0.1,
            "max_tokens": 10
        }
        resp = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=payload, timeout=5)
        if resp.status_code == 200:
            result = resp.json()['choices'][0]['message']['content'].strip().upper()
            return "PASS" in result
        return False
    except Exception as e:
        print(f"Moderation error: {e}")
        return False

@app.route('/messages', methods=['GET'])
def get_messages():
    msgs = load_messages()
    msgs.sort(key=lambda x: x.get('time', ''), reverse=True)
    return jsonify(msgs)

@app.route('/messages', methods=['POST'])
def add_message():
    data = request.json
    name = data.get('name', '匿名访客').strip()[:20]
    content = data.get('content', '').strip()[:500]

    if not name: name = '匿名访客'
    if not content:
        return jsonify({"status": "error", "message": "内容不能为空"}), 400

    # AI Moderation
    is_safe = moderate_content(content)

    if is_safe:
        msgs = load_messages()
        new_id = max([m.get('id', 0) for m in msgs] + [0]) + 1
        new_msg = {
            "id": new_id,
            "name": name,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "content": content,
            "isAdmin": False
        }
        msgs.append(new_msg) 
        save_messages(msgs)

    return jsonify({"status": "success", "message": "留言提交成功"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

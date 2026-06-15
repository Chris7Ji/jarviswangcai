#!/bin/bash
# 🔒 统一密钥加载器
# 用法: source ~/.openclaw/workspace/scripts/_load_secrets.sh
SECRETS_FILE="$HOME/.openclaw/workspace/.env.secrets"
if [ -f "$SECRETS_FILE" ]; then
  source "$SECRETS_FILE"
fi

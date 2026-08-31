#!/bin/bash
# 验证今日日记是否已生成
# 检查 diary.js 中是否存在今日日期的条目

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DIARY_FILE="$SCRIPT_DIR/../js/diary.js"
TODAY=$(date +%Y-%m-%d)

if [ ! -f "$DIARY_FILE" ]; then
  echo "❌ diary.js 文件不存在: $DIARY_FILE"
  exit 1
fi

# 检查文件中是否包含今日日期
if grep -q "\"$TODAY\"" "$DIARY_FILE"; then
  echo "✅ 今日($TODAY)日记已生成"
  exit 0
else
  echo "⚠️ 今日($TODAY)日记未生成"
  echo "最新条目:"
  grep -m1 '"date":' "$DIARY_FILE" | sed 's/^[[:space:]]*/  /'
  exit 1
fi

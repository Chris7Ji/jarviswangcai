#!/bin/bash
# 网站文件完整性检查
# 每次 git push 前自动检查核心文件是否存在

REQUIRED_FILES=(
  "index.html"
  "post.html"
  "diary.html"
  "CNAME"
  ".nojekyll"
  "css/style.css"
  "css/diary.css"
)

MISSING=0
for f in "${REQUIRED_FILES[@]}"; do
  if [ ! -f "$f" ]; then
    echo "❌ 缺失: $f"
    MISSING=1
  fi
done

if [ $MISSING -eq 0 ]; then
  echo "✅ 所有核心网站文件完整"
  exit 0
else
  echo "⚠️ 核心文件缺失，请不要 push！"
  exit 1
fi

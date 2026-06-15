#!/bin/bash
# Send via himalaya with raw message format
CONTENT=$(cat /Users/jiyingguo/.openclaw/workspace/news_summaries/openclaw_news_high_quality_2026-05-21.md)

# Build raw email with headers
{
  echo "From: 86940135@qq.com"
  echo "To: 86940135@qq.com, jiyingguo@huawei.com"
  echo "Subject: =?utf-8?B?8J+mnk9wZW5DbGF3TOaXpeWKqC0gMjAyNuW5tDA15pyIMDHml6U=?="
  echo "MIME-Version: 1.0"
  echo "Content-Type: text/plain; charset=utf-8"
  echo "Content-Transfer-Encoding: base64"
  echo ""
  echo "$CONTENT" | base64
} | himalaya message send --account qq 2>&1

echo "Exit code: $?"

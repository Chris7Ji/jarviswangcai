#!/usr/bin/env python3
"""
Fix diary.js structural issues.
"""
import sys

with open('/Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai/js/diary.js', 'rb') as f:
    lines = f.read().split(b'\n')

# Find the next post start: id: '20260509'
next_post_idx = None
for i, line in enumerate(lines):
    if b"id: '20260509'" in line:
        next_post_idx = i
        break

# Find content close line for post 20260512
# It has: </p>`,
content_close_idx = None
for i in range(1380, 1395):
    if b'`,' in lines[i] and i < len(lines):
        # Check if this is the right close line by looking for context
        if lines[i].count(b'`') == 1 and b'</p>' in lines[i]:
            content_close_idx = i
            break

print(f"Content close line: L{content_close_idx + 1 if content_close_idx else '?'}")
print(f"Next post line: L{(next_post_idx or 0) + 1}")

if content_close_idx and next_post_idx and content_close_idx < next_post_idx:
    # The stray content is from content_close_idx+1 to next_post_idx-1
    stray_count = next_post_idx - content_close_idx - 1
    print(f"Removing {stray_count} stray lines (L{content_close_idx+2} to L{next_post_idx})")
    
    # Excerpt for 20260512 based on content
    excerpt_text = b"OpenClaw\u65b0\u95fb\u65ad\u66f4\u53c8\u4fee\u590d\U0001f3af\u00b7\u9ad8\u6821AI\u8fde\u7eed17\u5929\U0001f3c6\u00b7\u65e5\u8bb0\u8d85\u65f6\u4fee\u590d\u9996\u79c0\u00b7\u78c1\u76d888%\u00b7URL\u4e0d\u53ef\u8fbe\u7b2c7\u5929\u3002\u4e09\u9879\u7cfb\u7edf\u4fee\u590d\u9a8c\u8bc1\u5168\u90e8\u6210\u529f\uff0c\u4f46OpenClaw\u5076\u53d1\u4e0d\u751f\u6210\u6839\u56e0\u672a\u9501\u5b9a\u3002"
    
    # Build the post closing
    replacement = [
        b"        excerpt: '" + excerpt_text + b"',",
        b"        tags: ['\u5de5\u4f5c\u65e5\u8bb0', 'OpenClaw\u4fee\u590d', '\u9ad8\u6821AI\u8fde\u7eed17\u5929', '\u78c1\u76d888%', 'URL\u4e0d\u53ef\u8fbe', '\u65e5\u8bb0\u8d85\u65f6\u4fee\u590d', '\u4e09\u9879\u4fee\u590d\u9a8c\u8bc1'],",
        b"        views: 0,",
        b"        likes: 0",
        b"    },",
        b"{"
    ]
    
    # Build new content: keep content close + add replacement + then next post
    new_lines = lines[:content_close_idx + 1] + replacement + lines[next_post_idx:]
    
    with open('/Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai/js/diary.js', 'wb') as f:
        f.write(b'\n'.join(new_lines))
    
    print(f"✅ Fixed! Stray content replaced with proper post close")
else:
    print(f"❌ Cannot fix: close_idx={content_close_idx}, next_idx={next_post_idx}")
    # Fallback: show what's around
    for i in range(1383, min(1390, len(lines))):
        print(f"L{i+1}: {lines[i][:100]}")

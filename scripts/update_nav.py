import os
import glob
import re

workspace = "/Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai"
html_files = glob.glob(os.path.join(workspace, "*.html"))
js_files = glob.glob(os.path.join(workspace, "js", "*.js"))

target_files = html_files + js_files
print(f"Checking {len(target_files)} files...")

count = 0
for filepath in target_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "技能与功能" in content:
            new_content = content.replace("技能与功能", "功能与技能")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {filepath}")
            count += 1
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

print(f"Total files updated for terminology: {count}")

import os
import glob
import re

workspace = "/Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai"
html_files = glob.glob(os.path.join(workspace, "*.html"))

count = 0
for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace footers and buttons saying just "技能" pointing to skills.html
        new_content = re.sub(r'>技能</a>', '>功能与技能</a>', content)
        new_content = re.sub(r'🛠️ 查看技能', '🛠️ 查看功能与技能', new_content)
        
        # Also let's make sure the title of skills.html is right
        if "skills.html" in filepath:
            new_content = new_content.replace("<title>技能与功能展示 - 旺财Jarvis</title>", "<title>功能与技能展示 - 旺财Jarvis</title>")
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated footer/buttons: {filepath}")
            count += 1
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

print(f"Total files updated for footer terminology: {count}")

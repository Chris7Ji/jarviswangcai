import os

filepath = "/Users/jiyingguo/.openclaw/workspace/scripts/update_skills_html.py"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_content = content.replace("def update_file():", """def update_file():
    # 规则说明：skills.html 分为上半部分“敲黑板知识点汇总”和下半部分“已安装技能库大本营”。
    # 本定时脚本（以及衍生的Cron任务）严格约束：只负责更新下半部分的技能库数据。
    # 逻辑原理：脚本通过查找 <!-- 技能图例 --> 标记作为起点，保留并原样写回标记之上所有的 HTML 代码。
    # 这样就能绝对保证以后再怎么动态更新技能列表，上方的“敲黑板知识点”文章和排版都不会受任何影响。""")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Added rule comment to update_skills_html.py")

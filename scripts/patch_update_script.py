import os
import re

filepath = "/Users/jiyingguo/.openclaw/workspace/scripts/update_skills_html.py"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the regex update part in `update_file()`
old_regex_part = """    content = re.sub(
        r'<span class="skill-count">\d+</span> 个技能持续为您服务',
        f'<span class="skill-count">{total_count}</span> 个技能持续为您服务',
        content
    )
    content = re.sub(
        r'共 \d+ 个技能，持续学习进化中\.\.\.',
        f'共 {total_count} 个技能，持续学习进化中...',
        content
    )"""

new_regex_part = """    # 动态统计知识点数量
    knowledge_count = len(re.findall(r'<div class="knowledge-card"', content))

    # 更新 Hero 区域的统计文案
    content = re.sub(
        r'<p>旺财Jarvis 拥有丰富的技能生态，助力高效工作<span class="skill-count">\d+</span> 个技能持续为您服务</p>',
        f'<p>沉淀 <span class="knowledge-count">{knowledge_count}</span> 篇核心知识，装载 <span class="skill-count">{total_count}</span> 项扩展技能持续为您服务</p>',
        content
    )
    # 兼容已经被替换过的文案（防止下次正则匹配不到）
    content = re.sub(
        r'<p>沉淀 <span class="knowledge-count">\d+</span> 篇核心知识，装载 <span class="skill-count">\d+</span> 项扩展技能持续为您服务</p>',
        f'<p>沉淀 <span class="knowledge-count">{knowledge_count}</span> 篇核心知识，装载 <span class="skill-count">{total_count}</span> 项扩展技能持续为您服务</p>',
        content
    )

    # 更新敲黑板标题的统计
    content = re.sub(
        r'<h2 style="font-size: 1\.8rem; color: var\(--text-primary\);">📝 敲黑板知识点汇总( \(共 <span class="knowledge-count">\d+</span> 篇\))?</h2>',
        f'<h2 style="font-size: 1.8rem; color: var(--text-primary);">📝 敲黑板知识点汇总 (共 <span class="knowledge-count">{knowledge_count}</span> 篇)</h2>',
        content
    )

    content = re.sub(
        r'共 \d+ 个技能，持续学习进化中\.\.\.',
        f'共 {total_count} 个技能，持续学习进化中...',
        content
    )"""

new_content = content.replace(old_regex_part, new_regex_part)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated python script successfully.")

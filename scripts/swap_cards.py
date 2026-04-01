import os

workspace = "/Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai"
skills_file = os.path.join(workspace, "skills.html")

with open(skills_file, 'r', encoding='utf-8') as f:
    content = f.read()

start_tag = '<section class="knowledge-list"'
end_tag = '</section>'

start_idx = content.find(start_tag)
end_idx = content.find(end_tag, start_idx) + len(end_tag)

if start_idx != -1 and end_idx != -1:
    new_list_html = """<section class="knowledge-list" style="margin-bottom: 4rem; display: flex; flex-direction: column; gap: 1.5rem;">
            <!-- 第一篇：执行白名单 (最新) -->
            <div class="knowledge-card" style="background: var(--bg-card); border-radius: 12px; border: 1px solid var(--border-color); padding: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.03); transition: transform 0.3s; cursor: pointer;" onclick="window.location.href='article_exec_allowlist.html'">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
                    <h3 style="font-size: 1.4rem; color: var(--accent-blue); margin: 0;">🛡️ 系统执行白名单 (Exec Allowlist) 机制深度解析</h3>
                    <span style="font-size: 0.9rem; color: var(--text-secondary); background: var(--bg-secondary); padding: 0.2rem 0.6rem; border-radius: 20px;">2026-04-01</span>
                </div>
                <p style="color: var(--text-secondary); line-height: 1.6; margin-bottom: 1.5rem; font-size: 1.05rem;">
                    执行白名单（Exec Allowlist）是保障 Mac mini 系统安全的“最后一道防线”。本文详细解析了该沙箱隔离机制的必要性、精确匹配与内联代码拦截的原理，以及如何通过“化动态为静态”的脚本沙箱模式安全有效地进行绕过与自动化配置。
                </p>
                <a href="article_exec_allowlist.html" style="color: var(--accent-gold); text-decoration: none; font-weight: bold; display: inline-flex; align-items: center; gap: 0.5rem;">查看全文 <span style="font-size: 1.2em;">→</span></a>
            </div>

            <!-- 第二篇：四D记忆系统 (较旧) -->
            <div class="knowledge-card" style="background: var(--bg-card); border-radius: 12px; border: 1px solid var(--border-color); padding: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.03); transition: transform 0.3s; cursor: pointer;" onclick="window.location.href='article_4d_memory.html'">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
                    <h3 style="font-size: 1.4rem; color: var(--accent-blue); margin: 0;">✨ 多层四D记忆系统架构全景</h3>
                    <span style="font-size: 0.9rem; color: var(--text-secondary); background: var(--bg-secondary); padding: 0.2rem 0.6rem; border-radius: 20px;">2026-03-31</span>
                </div>
                <p style="color: var(--text-secondary); line-height: 1.6; margin-bottom: 1.5rem; font-size: 1.05rem;">
                    作为一个不断进化的 Proactive Agent，旺财Jarvis 的大脑已经从最初的“扁平化文件堆叠”演进为“全息立体知识库”。它不仅能执行指令，更能通过一套具备时空感知、关系推理、自动代谢的立体记忆检索架构，在您提问的瞬间零延迟穿梭于四个维度，拼凑出最立体的上下文全貌。
                </p>
                <a href="article_4d_memory.html" style="color: var(--accent-gold); text-decoration: none; font-weight: bold; display: inline-flex; align-items: center; gap: 0.5rem;">查看全文 <span style="font-size: 1.2em;">→</span></a>
            </div>
        </section>"""
    
    new_content = content[:start_idx] + new_list_html + content[end_idx:]
    with open(skills_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully swapped the order of knowledge cards.")
else:
    print("Could not find the section.")

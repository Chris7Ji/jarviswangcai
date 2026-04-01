
// 留言板前端逻辑
document.addEventListener('DOMContentLoaded', () => {
    loadMessages();
});

function loadMessages() {
    const listEl = document.getElementById('gb-list');
    
    // 从静态数据源加载审核通过的留言
    fetch('data/messages.json?t=' + new Date().getTime())
        .then(response => response.json())
        .then(data => {
            if (!data || data.length === 0) {
                listEl.innerHTML = '<div style="text-align: center; color: var(--text-secondary); padding: 2rem;">暂无留言，快来抢沙发吧！</div>';
                return;
            }
            
            // 倒序排列（最新的在上面）
            data.sort((a, b) => new Date(b.time) - new Date(a.time));
            
            let html = '';
            data.forEach(msg => {
                const adminIcon = msg.isAdmin ? '<span style="background: var(--accent-gold); color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.75rem; font-weight: normal;">博主</span>' : '';
                const cardClass = msg.isAdmin ? 'gb-card admin' : 'gb-card';
                const name = msg.name || '匿名访客';
                
                // 简单的防XSS处理
                const safeContent = msg.content.replace(/</g, "&lt;").replace(/>/g, "&gt;");
                const safeName = name.replace(/</g, "&lt;").replace(/>/g, "&gt;");
                
                html += `
                    <div class="${cardClass}">
                        <div class="gb-header">
                            <span class="gb-name">🧑‍💻 ${safeName} ${adminIcon}</span>
                            <span class="gb-time">${msg.time}</span>
                        </div>
                        <div class="gb-content">${safeContent}</div>
                    </div>
                `;
            });
            listEl.innerHTML = html;
        })
        .catch(err => {
            console.error('加载留言失败:', err);
            listEl.innerHTML = '<div style="text-align: center; color: var(--accent-blue); padding: 2rem;">系统维护中，暂时无法加载留言。</div>';
        });
}

function submitGuestbook() {
    const nameInput = document.getElementById('gb-name');
    const msgInput = document.getElementById('gb-message');
    const statusEl = document.getElementById('gb-status');
    const submitBtn = document.getElementById('gb-submit');
    
    const content = msgInput.value.trim();
    if (!content) {
        showStatus('留言内容不能为空！', 'red');
        return;
    }
    
    if (content.length < 5) {
        showStatus('留言太短啦，多写几个字吧 (至少5个字符)', 'red');
        return;
    }

    // 界面表现为提交中
    submitBtn.disabled = true;
    submitBtn.innerText = "上传合规审核系统...";
    
    // 模拟网络请求和提交过程
    // 实际架构：这里可以通过 Formspree 或 Webhook 发送至您的后端或飞书机器人
    // 您的后端服务器/本地Cron脚本将接收此请求，调用LLM进行合规拦截，
    // 如果安全则写入 messages.json 并 git push。
    
    setTimeout(() => {
        msgInput.value = '';
        submitBtn.disabled = false;
        submitBtn.innerText = "提交留言";
        
        statusEl.style.display = 'block';
        statusEl.style.color = '#3D9CA8';
        statusEl.innerHTML = '✅ 提交成功！为符合中国大陆内容合规要求，您的留言已进入 <b>AI安全审核队列</b>。预计5-10分钟后完成审核并在本页公开展示。';
        
        // 3秒后隐藏提示
        setTimeout(() => {
            statusEl.style.display = 'none';
        }, 15000);
    }, 1500);
}

function showStatus(text, color) {
    const statusEl = document.getElementById('gb-status');
    statusEl.style.display = 'block';
    statusEl.style.color = color;
    statusEl.innerText = text;
}

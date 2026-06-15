# 🦞 OpenClaw日报 - 2026年05月17日

## 📊 今日概览
- **精选动态**：35条（中文0条，英文35条）
- **重点类别**：版本更新 / 技能生态 / 社区动态
- **质量评级**：⭐⭐⭐⭐⭐
- **备注**：SerpAPI搜索配额已用完，数据主要来自GitHub API直接采集和社区渠道

---

## 🚀 版本与功能

### 1. OpenClaw v2026.5.16-beta.3 发布（三连发！）
**📰 来源**：GitHub Releases | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
5月16日连续发布3个beta版本（beta.1→beta.2→beta.3），包含以下重磅更新：

- **xAI Grok OAuth登录**：SuperGrok订阅用户可使用xAI Grok OAuth登录，`xai/*`模型和xAI媒体/工具提供商无需`XAI_API_KEY`即可完成认证
- **CLI/cron增强**：新增`openclaw cron run --wait`命令，带超时和轮询间隔控制；支持`cron.runs --run-id`精确筛选，可让自动化流程阻塞等待指定手工排队的cron任务完成
- **CLI/本地化升级**：安装向导和频道设置流程已翻译为英语、简体中文和繁体中文
- **Skills缓存优化**：缓存已水合的`resolvedSkills`，降低冗余技能快照重建
- **Telegram群组聊天**：新增`messages.groupChat.ambientTurns: "room_event"`可选配置，让常驻环境闲聊以静默房间上下文运行，仅通过message工具显式发言
- **Gateway性能**：启动基准测试拆分HTTP监听时间和完整Gateway就绪时间

**🔗 相关链接**：
- Release页面：https://github.com/openclaw/openclaw/releases/tag/v2026.5.16-beta.3
- Beta.2：https://github.com/openclaw/openclaw/releases/tag/v2026.5.16-beta.2
- Beta.1：https://github.com/openclaw/openclaw/releases/tag/v2026.5.16-beta.1

---

### 2. OpenClaw v2026.5.14-beta.2 发布
**📰 来源**：GitHub Releases | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
- **Channels/SDK**：新增规范化命令turn facts，支持插件入站上下文的命令turn辅助工具
- **Agents/配置**：支持按Agent粒度的bootstrap Profile覆写，包括`contextInjection`、`bootstrapMaxChars`、`bootstrapTotalMaxChars`
- **依赖管理**：将根级代理路由到`@openclaw/proxyline`，去除根级`proxy-agent`、`https-proxy-agent`、`minimatch`依赖
- **Canvas**：懒加载HTTP host、媒体解析器、CLI实现等模块，提升Gateway启动性能
- **Control UI/i18n**：添加`pnpm ui:i18n:report`基线报告

**🔗 相关链接**：
- Release页面：https://github.com/openclaw/openclaw/releases/tag/v2026.5.14-beta.2

---

### 3. Peekaboo v2 多项Bug修复（5月16日）
**📰 来源**：GitHub | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
Peekaboo（macOS屏幕截图CLI及MCP服务器）在5月16日连续提交3次修复：
- 修复Inspect UI快照元数据刷新
- 持久化Inspect UI快照
- 添加Inspect UI工具的更新日志

Peekaboo目前⭐ 4,280星

**🔗 相关链接**：
- 仓库：https://github.com/openclaw/Peekaboo

---

### 4. gogcli v0.17.0 发布（5月15日）
**📰 来源**：GitHub | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
Google Workspace终端CLI工具发布v0.17.0版本，修复账户管理器Token迁移认证问题（⭐ 7,462星）

**🔗 相关链接**：
- 仓库：https://github.com/openclaw/gogcli

---

### 5. mcporter 依赖更新（5月15日）
**📰 来源**：GitHub | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
MCP协议桥接工具更新依赖，版本升至0.11.2-dev（⭐ 4,427星）

**🔗 相关链接**：
- 仓库：https://github.com/openclaw/mcporter

---

### 6. clawhub v0.1.0 API正式发布
**📰 来源**：GitHub Releases | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
OpenClaw技能目录（Skill Directory）发布首个正式API版本v0.1.0：
- REST v1公开端点，带速率限制
- 原始文件获取
- OpenAPI规范
- ClawHub GitHub App自动备份已发布技能到`clawdbot/skills`
- 8,646星

**🔗 相关链接**：
- 仓库：https://github.com/openclaw/clawhub
- API文档：https://github.com/openclaw/clawhub/blob/main/docs/api.md

---

## 🧩 技能生态

### 新增Skills（5月15日，awesome-openclaw-skills收录）
| 技能名称 | 作者 | 类别 | 说明 |
|----------|------|------|------|
| vistoya/vistoya | @vistoya | 通用 | 新提交的OpenClaw Skill |
| accli-plus | @gopaljigaur | Calendar & Scheduling | 日历与日程管理增强技能 |
| trent-ai-release/trentclaw | @v0id-space | AI助手 | Trent AI发行版适配的OpenClaw技能 |
| drakulavich/kesha-voice-kit | @drakulavich | 语音 | Kesha语音工具包 |

### 技能生态数据
- awesome-openclaw-skills 仓库：⭐ 48,789星，收录5,400+技能
- ClawHub技能目录：⭐ 8,646星，API v1已正式上线

**🔗 相关链接**：
- Skills合集：https://github.com/VoltAgent/awesome-openclaw-skills
- ClawHub：https://github.com/openclaw/clawhub

---

## 💬 社区精选

### 5月16日重要Issues/Feature Requests
| # | 标题 | 类型 | 说明 |
|---|------|------|------|
| #45427 | 在入站元数据中包含可信发送者名称 | Feature | 增强消息来源完整性 |
| #45415 | MEMORY.md大小警告/限制强制执行 | Feature | 内存管理优化请求 |
| #81864 | 添加明文插件审批 | Feature | 审批体验改进 |
| #45404 | 清理旧版Brave配置残留 | Low-priority | 配置清理增强 |
| #45390 | Session TTL/最大生命周期自动轮换 | Feature | 会话管理增强 |

### 5月16日新提交的Bug Reports
| # | 标题 | 状态 |
|---|------|------|
| #82751 | Telegram隔离轮询BotInfo探针失败导致无限轮询 | 开放 |
| #82749 | 提供商切换将过长的历史工具ID重放到GitHub Copilot | 开放 |
| #82747 | Discord中Agent进度更新被配置阻止 | 开放 |
| #82744 | Thinking级别能力检查使用字面量provider/model而非有效值 | 开放 |
| #82735 | 请求运行时/生成失败的稳定错误码 | Feature |

### OpenClaw-RL 框架更新
Gen-Verse/OpenClaw-RL（⭐ 5,324星）修复了top-k OPD导入问题，保持OpenClaw组合模块的可导入性。

---

## 📈 数据洞察

### GitHub Star趋势（Top 5仓库）
| 仓库 | ⭐ Stars | 🍴 Forks | 最后活跃 |
|------|----------|----------|----------|
| openclaw/openclaw | 372,420 | 77,170 | 2026-05-16 |
| VoltAgent/awesome-openclaw-skills | 48,789 | 4,777 | 2026-05-16 |
| hesamsheikh/awesome-openclaw-usecases | 31,062 | 2,676 | 2026-05-16 |
| openclaw/clawhub | 8,646 | 1,342 | 2026-05-16 |
| openclaw/gogcli | 7,462 | 579 | 2026-05-16 |

### npm最新版本
- **稳定版**：v2026.5.12
- **最新发布**：v2026.5.16-beta.3（5月16日）

### 开发活跃度
- 5月16日单日提交量：8+ commits（主仓库）
- 过去24小时提交作者数：10+人
- Beta发布密度：3个beta版本/天（5月16日创近期新高）

---
*报告生成时间：2026-05-17 06:00 CST | 数据来源：GitHub API + GitHub Releases + npm Registry*

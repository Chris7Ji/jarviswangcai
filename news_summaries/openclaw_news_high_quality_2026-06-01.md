# 🦞 OpenClaw日报 - 2026年06月01日

## 📊 今日概览
- **精选动态**：8条（中文0条，英文8条）
- **重点类别**：版本更新 🔥
- **今日重磅**：OpenClaw v2026.5.31 系列版本发布（含 beta.1/2/3），Skill Workshop 正式上线！
- **质量评级**：⭐⭐⭐⭐⭐

---

## 🚀 版本与功能

### 1. OpenClaw v2026.5.31-beta.3 发布 — 五月收官重磅更新
**📰 来源**：GitHub Release | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
OpenClaw 团队于 5月31日 连续发布了 v2026.5.31-beta.1、beta.2 和 beta.3，并同时推出稳定版 v2026.5.28。本次更新是一次大规模的稳定性与功能增强发布。

**🔥 三大亮点**：
1. **Skill Workshop（技能工坊）正式上线** — 全新的受控技能创建流程，支持提案（PROPOSAL.md）、CLI/Gateway 审查、回滚元数据，以及 `skill_workshop` Agent 工具，Agent 可直接申请/拒绝/隔离技能提案
2. **Workboard 编排系统** — 多 Agent 规划和运行跟踪的原语和协调工具
3. **Codex / Agent 运行时大幅增强** — 子进程保持 cwd/workspace 隔离，会话锁超时安全释放，Codex app-server/helper 故障不再破坏共享运行时状态

**🔧 其他关键更新**：
- **插件生态外部化**：Tokenjuice 和 GitHub Copilot 作为官方插件发布（npm + ClawHub）
- **iOS 增强**：hosted push relay、实时 Talk 播放、WebSocket ping 路径
- **Code Mode**：新增内部命名空间，支持作用域 Agent/全局会话和精确命名空间工具调度
- **Control UI**：Dreaming 标签页新增 Agent 选择器
- **渠道稳定性**：Telegram、WhatsApp、iMessage、Slack、Discord、Teams、Google Chat/Meet、iOS Talk 全面加固
- **Provider 超时加固**：OpenAI/Google/MiniMax/FAL 等多个 Provider 的媒体下载、轮询、OAuth 计时器全面覆盖
- **安全增强**：配置解析中拒绝不安全的 OAuth/Token 生命周期、重试延迟、响应体大小等

**🔗 相关链接**：
- Release (beta.3)：https://github.com/openclaw/openclaw/releases/tag/v2026.5.31-beta.3
- Release (stable)：https://github.com/openclaw/openclaw/releases/tag/v2026.5.28
- Release 提交：3fcd8e08fbcf8f3cf065a5ea574dcbec8c2df62a
- npm 包：https://www.npmjs.com/package/openclaw/v/2026.5.31-beta.3

---

### 2. Skill Workshop — 受控技能创建与审查机制
**📰 来源**：GitHub Release | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
本次发布最大的功能亮点是 Skill Workshop。它引入了一套完整的技能生命周期管理流程：
- **提案阶段**：`PROPOSAL.md` 草案，带版本化日期前置元数据
- **审查流程**：CLI 和 Gateway 均可执行审查操作（apply/reject/quarantine）
- **Agent 工具**：`skill_workshop` Agent 工具可直接操作提案流
- **安全机制**：支持文件扫描器、哈希校验、回滚保护
- **文档**：新增专门的 Skill Workshop 指南，涵盖创建、提案、CLI/Gateway、Agent 行为、审批策略和恢复

感谢 @shakkernerd 贡献此功能！

**🔗 相关链接**：
- Release: https://github.com/openclaw/openclaw/releases/tag/v2026.5.31-beta.3

---

### 3. Codex 运行时大修 — Agent 恢复能力全面升级
**📰 来源**：GitHub Release | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
本次发布集中修复了 Agent 和 Codex 运行时的大量问题：
- 子 Agent 保持独立的 cwd/workspace
- Hook 上下文只作用域于当前 prompt
- 会话锁在超时中止时安全释放
- 实时 OpenClaw 锁在清理过程中存活
- 避免陈旧的重启延续
- Codex app-server/helper 故障不再破坏共享运行时状态
- 中断的工具调用、陈旧的 session binding、压缩交接、媒体投递重试均更优雅地恢复

涉及的 PR：#87218, #86875, #87409, #87399, #87375, #88129, #88136, #88141, #88162, #88182

**🔗 相关链接**：
- Release: https://github.com/openclaw/openclaw/releases/tag/v2026.5.28

---

### 4. 外部化插件：Tokenjuice 与 GitHub Copilot
**📰 来源**：GitHub Release | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
Tokenjuice 正式作为 `@openclaw/tokenjuice` 插件通过 npm 和 ClawHub 发布。GitHub Copilot Agent 运行时也作为 `@openclaw/copilot` 插件外部化。这是一个重要的架构变化，将之前的捆绑组件拆分为独立插件，便于独立版本管理和社区贡献。

**🔗 相关链接**：
- GitHub: https://github.com/openclaw/openclaw

---

### 5. 渠道稳定性大升级
**📰 来源**：GitHub Release | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
跨渠道的消息投递和移动端交付大幅增强：
- Telegram、WhatsApp、iMessage、Slack、Discord、Microsoft Teams、Google Chat、Google Meet
- iOS 实时 Talk 增强：hosted push relay 默认值、WebSocket ping 路径
- 失败进度草稿的恢复（Discord/Telegram/Slack/Matrix/Teams）
- Discord REST 实体缓存增长限制
- 各渠道请求/重试计时器全面设限

涉及 PR：#88096, #88105, #88183, #88231, #83115, #88749

---

## 🧩 技能生态

### 6. 核心技能索引系统
**📰 来源**：GitHub Release | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
新增核心技能索引系统，集中化技能运行时加载、状态管理、过滤和 prompt 格式化。这是 Skill Workshop 的基础设施支撑。

---

## 💬 社区精选

### 7. Reddit r/OpenClawUseCases — v2026.4.12 隐藏功能讨论
**📰 来源**：Reddit | **🌐 语言**：英 | **✅ 验证状态**：已验证（1个月前）

**📝 核心内容**：
Reddit 社区深入分析了 v2026.4.12 更新日志中的隐藏细节，讨论 OpenClaw GitHub 发布功能、VPS 创新用例等。社区对新的 rate limit 错误处理和计费阈值拒绝能力给予积极反馈。

**🔗 相关链接**：
- Reddit: https://www.reddit.com/r/OpenClawUseCases/comments/1skza9u/whats_actually_hiding_in_the_openclaw_2026412/

---

### 8. Skywork 指南 & Petronella Tech 博客 — OpenClaw 2026 全面解读
**📰 来源**：Skywork / Petronella Technology | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
- **Skywork Guide**（4月26日）：详解 OpenClaw 2026.4.25 免费本地 AI Agent、多渠道消息、Google Meet 支持、DeepSeek 模型
- **Petronella Tech Blog**（5月6日）：追踪 OpenClaw 2026 全系列发布，涵盖 Active Memory、Task Brain、安全加固、破坏性变更和迁移指南

**🔗 相关链接**：
- Skywork: https://skywork.ai/skypage/en/openclaw-latest-release-guide/2048643673994948608
- Petronella Tech: https://petronellatech.com/blog/openclaw-ai-agent-guide-2026/

---

## 📈 数据洞察

| 指标 | 数值 | 趋势 |
|------|------|------|
| ⭐ GitHub Stars | **375,868** | 📈 持续增长 |
| 🍴 Forks | **78,478** | 📈 |
| 👁️ Watchers | **1,815** | ✅ |
| 🔧 Open Issues | **6,881** | — |
| 🏷️ 最新版本 | **v2026.5.31-beta.3** | 🔥 今日发布 |
| 🏷️ 最新稳定版 | **v2026.5.28** | ✅ 5月30日 |

---

## 🎯 重点关注

### 对个人部署的建议
1. **Skill Workshop** — 如果你是技能开发者，建议立即了解和配置 Skill Workshop 流程
2. **Tokenjuice / Copilot 插件** — 如果你使用这些功能，注意它们已外部化，需要显式安装
3. **渠道配置** — 本次更新对所有渠道进行了稳定性加固，建议重新检查各渠道配置

### 值得观察的趋势
- OpenClaw 正在从单体架构向**插件化、模块化**方向演进
- **Agent 自管理能力**（Skill Workshop）和**多 Agent 编排**（Workboard）成为新重点
- iOS 移动端体验持续增强

---
*报告生成时间：2026-06-01 06:00 CST | 数据来源：GitHub + 全球技术社区*

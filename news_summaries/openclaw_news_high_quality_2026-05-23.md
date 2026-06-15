# 🦞 OpenClaw日报 - 2026年05月23日

## 📊 今日概览
- **精选动态**：5条（中文2条，英文3条）
- **重点类别**：版本更新 🚀 | 安全加固 🔒 | 社区动态 💬
- **质量评级**：⭐⭐⭐⭐⭐

---

## 🚀 版本与功能

### 1. OpenClaw v2026.5.20 正式版发布（安全加固与Discord语音重大更新）

**📰 来源**：GitHub Releases | **🌐 语言**：英 | **✅ 验证状态**：✅ 已验证

**📝 核心内容**：

5月21日，OpenClaw发布了 **v2026.5.20** 正式稳定版本。这是继v2026.5.19之后的又一次快速迭代，包含大量安全加固和功能增强：

**🔐 安全加固（重点）：**
- **Exec审批**：移除了旧的 `cat SKILL.md && printf ... && <skill-wrapper>` allowlist兼容路径，Skill文件必须通过 read 工具加载，只有真正的Skill可执行文件被自动放行。这是对Skill安全性的重大提升。
- **凭证安全**：`doctor` 命令现在会警告 `openclaw.json` 中存储的明文敏感配置（包括API密钥和provider headers）(#84718)
- **Doctor增强**：新增沙箱工具策略与MCP服务器工具可见性检查 (#84699)

**🎤 Discord语音大更新（来自 @fuller-stack-dev）：**
- 语音会话现在可以跟随配置的Discord用户进入语音频道
- 支持多用户切换、有限 reconciliation 和 DAVE 恢复保留 (#84264)
- 语音实时会话默认注入有限的 `IDENTITY.md`、`USER.md`、`SOUL.md` 上下文，可配置文件关闭 (#84499)

**🆕 新功能：**
- **Policy插件**：新增内置Policy插件，支持基于策略的频道合规检查、doctor lint发现和可选的workspace修复 (#80407) 感谢 @giodl73-repo
- **xAI设备码OAuth**：远程和无头环境可通过设备码授权xAI，无需本地浏览器回调 (#84005) 感谢 @fuller-stack-dev
- **OpenRouter路由策略**：支持provider级别的 `params.provider` 路由策略 (#84005)
- **Agent本地模型优化**：新增 `agents.list[].experimental.localModelLean`，可为单个Agent单独启用精简本地模型模式
- **依赖升级**：Codex harness 更新至 `@openai/codex` `0.132.0`

**🐛 关键修复（共40+项）：**
- Cron任务运行不再阻塞主会话聊天 (#82766) 感谢 @galiniliev
- WhatsApp消息交付增强，30s轮询确保连接后发送 (#79083) 感谢 @Oviemudiaga
- macOS MLX TTS音频发布版修复 (#78792)
- 浏览器截图图片缩放策略对齐 (#84595)
- Ollama本地模型默认启用工具能力 (#84055)
- iOS TestFlight编译修复 (#84255)
- Control UI终端状态修正 (#84057)
- 大量subagent、compaction、Codex集成可靠性修复

**🔗 相关链接：**
- Release页面：https://github.com/openclaw/openclaw/releases/tag/v2026.5.20
- npm包：https://www.npmjs.com/package/openclaw/v/2026.5.20
- GitHub Actions CI：https://github.com/openclaw/openclaw/actions/runs/26248546974

---

### 2. OpenClaw v2026.5.19 版本 - Docker增强与依赖升级

**📰 来源**：GitHub Releases | **🌐 语言**：英 | **✅ 验证状态**：✅ 已验证

**📝 核心内容**：

5月19日发布的v2026.5.19版本主要包含：
- **Docker/Podman增强**：新增 `OPENCLAW_IMAGE_APT_PACKAGES` 构建参数，支持运行时中立的额外apt包安装，保留 `OPENCLAW_DOCKER_APT_PACKAGES` 作为兼容fallback (#62431)
- **依赖更新**：`@openclaw/proxyline` → 0.3.3, Pi packages → 0.75.1
- **Node.js版本**：最低支持提高到 22.19
- Agent修复默认采用clean bounded重构模式

**🔗 相关链接：**
- Release页面：https://github.com/openclaw/openclaw/releases/tag/v2026.5.19

---

### 3. 最新Commits动态（5月22日）

**📰 来源**：GitHub Commits | **🌐 语言**：英 | **✅ 验证状态**：✅ 已验证

**📝 核心内容**：

5月22日最新几次提交：
- 🆕 **feat: fresh CLI安装引导** - 新增CLI首次安装的onboarding体验 (#85519)
- 📝 **docs: 刷新贡献者文档** - Peter Steinberger更新了贡献指南
- 🔧 **fix(update): prepack npm git更新规格** - Jason修复npm更新问题
- 🔧 **fix: 简化聊天会话搜索** - 聊天搜索逻辑简化
- 🔧 **fix: 使用原生Mac设置侧边栏** - macOS原生设置体验优化

**🔗 相关链接：**
- Commits：https://github.com/openclaw/openclaw/commits/main

---

## 🧩 技能生态

### 4. OpenClaw飞书官方插件上线

**📰 来源**：飞书官方 | **🌐 语言**：中 | **✅ 验证状态**：✅ 已验证

**📝 核心内容**：

飞书官方发布了OpenClaw官方插件，一篇详细文章说明了插件的功能、安装和更新教程，包括：
- OpenClaw核心能力介绍
- 飞书插件具体功能场景
- 安装与配置步骤
- 常见问题排查

让用户在几分钟内完成飞书与OpenClaw的集成。

**🔗 相关链接：**
- 飞书文章：https://www.feishu.cn/content/article/7613711414611463386

---

### 5. Awesome OpenClaw Skills 中文官方库持续更新

**📰 来源**：GitHub | **🌐 语言**：中 | **✅ 验证状态**：✅ 已验证

**📝 核心内容**：

`clawdbot-ai/awesome-openclaw-skills-zh` 官方中文Skill库持续更新，包含Cursor CLI Agent (支持tmux自动化)、以及各类热门AI Agent技能的2026年更新版本。

**🔗 相关链接：**
- GitHub仓库：https://github.com/clawdbot-ai/awesome-openclaw-skills-zh

---

## 💬 社区精选

### 6. OpenClaw 2026.4.15 正式版更新一览（第三方评测）

**📰 来源**：scensmart.com | **🌐 语言**：中 | **✅ 验证状态**：✅ 已验证

**📝 核心内容**：

第三方技术博客详细介绍了OpenClaw 2026.4.15系列正式稳定版（4.15系列最终版）：
- 基于v2026.4.15-beta.1和beta.2迭代完成
- 修复30+项遗留问题
- 完成Claude Opus（原文指Claude Opus兼容性）等模型集成

**🔗 相关链接：**
- 文章：https://www.scensmart.com/news/openclaw-2026-4-15-official-version-update-list/

---

### 7. Reddit社区：2026.4.12更新隐藏内容讨论

**📰 来源**：Reddit r/OpenClawUseCases | **🌐 语言**：英 | **✅ 验证状态**：✅ 社区讨论

**📝 核心内容**：

Reddit社区用户讨论2026.4.12版本的变更日志，发现Anthropic provider模块进行了大量重构以处理新的速率限制错误和计费问题。社区活跃度持续增长。

**🔗 相关链接：**
- Reddit：https://www.reddit.com/r/OpenClawUseCases/comments/1skza9u/

---

## 📈 数据洞察

| 指标 | 数值 | 趋势 |
|------|------|------|
| ⭐ GitHub Stars | **373,988** | 📈 持续增长 |
| 🍴 Forks | **77,713** | 📈 活跃开发 |
| 🔧 Open Issues | **7,303** | 📊 维护良好 |
| 👁️ Watchers | **1,810** | 🟢 稳定 |
| 🚀 Latest Release | **v2026.5.20** | 🆕 昨日发布 |
| 📝 Last Commit | **2026-05-22** | 🟢 每日活跃 |
| 🖥️ Primary Language | **TypeScript** | ✅ |
| 🏷️ Topics | AI, Assistant, OpenClaw, Own-Your-Data | ✅ |

### 版本迭代节奏
- **2026.5.20** (05/21) - 正式稳定版 🆕
- **2026.5.20-beta.2** (05/21) - 测试版
- **2026.5.20-beta.1** (05/21) - 测试版
- **2026.5.19** (05/20) - 正式版
- **2026.5.19-beta.2** (05/19) - 测试版

平均每天发布1个版本，开发活跃度极高。

### 社区热度
- **知乎专栏**：多篇OpenClaw深度技术分析文章持续输出，阅读量大
- **Reddit r/OpenClawUseCases**：社区讨论活跃，聚焦技术细节
- **飞书官方**：发布官方集成插件，企业级应用推进
- **第三方生态**：n8n-claw（在n8n中运行OpenClaw agent）等衍生项目涌现

---

## 📌 本周重点总结

1. **🚀 v2026.5.20发布** - 安全加固是本周最大主题，exec审批路径清理、明文凭证警示、沙箱策略检查
2. **🎤 Discord语音重大升级** - 语音频道跟随、多用户切换，Agent配置注入能力
3. **🛡️ Policy插件发布** - 内置策略引擎加入，频道合规检查体系成型
4. **🌐 飞书官方插件上线** - 中国市场企业部署路径打通
5. **⚡ GitHub 37.4万星** - 距40万星仅差2.6万，社区增长迅猛

---
*报告生成时间：2026-05-23 06:00 CST | 数据来源：GitHub API + SerpAPI + 全球技术社区*

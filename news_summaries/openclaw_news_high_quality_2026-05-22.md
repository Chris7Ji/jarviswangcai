# 🦞 OpenClaw日报 - 2026年05月22日

## 📊 今日概览
- **精选动态**：10条（中文2条，英文8条）
- **重点类别**：版本更新、技能生态、社区动态
- **质量评级**：⭐⭐⭐⭐⭐

---

## 🚀 版本与功能

### 1. OpenClaw v2026.5.20 正式发布 — Discord语音增强 & 安全强化
**📰 来源**：GitHub Release | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
2026年5月21日，OpenClaw发布 v2026.5.20 稳定版。本次更新重点围绕Discord语音功能增强和安全加固：

- **Security/Exec审批**：移除了旧的 `cat SKILL.md && printf ... && <skill-wrapper>` allowlist兼容路径，现在Skill文件必须使用`read`工具加载，只有真实的Skill可执行文件被自动允许，大幅提升安全性
- **Discord语音增强**：语音会话现可跟随配置的Discord用户进入语音频道，支持多用户交接、有界 reconciliation 和 DAVE恢复保留（#84264 | @fuller-stack-dev）
- **Discord语音Profile上下文**：实时语音会话默认注入 `IDENTITY.md`、`USER.md`、`SOUL.md` 上下文，可通过 `voice.realtime.bootstrapContextFiles: []` 禁用（#84499 | @fuller-stack-dev）
- **Codex集成升级**：将捆绑的 Codex harness 升级至 `@openai/codex 0.132.0`
- **CLI/Policy插件**：新增 Policy 插件，支持基于策略的频道合规检查和 `doctor lint` 诊断（#80407 | @giodl73-repo）
- **xAI OAuth登录**：新增设备码OAuth登录，远程/无头环境无需本地浏览器即可授权xAI（#84005 | @fuller-stack-dev）
- **OpenRouter路由策略**：支持 provider 级别的 `params.provider` 路由策略（@amknight）
- **Agent本地模型**：新增 `agents.list[].experimental.localModelLean` 配置，可按Agent单独启用轻量本地模型模式

**🔗 相关链接**：
- Release页面：https://github.com/openclaw/openclaw/releases/tag/v2026.5.20

---

### 2. OpenClaw v2026.5.19 — Mac App大改版 & 新Skill加入
**📰 来源**：GitHub Release | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
2026年5月20日发布，关键更新：

- **Mac App全面焕新**：重新设计Settings页面，采用统一卡片布局、缓存导航，权限/语音/Skill/Cron/Exec/Debug面板更清晰
- **Meme Maker Skill**：新增表情包制作Skill，支持模板搜索、本地SVG/PNG渲染、Imgflip托管渲染和 Know Your Meme 来源链接
- **Gateway启动加速**：优化启动日志和插件服务启动时序，与频道sidecar重叠运行，降低重启就绪延迟（#83301 | @samzong）
- **Docker增强**：新增 `OPENCLAW_IMAGE_APT_PACKAGES` 构建参数
- **Skills CLI升级**：`openclaw skills install` 和 `openclaw skills update` 新增 `--global` 参数（#74466 | @Marvae）
- **浏览器增强**：快照中显示待处理和已处理的弹窗，新增 `browser dialog --dialog-id` 命令
- **依赖更新**：proxyline → 0.3.3, Pi → 0.75.1, Node.js最低版本提升至22.19

**🔗 相关链接**：
- Release页面：https://github.com/openclaw/openclaw/releases/tag/v2026.5.19

---

### 3. OpenClaw v2026.5.18 稳定版 — 控制UI与Mac App全面优化
**📰 来源**：GitHub Release | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
2026年5月18日发布的稳定 rollup 版本，整合了2026.5.14～2026.5.17 beta更新：

- **Control UI & Mac App**：更快的Settings、更清晰的聊天/会话控制、响应式日志、远程网关支持
- 包含2026.5.12以来的所有修复

**🔗 相关链接**：
- Release页面：https://github.com/openclaw/openclaw/releases/tag/v2026.5.18

---

### 4. 🆕 Apify Web搜索/抓取Provider插件
**📰 来源**：GitHub PR | **🌐 语言**：英 | **✅ 验证状态**：已验证（已合并）

**📝 核心内容**：
PR #84986 已合并，新增Apify作为bundled插件：

- **web_search**：使用RAG Web Browser actor，返回完整Markdown页面内容
- **web_fetch**：使用Website Content Crawler actor
- 解决内置 `web_fetch` 无法抓取JS渲染SPA和受保护页面（Cloudflare、PerimeterX、DataDome）的问题
- 内置 `web_search` 仅返回链接列表，Apify实现让Agent研究更深

**🔗 相关链接**：
- PR：https://github.com/openclaw/openclaw/pull/84986

---

## 🧩 技能生态

### 5. 🔄 `openclaw skills verify` — ClawHub信任卡支持
**📰 来源**：GitHub PR | **🌐 语言**：英 | **✅ 验证状态**：已验证（Open PR #85102）

**📝 核心内容**：
社区贡献者 @steipete 提交新功能 `openclaw skills verify <slug>`，受NVIDIA Verified Agent Skills启发：
- 验证指定 `--version` 或 `--tag` 的Skill
- 默认从 `.clawhub/origin.json` 获取已安装版本
- 从 ClawHub `/api/v1/skills/:slug/trust-card` 获取信任卡并进行验证
- 为 Skill 生态的安全治理打下了基础

**🔗 相关链接**：
- PR：https://github.com/openclaw/openclaw/pull/85102

### 6. 🎨 Meme Maker Skill正式加入
**📰 来源**：GitHub Release (v2026.5.19) | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
作为 v2026.5.19 的一部分，Meme Maker Skill 正式加入OpenClaw技能库：
- 精选模板搜索
- 本地SVG/PNG渲染
- Imgflip托管渲染
- Know Your Meme 出处链接

**🔗 相关链接**：
- Release：https://github.com/openclaw/openclaw/releases/tag/v2026.5.19

---

## 💬 社区精选

### 7. 🏢 OpenClaw After Hours @ GitHub HQ — Microsoft Build 2026期间
**📰 来源**：GitHub Blog | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
GitHub官方宣布，将在Microsoft Build 2026期间于GitHub总部举办 **OpenClaw: After Hours @ GitHub** 活动。OpenClaw构建者将齐聚一堂进行演示和交流。提供线下参与和Twitch直播两种方式。

**🔗 相关链接**：
- GitHub Blog：https://github.blog/open-source/register-now-for-openclaw-after-hours-github/

### 8. 🦞 OpenClaw GitHub Stars突破37.3万
**📰 来源**：GitHub | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
截至2026年5月22日，OpenClaw在GitHub上已获得 **373,751 颗星标**，Fork数 77,646，Open Issues 7,405。项目保持高速迭代，近三天内连续发布了 v2026.5.20、v2026.5.19 和 v2026.5.18 三个版本。

**🔗 相关链接**：
- GitHub：https://github.com/openclaw/openclaw

### 9. 📖 多篇OpenClaw 2026完整指南发布
**📰 来源**：Medium / PetronellaTech / Skywork | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
多家技术媒体发布OpenClaw 2026完整指南：
- **Medium**（Data Science Collective）："355K GitHub Stars in 5 Months" — 分析了OpenClaw 5个月从零到35.5万星标的增长曲线
- **PetronellaTech**：详细部署指南，涵盖CMMC、HIPAA、ITAR合规的私有GPU基础设施部署
- **Skywork.ai**：2026.4.25版本功能亮点，包括 Google Meet 支持、DeepSeek模型集成

**🔗 相关链接**：
- Medium：https://medium.com/data-science-collective/355k-github-stars-in-5-months-17-defense-rate-the-complete-honest-guide-to-openclaw-28d2f59598e1
- PetronellaTech：https://petronellatech.com/blog/openclaw-ai-agent-guide-2026/
- Skywork：https://skywork.ai/skypage/en/openclaw-latest-release-guide/2048643673994948608

### 10. Matrix集成增强 — 线程内@提及可绕过
**📰 来源**：GitHub PR | **🌐 语言**：英 | **✅ 验证状态**：已验证（已合并）

**📝 核心内容**：
PR #85112 合并 — `feat(matrix): opt-in mention bypass for in-thread replies`。为Matrix频道添加 `threadBindings.bypassMentionInBoundThreads` 配置，允许线程内回复可选绕过@提及。

**🔗 相关链接**：
- PR：https://github.com/openclaw/openclaw/pull/85112

---

## 📈 数据洞察

### GitHub仓库关键指标
| 指标 | 数值 |
|------|------|
| ⭐ GitHub Stars | **373,751** |
| 🍴 Forks | 77,646 |
| 🔧 Open Issues | 7,405 |
| 🏷️ npm最新版 | **2026.5.20** |
| 📅 最后推送 | 2026-05-21 22:02 UTC |

### 活跃度亮点
- **3天3个版本**：v2026.5.18 → v2026.5.19 → v2026.5.20 的快速迭代节奏
- **Discord语音**成为本周最大功能亮点，获得两位贡献者(@fuller-stack-dev)的连续PR
- **Apify Provider**解决JS渲染页面抓取的长期痛点
- **Skill信任机制**向成熟生态迈出重要一步

### 重点Bug修复
- Codex app-server `item/completed` 后卡死问题修复 (#85107, #84076)
- Discord会话恢复abort归属问题 (#85100)
- Session存储内存占用优化 (#84693)
- Discord组件注册错误日志增强 (#84190)

---

---
*报告生成时间：2026-05-22 06:02 CST | 数据来源：GitHub API + SerpAPI + 全球技术社区*

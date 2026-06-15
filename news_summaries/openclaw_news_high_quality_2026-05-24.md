# 🦞 OpenClaw日报 - 2026年5月24日

## 📊 今日概览
- **精选动态**：6条（中文2条，英文4条）
- **重点类别**：版本更新 | 功能特性 | 文档改进 | 社区生态
- **质量评级**：⭐⭐⭐⭐⭐

---

## 🚀 版本与功能

### 1. OpenClaw v2026.5.20 稳定版发布 — 重大特性更新
**📰 来源**：GitHub Release | **🌐 语言**：英 | **✅ 验证状态**：已验证 ✅

**📝 核心内容**：
5月21日，OpenClaw发布 **v2026.5.20** 稳定版，包含多项核心功能改进：

**新功能：**
- 🔐 **Exec审批安全加固**：移除旧的 `cat SKILL.md && printf ...` 白名单兼容路径，Skill文件必须通过 `read` 工具加载，仅真正的Skill可执行文件被自动允许
- 🎤 **Discord语音会话增强**：支持跟随被配置用户进入语音频道，允许频道检查、多用户切换、边界协调和DAVE恢复保持
- 📄 **Discord/语音配置注入**：默认在实时语音会话中注入 `IDENTITY.md`、`USER.md`、`SOUL.md` 文件上下文，可通过 `voice.realtime.bootstrapContextFiles: []` 禁用
- 🔧 **Policy插件**：新增内置Policy插件，提供策略驱动的频道一致性检查、`doctor` lint发现和可选的workspace修复
- 🤖 **本地模型Lean模式**：允许按Agent启用 `experimental.localModelLean`，而非全局设置
- ✅ **xAI设备码OAuth登录**：远程和headless设置无需浏览器回调即可授权xAI
- 🔀 **OpenRouter路由策略**：支持provider级别 `params.provider` 路由策略

**重要修复（部分）：**
- Codex app-server系统提示报告修复
- MiniMax音乐生成duration控制修复
- WhatsApp更新Baileys至7.0.0-rc12
- 浏览器截图图像缩放策略对齐
- Doctor新增明文密钥配置警告
- Cron任务隔离和恢复改进
- 内存搜索超时自动关闭embedding provider
- 超过40项各类修复

**📊 下载验证**：
- npm包: [openclaw@2026.5.20](https://www.npmjs.com/package/openclaw/v/2026.5.20)
- macOS: [OpenClaw-2026.5.20.dmg](https://github.com/openclaw/openclaw/releases/download/v2026.5.20/OpenClaw-2026.5.20.dmg)
- 完整性：`sha512-cgshS76CxS3Vp9NGtJR2UGtVZxVR5/4rvok8DKGGL19DugAftNabsXfYajyAEiJ3dC8QTXNqF62MdQNzUnQe8Q==`

**🔗 相关链接**：
- Release页面：https://github.com/openclaw/openclaw/releases/tag/v2026.5.20
- NPM包：https://www.npmjs.com/package/openclaw/v/2026.5.20

---

### 2. OpenClaw v2026.5.22-beta.1 发布 — 大规模文档修订
**📰 来源**：GitHub Release (Prerelease) | **🌐 语言**：英 | **✅ 验证状态**：已验证 ✅

**📝 核心内容**：
5月23日发布的beta版本，核心亮点是大规模文档改进：
- README入门和Gateway启动路径澄清
- WhatsApp QR码/408恢复指南
- Cron输出语言提示配置
- Skill高级功能文档
- Gateway上游403故障排除
- 插件fallback覆盖指南
- 上下文剪裁比例边界说明
- 本地Dashboard恢复指南
- CLI环境标记说明
- Peekaboo Bridge子进程权限说明
- Crabbox/Testbox：从临时完整checkout运行干净的sparse-checkout同步
- 合并多项社区文档贡献，感谢 @deepujain、@Zacxxx、@Jah-yee、@neyric、@usimic 等数十位贡献者

**🔗 相关链接**：
- Release页面：https://github.com/openclaw/openclaw/releases/tag/v2026.5.22-beta.1

---

### 3. 过去24小时GitHub活跃开发 — Codex集成测试与功能增强
**📰 来源**：GitHub Commits | **🌐 语言**：英 | **✅ 验证状态**：已验证 ✅

**📝 核心内容**：
5月23日（周六）Peter Steinberger团队仍在密集提交，主要变更包括：

- **feat(agents)**: 暴露估算上下文预算状态 — Gio Della-Libera新增Session条目和Gateway会话行的路径无关上下文预算状态展示，在provider使用信息可用时渲染状态
- **feat(whatsapp)**: 支持emoji审批反应 — Kevin Lin实现WhatsApp通过emoji反应进行审批确认
- **fix(discord)**: 保持强制语音咨询诊断私有 — Jason修复discord和电话实时咨询负载中的诊断泄露
- **fix**: Codex图片API密钥路由至OpenAI — Peter Steinberger
- 数十次Codex app-server集成测试隔离修复

**🔗 相关链接**：
- Commit历史：https://github.com/openclaw/openclaw/commits/main

---

## 🧩 技能与生态

### 4. SkillClaw开源 — 集体进化的智能技能框架
**📰 来源**：GitHub (AMAP-ML/SkillClaw) | **🌐 语言**：英 | **✅ 验证状态**：已验证 ✅

**📝 核心内容**：
SkillClaw项目于2026年4月10日开源。该项目使LLM Agent能够通过集体进化机制逐步提升技能，由Agentic Evolver驱动技能协同进化。适合需要自主学习和技能优化的OpenClaw部署场景。

**🔗 相关链接**：
- GitHub仓库：https://github.com/AMAP-ML/SkillClaw

---

### 5. ClawSec安全技能套件 — 完整的安全防护方案
**📰 来源**：GitHub (prompt-security/clawsec) | **🌐 语言**：英 | **✅ 验证状态**：已验证 ✅

**📝 核心内容**：
ClawSec是一套完整的OpenClaw安全技能套件，同样支持Hermes、PicoClaw和NanoClaw Agent变体。主要功能：
- SOUL.md 等关键文件漂移检测
- 实时威胁监控
- 安全策略自动化执行
- 兼容OpenClaw安全生态

**🔗 相关链接**：
- GitHub仓库：https://github.com/prompt-security/clawsec

---

## 💬 社区精选

### 6. 中文社区 — OpenClaw飞书官方插件上线
**📰 来源**：飞书官方 | **🌐 语言**：中 | **✅ 验证状态**：已验证 ✅

**📝 核心内容**：
飞书官方发布OpenClaw飞书插件详尽教程，涵盖功能说明、安装更新教程和常见问题排查。用户可几分钟内完成飞书与OpenClaw的集成部署，实现IM消息驱动的AI Agent管理。

**🔗 相关链接**：
- 飞书文章：https://www.feishu.cn/content/article/7613711414611463386

---

## 📈 数据洞察

| 指标 | 数值 | 趋势 |
|------|------|------|
| ⭐ GitHub Stars | **374,171** | 稳定增长 |
| 🍴 Forks | **77,801** | 持续上升 |
| 📋 Open Issues | **7,156** | - |
| 🚀 最新Release | **v2026.5.20 (stable)** / v2026.5.22-beta.1 | 双版本活跃 |
| 👨‍💻 Core Contributors | Peter Steinberger, Gio Della-Libera, Kevin Lin, Jason 等 | 周末仍在提交 |
| ⏱ Last Push | 2026-05-23 21:55 UTC | 24小时内活跃 |

---

*报告生成时间：2026-05-24 06:00 CST | 数据来源：GitHub API + SerpAPI 全球搜索*

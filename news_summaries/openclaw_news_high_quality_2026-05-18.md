# 🦞 OpenClaw日报 - 2026年05月18日

## 📊 今日概览
- **精选动态**：13条（中文0条，英文13条）
- **重点类别**：版本更新 / 技能生态 / 社区动态 / 基础设施
- **质量评级**：⭐⭐⭐⭐⭐（全部来源于GitHub官方仓库）
- **数据速览**：
  - GitHub Stars: 372,670 ⭐ | Forks: 77,261 | Watchers: 1805
  - 最新稳定版：**v2026.5.12** (npm) | 最新 Beta：**v2026.5.16-beta.5**
  - 过去24h提交：30+ commits
  - awesome-openclaw-skills: 48,862 ⭐ | 5,400+ Skills

---

## 🚀 版本与功能

### 1. OpenClaw v2026.5.16 Beta 5 发布
**📰 来源**：GitHub Tags | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
Peter Steinberger 于 5月17日17:17 UTC 签署发布了 **v2026.5.16-beta.5** 标签。从 v2026.5.12 到该 beta 版本之间有 **250+ commits**，包含大量功能增强和Bug修复。

**🔥 重点新增功能**：
- **工具插件创作系统** (`feat: add simple tool plugin authoring`) — 新增简化的工具插件开发框架，配套创作指南
- **Presentation 能力限制** (`feat: add presentation capability limits`) — 限制 Agent 展示内容的输出能力
- **Teams Adaptive Cards 渲染** (`feat: render Teams presentations as Adaptive Cards`) — 支持 Microsoft Teams 自适应卡片展示
- **新 Skills**：meme maker、debugger diagram & spike、crawl archive、python debugpy
- **Codex 运行时路由修复** — OpenAI Codex 运行时路由终于修复 (#82864)
- **Codex 原生工具轨迹记录** — `fix(codex): record native tool trajectories`
- **Gateway 重启稳定性增强** — unmanaged restart 保持 in-process，减少断开

**🔗 相关链接**：
- Tag 签名：`v2026.5.16-beta.5` (https://github.com/openclaw/openclaw/releases/tag/v2026.5.16-beta.5)
- Change comparison: https://github.com/openclaw/openclaw/compare/v2026.5.12...v2026.5.16-beta.5

---

### 2. MCP 工具 Schema 内联本地引用修复
**📰 来源**：GitHub Commit | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
Gio Della-Libera 提交 `fix(mcp): inline local refs in bundled tool schemas (#81238)`，修复了 MCP 工具 Schema 中本地引用未能正确内联打包的问题，对使用 MCP 协议的 Skill/Plugin 开发者影响重大。

**🔗 相关链接**：
- Commit: https://github.com/openclaw/openclaw/commit/b7f3d01633e5

---

### 3. Gateway 协议诊断与 v4 协议恢复
**📰 来源**：GitHub Commit | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
Peter Steinberger 提交了多项 Gateway 关键修复：
- `fix: improve gateway protocol mismatch diagnostics (#82908)` — 优化协议不匹配的诊断信息
- `fix(gateway): restore v4 message action protocol` — 恢复 v4 消息操作协议兼容性
- `fix(gateway): explain protocol mismatches` — 更清楚地解释协议不匹配原因
- `fix(gateway): allow trusted-proxy local-direct password fallback (#82953)` — 允许 trusted-proxy 配置下本地密码回退

**🔗 相关链接**：
- Commit: https://github.com/openclaw/openclaw/commit/38b3e7362272
- Commit: https://github.com/openclaw/openclaw/commit/ad155fbbd7b3

---

### 4. OpenAI Codex 运行时全面修复
**📰 来源**：GitHub Commit | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
多项 Codex 相关改进入 commPit：
- `Fix OpenAI Codex runtime provider routing (#82864)` — 修复 Codex 运行时路由
- `fix(codex): record native tool trajectories` — 记录原生工具轨迹
- `fix(codex): preserve streamed command output (#83222)` — 保持流式命令输出
- `fix(codex): deliver Telegram verbose tool progress (#83214)` — Telegram 详细工具进度
- `fix(codex): preserve nested tool-result middleware output` — 嵌套工具结果中间件输出
- `Guard Codex app-server context budgets` — Codex app-server 上下文预算防护
- `fix: avoid idle Codex hook relay subprocesses` — 避免空闲 hook 中继子进程

**🔗 相关链接**：
- Commit: https://github.com/openclaw/openclaw/commit/58f1db1bc8eb
- Commit: https://github.com/openclaw/openclaw/commit/d1638f1185df

---

## 🧩 技能生态

### 5. awesome-openclaw-skills 突破 48K Stars
**📰 来源**：GitHub | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
`VoltAgent/awesome-openclaw-skills` 仓库现已收录 **5,400+ Skills**，Stars 达 **48,862**。近24小时新增 Skills 包括 **Parley**（对话工具）等。上周新增的 Skills 包括 `vistoya/vistoya`、`accli-plus`（日程管理）、`trent-ai-release/trentclaw` 等。

**🔗 相关链接**：
- Repository: https://github.com/VoltAgent/awesome-openclaw-skills

---

### 6. OpenClaw 官方仓库新增 Skills
**📰 来源**：GitHub Commit | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
官方仓库在 v2026.5.16-beta 生命周期中直接新增了多个内置 Skills：

| Skill | 类型 | 用途 |
|-------|------|------|
| 🎭 meme maker | 娱乐 | 制作表情包 |
| 🐛 debugger diagram & spike | 开发调试 | 调试器图表与 Spike 工具 |
| 📥 crawl archive | 数据收集 | 网页归档爬取 |
| 🐍 python debugpy | 开发调试 | Python Debug 协议支持 |
| 🔄 autoreview (原 codex review) | 代码审查 | Codex 代码自动审查 |

**🔗 相关链接**：
- Commit: https://github.com/openclaw/openclaw/commit/b7704b917e10
- Commit: https://github.com/openclaw/openclaw/commit/0591b3138834

---

## 🔧 基础设施与稳定性

### 7. Agent 子系统多项关键修复
**📰 来源**：GitHub | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
- `fix(agents): persist subagent registry before returning accepted (#83132)` — 子Agent注册表持久化
- `fix(agents): preserve run-mode keep subagents past session sweep TTL (#83132)` — 保持 run-mode 子Agent 超出 sweep TTL
- `fix(agents): exclude tool result details from guard budget (#75525)` — 排除工具结果细节免于守卫预算计算
- `fix(agents): classify ACP no-output stalls` — 分类 ACP 无输出卡顿
- `fix(agents): skip malformed transcript state entries (#82624)` — 跳过畸形转录状态
- `fix(agents): preserve suspended subagent final deliveries (#82999)` — 保持挂起子Agent最终投递
- `fix: route subagent announce to originating parent session` — 子Agent通知路由到父会话

**🔗 相关链接**：
- Commit: https://github.com/openclaw/openclaw/commit/214f718be7b3

---

### 8. 内存系统改进
**📰 来源**：GitHub | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
- `fix(memory): preserve qmd lexical search for hyphenated queries (#81423)` — 修复连字符查询的词汇搜索
- `fix(memory): clarify vector degradation warning` — 明确向量退化警告信息
- `fix: explain memory compaction tool allowlist warnings` — 解释内存压缩工具 allowlist 警告

**🔗 相关链接**：
- Commit: https://github.com/openclaw/openclaw/commit/44c3d8ea2efd

---

### 9. Telegram 通道多项修复
**📰 来源**：GitHub | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
- `Fix Telegram stop debounce bypass (#83248)` — 修复 Telegram stop 去抖动绕过
- `Log Telegram outbound delivery success (#83247)` — 新增 Telegram 发送成功日志
- `fix(codex): deliver Telegram verbose tool progress (#83214)` — Codex 在 Telegram 上展示详细工具进度

**🔗 相关链接**：
- Commit: https://github.com/openclaw/openclaw/commit/aa71f7fe1568

---

### 10. 插件系统强化
**📰 来源**：GitHub | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
- `fix(plugins): surface configured runtime plugin doctor warnings (#81674)` — 插件 Doctor 配置警告
- `fix(plugins): default 15s timeout for before_agent_start hook (#48534) (#83147)` — 默认插件启动钩子超时
- `fix(build): bundle zod inline to fix pnpm global install resolution (#78515)` — Zod 内联打包修复 pnpm 全局安装

**🔗 相关链接**：
- Commit: https://github.com/openclaw/openclaw/commit/9a11e764589c

---

### 11. 飞书(Feishu)通道修复
**📰 来源**：GitHub | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
- `fix(feishu): return subagent thread delivery origin (#83190)` — 修复子Agent线程投递来源
- `fix(feishu): refresh inbound session routes` — 刷新入站会话路由

**🔗 相关链接**：
- Commit: https://github.com/openclaw/openclaw/commit/7c416950c615

---

### 12. Doctor 健康检查系统增强
**📰 来源**：GitHub | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
Gio Della-Libera 提交 `Doctor: add health-check contract and --lint validation (#80055)`，为 `openclaw doctor` 命令新增健康检查合约和 `--lint` 验证模式，配合 `fix(doctor): detect stale session snapshot paths (#82867)` 增强诊断能力。

**🔗 相关链接**：
- Commit: https://github.com/openclaw/openclaw/commit/9a5f2f61e76f

---

## 💬 社区精选

### 13. Issues 与 Bug 报告
**📰 来源**：GitHub Issues | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
过去24小时新增的 Issues 和 PRs：

| # | 标题 | 类型 | 标签 |
|---|------|------|------|
| #83280 | `openclaw infer model run` exits 0 when provider returns empty output | 🐛 Bug | P2, bug, auth-provider |
| #83279 | fix(heartbeat): rename target-none skip reason to delivery-disabled | 🔧 PR | XS |
| #83278 | fix(telegram): delete progress draft before final reply | 🔧 PR | XS, telegram |
| #83277 | WhatsApp channel login provider unavailable on Windows | 🐛 Bug | P2, auth-provider |
| #83276 | feat: Generic tool-call interrupt primitive for HITL workflows | 💡 Feature | P3 |

**🔗 相关链接**：
- All issues: https://github.com/openclaw/openclaw/issues

---

## 📈 数据洞察

| 指标 | 当前值 | 变化趋势 |
|------|--------|----------|
| ⭐ GitHub Stars | **372,670** | 📈 持续增长中 |
| 🍴 Forks | 77,261 | — |
| 👁️ Watchers | 1,805 | — |
| 📦 npm 最新稳定版 | **v2026.5.12** | — |
| 🔬 npm 最新 Beta | v2026.5.16-beta.x 系列 | — |
| 🛠️ Open Issues | 6,967 | 活跃项目管理 |
| 🧩 awesome Skills | **5,400+** | 持续扩展 |
| 💻 主语言 | TypeScript | MIT License |
| 🗓️ 项目创建 | 2025-11-24 | 不到6个月时间！ |

**生态亮点**：OpenClaw 仅用不到6个月时间就从零增长到 372K+ Stars，超越了众多成熟的 AI 开源项目，展现出极其强劲的增长势头。

---

## 🔮 趋势展望

1. **Codex 集成深化**：多项 Codex 相关修复表明 OpenClaw 正积极与 OpenAI Codex 生态融合
2. **Plugin SDK 成熟化**：工具插件创作系统、SDK 别名等表明插件生态正走向标准化
3. **企业级通道拓展**：Teams、飞书（Feishu）通道持续改进
4. **Gateway 稳定性**：协议诊断、非管理重启、trusted-proxy 等提升生产环境可靠性
5. **Skills 生态爆发**：5,400+ Skills 和 48K+ Stars 的 awesome 生态说明社区参与度极高

---
*报告生成时间：2026-05-18 06:00 CST | 数据来源：GitHub API + npm registry | 生成方式：自动化检索+人工摘要*

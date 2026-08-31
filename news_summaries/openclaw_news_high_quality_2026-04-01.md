# 🦞 OpenClaw日报 - 2026年04月01日

## 📊 今日概览
- 精选动态：3条（中文1条，英文2条）
- 重点类别：[版本更新/技能生态/安全修复]
- 质量评级：⭐⭐⭐⭐⭐

---

## 🚀 版本与功能

### 1. 🎉 v2026.3.31 重磅发布：内置QQ Bot与全新任务流引擎
**📰 来源**：GitHub Official Release | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
OpenClaw v2026.3.31 稳定版已于 2026-03-31 20:54 UTC 正式发布。本次更新带来了基础架构的全面升级与多平台拓展：

- **重大变更 (Breaking)**：
  - `Nodes/exec` 移除了冗余的 shell wrapper，确保节点执行强制通过安全通道。
  - `Plugin SDK` 弃用了旧版兼容层。
  - `Skills/Plugins` 安装现在默认拦截危险代码（Fail Closed），提升了生态系统整体安全性。
  - 网关（Gateway）节点命令在设备完成配对确认前默认保持禁用状态。

- **核心功能增强 (Changes)**：
  - **后台任务革命**：统一 ACP、Subagent、Cron 与后台 CLI 执行，全部迁移至由 SQLite 驱动的全新任务流水线账本（Ledger）中，并新增了 `openclaw flows list|show|cancel` 线性任务流控制面板。
  - **QQ Bot 原生支持**：将 QQ Bot 设为内置（Bundled）频道插件，支持多账号、SecretRef 凭证保护、斜杠命令及多媒体收发。
  - **LINE 媒体增强**：在 LINE 频道上新增了图片、视频及音频的出站发送能力。
  - **MCP 扩展**：新增远程 HTTP/SSE MCP 服务器支持，并支持 Auth Headers 与凭证脱敏。
  - **Microsoft Teams 集成**：新增基于 Graph API 的成员信息解析 Action。

**🔗 相关链接**：
- Release页面：https://github.com/openclaw/openclaw/releases/tag/v2026.3.31

---

## 🧩 技能生态

### 1. WhatsApp 互动与 MCP 协议升级
**📰 来源**：GitHub Discussions/Commits | **🌐 语言**：英 | **✅ 验证状态**：已验证

**📝 核心内容**：
- **WhatsApp Emoji 互动**：Agent 现在可以使用 Emoji 对 WhatsApp 的传入消息进行原生 React 响应，交互更加拟人化（例如用 ❤️ 回应图片，而不必发送文本回复）。
- **Pi/Codex 原生搜索**：为内嵌的 Pi 运行环境新增了原生 Codex 网络搜索支持，内置引导和文档。
- **MCP 行为优化**：捆绑的 MCP 工具现在统一采用了服务安全的名称格式 (`serverName__toolName`)，并支持可选的 `streamable-http` 传输选择和每服务器连接超时控制。

---

## 🔐 社区精选与安全修复

### 1. 全方位安全沙箱与执行加固
**📰 来源**：OpenClaw Security Advisory | **🌐 语言**：中/英 | **✅ 验证状态**：已验证

**📝 核心内容**：
在最新发布中，包含大量涉及主机执行（Exec）和沙箱（Sandbox）的安全防御加固，社区反应热烈：
- 阻止了请求范围内的 Proxy、TLS 和 Docker 环境变量覆盖，防止宿主流量被悄悄重定向。
- 修复了 macOS 执行下的 `caffeinate` 和 `sandbox-exec` 的安全解包逻辑，防止被恶意包装的命令意外获得永久信任。
- 对 Discord 语音接入进行了身份验证校验，确保只有白名单频道的成员能发送语音指令。

---

## 📈 数据洞察
- **发布速度与热度**：v2026.3.31 发布仅一小时，即获大量核心维护者与社区成员（51 位提及开发者）关注与点赞。
- **活跃维护者**：本次发布由 @steipete 领衔发布，并涵盖了 @jacobtomlinson, @vincentkoc, @sliverp, @mbelinky 等数十位贡献者的关键 Commit。
- **仓库趋势**：基于上周末（v2026.3.28）爆发式的 187+ 提交后，今日版本快速稳定了关键 API 与通道插件。

---
*报告生成时间：2026-04-01 06:00 | 数据来源：GitHub + 全球技术社区*
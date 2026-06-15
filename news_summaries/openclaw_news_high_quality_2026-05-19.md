# 🦞 OpenClaw日报 - 2026年05月19日

## 📊 今日概览
- **精选动态**：12条（中文0条，英文12条）
- **重点类别**：版本更新、技能生态、插件社区
- **质量评级**：⭐⭐⭐⭐⭐

> ⚠️ 说明：SerpAPI搜索配额已耗尽，数据来源为GitHub API直接采集，均为已验证信息。

---

## 🚀 版本与功能

### 1. OpenClaw v2026.5.18 稳定版发布
**📰 来源**：GitHub Release | **🌐 语言**：英 | **✅ 验证状态**：✅ 已验证

**📝 核心内容**：
2026年5月18日，OpenClaw发布 v2026.5.18 稳定版本。主要更新包括：

**变化亮点：**
- **依赖更新**：`@openclaw/proxyline` 升级至 0.3.3，Pi 包升级至 0.75.1，最低 Node.js 版本提升至 22.19
- **Docker/Podman**：新增 `OPENCLAW_IMAGE_APT_PACKAGES` 运行时无关镜像构建参数（#62431，感谢 @urtabajev）
- **Gateway/ACPX**：启动探测、配置、运行时和资源计数成本归因到重启追踪（#83300，感谢 @samzong）
- **Gateway**：重叠启动日志与插件服务启动，减少重启就绪延迟（#83301，感谢 @samzong）
- **插件/admin-http-rpc**：允许受信任的HTTP RPC客户端启动和等待Web QR登录流程（#83259，感谢 @liorb-mountapps）
- **Mac应用**：重新设计设置页面，采用一致的卡片布局、缓存导航、更干净的权限/语音/技能/cron/exec/调试窗格
- **技能**：将Codex结算审核技能重命名为 `autoreview`；新增 meme-maker 技能（Imgflip托管渲染 + Know Your Meme溯源）
- **技能新增**：节点检查器调试、融合图表生成、快速原型工作流技能
- **CLI/插件**：新增 `defineToolPlugin` 及 `openclaw plugins build`、`validate`、`init` 命令
- **技能更新**：Obsidian技能转向官方 `obsidian` CLI；新增Python调试技能（pdb、breakpoint、debugpy远程附加）
- **代理**：支持HTTPS管理正向代理端点及 `proxy.tls.caFile` CA信任配置（#79171，感谢 @jesse-merhi）
- **QA-Lab**：新增20轮和可选100轮运行时一致性场景
- **Android**：Talk模式转为实时的 Gateway 中继语音会话（流式麦克风输入、实时音频播放、工具结果桥接、屏幕转录）（#83130，感谢 @sliekens）

**修复亮点：**
- Discord/OpenAI：实时语音会话后续轮次保持畅通（#80505，感谢 @Solvely-Colin）
- 媒体：防止外部解码器代理对无法识别图像的处理
- Telegram：论坛话题中媒体交付修复（#83556，感谢 @fuller-stack-dev）
- xAI插件：PKCE挑战字段在OAuth授权码令牌交换中的兼容性（#83499）
- Codex应用服务器：内联图片附件在队列运行前的水化处理（#83466）
- CLI/TUI：强制独立 `/exit` 运行终止（#83501）
- 多个QQBot、Discord、Telegram、WhatsApp渠道修复
- Xiaomi Moonshot/Kimi余额耗尽429分类为计费错误

**🔗 相关链接**：
- Release页面：https://github.com/openclaw/openclaw/releases/tag/v2026.5.18
- 完整变更日志：https://github.com/openclaw/openclaw/releases/tag/v2026.5.18

---

### 2. v2026.5.18-beta.1 预发布
**📰 来源**：GitHub Release | **🌐 语言**：英 | **✅ 验证状态**：✅ 已验证

**📝 核心内容**：
与v2026.5.18稳定版基本相同的变更集，提前数小时发布作为beta测试。

**🔗 相关链接**：
- Release页面：https://github.com/openclaw/openclaw/releases/tag/v2026.5.18-beta.1

---

### 3. v2026.5.16-beta.7 — Mac设置页面重新设计
**📰 来源**：GitHub Release | **🌐 语言**：英 | **✅ 验证状态**：✅ 已验证

**📝 核心内容**：
- **Mac应用**：设置页面全新设计，统一卡片布局、缓存导航、更干净的权限/语音/技能/cron/exec/调试窗格
- **技能**：新增 meme-maker 技能（模板搜索、SVG/PNG渲染、Imgflip托管、KYM溯源链接）
- `@openclaw/proxyline` 更新至0.3.3

**🔗 相关链接**：
- Release页面：https://github.com/openclaw/openclaw/releases/tag/v2026.5.16-beta.7

---

### 4. 近期重要Commits（过去24小时）
**📰 来源**：GitHub | **🌐 语言**：英 | **✅ 验证状态**：✅ 已验证

**📝 核心内容**：
- `9968db6` — Tak Hoffman: fix(github): 保留clawsweeper证明标签（#83781）
- `d124c5a` — Super Zheng: fix(cli): 修复因环境变量泄漏导致的配置设置测试不稳定问题（#83423）
- `721ad15` — Patrick Erichsen: fix: 将会话间溯源信息从转录中排除（#83755）
- `b2c5ba6` — Andy Ye: fix(outbound): 解析可发送通道注册表（#83733）
- `424c6d0` — clawsweeper[bot]: fix(auto-reply): 使WebChat的textChunkLimit/chunkMode配置覆盖生效（#83742）

**🔗 相关链接**：
- https://github.com/openclaw/openclaw/commits/main

---

## 📊 生态数据

### OpenClaw核心仓库
| 指标 | 数值 |
|------|------|
| ⭐ GitHub Stars | **372,960** |
| 🍴 Forks | 77,352 |
| 📋 Open Issues | 7,068 |
| 🔄 最后更新 | 2026-05-18 22:10 UTC |
| 📝 描述 | Your own personal AI assistant. Any OS. Any Platform. 🦞 |

### 热门插件/技能排行
| 排名 | 项目 | ⭐ Stars | 描述 |
|:----:|------|:-------:|------|
| 🥇 | **lossless-claw** | **4,744** | LCM (Lossless Context Management) 插件 |
| 🥈 | **tweetclaw** | **39** | X/Twitter搜索、发推、管理、媒体导出、抽奖 |
| 🥉 | **forge** | **12** | 目标、专注与心理健康的插件 |
| 4 | **tlon** | **7** | Tlon/Urbit渠道插件 |
| 5 | **OpenClawChineseTranslation** | **6** | 🌐 中文翻译，一小时内自动同步官方更新 |

---

## 🧩 技能生态

### 新增技能
1. **meme-maker skill** — 模因图生成技能，支持模板搜索、SVG/PNG本地渲染、Imgflip托管渲染、Know Your Meme溯源链接
2. **node inspector debugging skill** — 节点检查器调试技能
3. **fused diagram generation skill** — 融合图表生成技能
4. **throwaway spike workflow skill** — 快速原型工作流技能
5. **Python debugging skill** — Python调试技能（pdb、breakpoint()、post-mortem检查、debugpy远程附加）

### 技能更新
- **Obsidian skill** — 转向官方 `obsidian` CLI，不再使用第三方 `obsidian-cli`
- **Codex closeout review skill** — 重命名为 `autoreview`，保留Codex优先的回退行为

### 新插件/工具
- **`defineToolPlugin`** + `openclaw plugins build`、`validate`、`init` — 用于类型化简单工具插件的CLI生态
- **admin-http-rpc插件** — 允许受信HTTP RPC客户端启动和等待Web QR登录流程

---

## 💬 社区精选

### 热门GitHub讨论
- **#52951**: feat: 添加 `tools.fs.roots` — 按代理设置文件系统根目录及访问模式（52条评论）
- **#70864**: feat: 添加作用域提及模式策略（215条评论）
- **#69312**: fix: 防止从缩进代码块中误提取 MEDIA（149条评论）
- **#36630**: fix(signal): 完整双向引用回复支持
- **#43793**: feat(tui): 断连时显示重连提示并自动探测Gateway

### 社区插件推荐
- **Adverant-Nexus-Plugin-OpenClaw** — 多通道AI助手，100+技能与Nexus集成
- **nextclaw** — Postgres + pgvector 长时记忆插件（4级召回、新华字典索引、确定性优先导入）
- **quality-guard** — 实时阻止危险Shell命令并检查工具输出质量
- **openclaw-agent-sdk-plugin** — 通过Anthropic Agent SDK驱动Claude Code

---

## 📈 数据洞察

- **核心仓库**：372,960 Stars，较前日持续增长，开源AI助手赛道热度不减
- **插件生态**：lossless-claw（4,744⭐）持续巩固其领先地位，成为OpenClaw最受欢迎的独立插件
- **QA-Lab体系**：大幅扩展的QA测试框架标志着OpenClaw向企业级稳定性迈进，新增Codex-vs-Pi运行时一致性测试、20-turn/100-turn压力测试
- **渠道覆盖**：Android Talk模式实时语音、Telegram论坛话题修复、Discord实时语音优化 — 全渠道体验持续提升
- **Mac原生应用**：设置页面全面重新设计，用户体验大幅提升

---
*报告生成时间：2026-05-19 06:10 CST | 数据来源：GitHub API + 全球技术社区*

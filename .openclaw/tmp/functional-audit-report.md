# 🔍 旺财Jarvis 功能完备性审计报告

**审计日期**: 2026-06-15
**审计范围**: ~/.openclaw/workspace 全量技能、脚本、定时任务、插件
**系统版本**: OpenClaw (Node v26.0.0, macOS Darwin 24.6.0 arm64)
**当前模型**: qwen/qwen3.7-max

---

## 📊 总览

| 维度 | 数量 | 健康率 |
|------|------|--------|
| 工作区技能 (workspace/skills/) | 68个目录 | 97% (67/68有SKILL.md) |
| 插件技能 (plugin-skills/) | 7个 | 100% |
| 内置技能 (bundled) | ~30个 | 77% (17 disabled) |
| 就绪技能 (openclaw skills list) | **96/113** | **85%** |
| 定时任务脚本 | 2个cron + 多个OpenClaw cron | ✅ 全部存在 |
| 辅助脚本 (scripts/) | 97个文件 | 部分冗余 |

---

## 一、已安装技能完整清单

### 1.1 工作区技能 (workspace/skills/) — 68个目录

#### ✅ 有可执行脚本的技能（26个，核心战力）

| # | 技能名 | 功能 | 脚本 | 版本 | 活跃度 | 评分 |
|---|--------|------|------|------|--------|------|
| 1 | bilibili-hot-monitor | B站热门视频日报 | py=4 | 1.0.21 | ⭐活跃 | 9/10 |
| 2 | duckduckgo-search | DuckDuckGo搜索 | py=1,sh=1 | - | ⭐活跃 | 8/10 |
| 3 | email-manager | QQ邮箱收发 | py=1 | - | ⭐活跃 | 8/10 |
| 4 | feishu-calendar | 飞书日历管理 | py=1 | - | ⭐活跃 | 8/10 |
| 5 | knowledge-pipline | 知识管线(超大型) | py=79,js=3 | - | ⚠️臃肿 | 6/10 |
| 6 | local-whisper | 本地语音识别 | py=1 | - | 偶尔用 | 7/10 |
| 7 | mayguard | 安全防护 | py=1 | - | ⭐活跃 | 8/10 |
| 8 | md-to-pdf-cjk | Markdown转PDF | py=1 | - | 偶尔用 | 8/10 |
| 9 | nano-banana-pro | 图片生成(Gemini) | py=1 | 1.0.1 | ⭐活跃 | 9/10 |
| 10 | obsidian-ontology-sync | Obsidian知识图谱 | py=3 | 1.0.1 | ⭐活跃 | 8/10 |
| 11 | oc-security-hardener | OpenClaw安全加固 | py=1 | - | 偶尔用 | 7/10 |
| 12 | openclaw-agent-browser | 浏览器自动化 | sh=1 | - | ⭐活跃 | 8/10 |
| 13 | proactive-agent | 主动思考/WAL协议 | sh=1 | 3.1.0 | ⭐核心 | 9/10 |
| 14 | self-improving-agent | 自我改进+反思 | sh=3,js=1 | 3.0.0 | ⭐核心 | 9/10 |
| 15 | stock-analysis | 股票深度分析 | py=7 | 6.2.0 | ⭐活跃 | 9/10 |
| 16 | stock-industry-analyzer | 股票行业分析 | py=9 | - | ⭐活跃 | 8/10 |
| 17 | stock-monitor | 股票价格监控 | py=3 | 1.3.0 | ⭐活跃 | 8/10 |
| 18 | stock-monitor-hkus | 港股美股监控 | py=1 | 1.1.0 | ⭐活跃 | 8/10 |
| 19 | tavily-search | Tavily AI搜索 | py=1,sh=1 | - | ⭐活跃 | 8/10 |
| 20 | tophot-chinese | 中文热榜聚合 | py=2 | - | ⭐活跃 | 8/10 |
| 21 | ui-ux-pro-max | UI/UX设计指导 | py=4 | 0.1.0 | 偶尔用 | 7/10 |
| 22 | video-summary | 视频摘要(B站/抖音/YT) | sh=1 | 1.6.4 | ⭐活跃 | 9/10 |
| 23 | weekly-report | 周报生成 | js=1 | - | 偶尔用 | 7/10 |
| 24 | 12306 | 火车票查询 | js=2 | - | 偶尔用 | 6/10 |
| 25 | feishu-bitable | 飞书多维表格 | js=2 | - | ⚠️薄弱 | 4/10 |
| 26 | ui-ux-pro-max-skill | UI/UX设计(旧版/Git仓库) | py=26 | - | ❌废弃 | 2/10 |

#### 📄 纯文档型技能（36个，无脚本，依赖内置工具或纯指令）

| # | 技能名 | 功能 | 文件数 | 活跃度 | 评分 |
|---|--------|------|--------|--------|------|
| 1 | ai-data-analyst-cn | AI数据分析助手 | 3 | ⭐活跃 | 7/10 |
| 2 | clawsec | 安全代理监控 | 4 | ⭐活跃 | 8/10 |
| 3 | competitor-analysis | 竞品分析 | 7 | ⭐活跃 | 8/10 |
| 4 | competitor-research | 竞品调研 | 6 | ⭐活跃 | 8/10 |
| 5 | content-brainstorm | 内容头脑风暴 | 3 | ⭐活跃 | 7/10 |
| 6 | content-writer | 内容写作 | 3 | ⭐活跃 | 7/10 |
| 7 | copywriting | 文案撰写 | 4 | ⭐活跃 | 7/10 |
| 8 | daily-report-skill | 日报生成 | 5 | ⭐活跃 | 7/10 |
| 9 | debug-checklist | 调试清单 | 4 | 偶尔用 | 6/10 |
| 10 | diagram-generator | 图表生成 | 15 | ⭐活跃 | 8/10 |
| 11 | distil | 网页内容提取 | 5 | ⚠️禁用 | 5/10 |
| 12 | evolink-music | AI音乐(Suno) | 5 | ⚠️禁用 | 5/10 |
| 13 | evolink-video | AI视频(Sora等) | 5 | ⚠️禁用 | 5/10 |
| 14 | find-skills-robin | 技能发现 | 3 | 偶尔用 | 6/10 |
| 15 | games | 游戏互动 | 3 | 偶尔用 | 5/10 |
| 16 | github | GitHub操作 | 3 | ⭐活跃 | 7/10 |
| 17 | gog | GOG游戏平台 | 3 | ❌不用 | 3/10 |
| 18 | healthcheck | 系统健康检查 | 3 | ⭐活跃 | 7/10 |
| 19 | humanizer | 文本人性化 | 5 | ⭐活跃 | 8/10 |
| 20 | market-analysis-cn | 中国市场分析 | 4 | ⭐活跃 | 7/10 |
| 21 | memory-lancedb-hybrid | 向量记忆检索 | 9 | ⭐活跃 | 8/10 |
| 22 | multi-search-engine | 多源搜索引擎(17个) | 8 | ⭐活跃 | 8/10 |
| 23 | n8n-workflow-automation | n8n工作流 | 4 | ❌不用 | 3/10 |
| 24 | nano-banana-2 | 图片生成(旧版) | 3 | ⚠️被Pro替代 | 4/10 |
| 25 | office-xyz | Office文档 | 3 | 偶尔用 | 6/10 |
| 26 | office | Office套件 | 7 | 偶尔用 | 6/10 |
| 27 | reminder | 提醒管理 | 4 | ⭐活跃 | 7/10 |
| 28 | schedule-feishu | 飞书日程 | 4 | ⭐活跃 | 7/10 |
| 29 | scrapling-skill | 网页抓取 | **1** | ⚠️不完整 | 5/10 |
| 30 | security-auditor | 安全审计 | 3 | ⭐活跃 | 8/10 |
| 31 | self-improving | 自我改进(另一版本) | 11 | ⚠️重复 | 5/10 |
| 32 | serpapi | SerpAPI搜索 | 2 | ⭐活跃 | 7/10 |
| 33 | skill-vetter | 技能安全审查 | 3 | ⭐活跃 | 7/10 |
| 34 | summarize | URL/文件摘要 | 3 | ⭐活跃 | 8/10 |
| 35 | weather | 天气查询 | 2 | ⭐活跃 | 8/10 |

#### ❌ 问题技能

| 技能 | 问题 | 建议 |
|------|------|------|
| **ui-ux-pro-max-skill** | 无根级SKILL.md，是完整Git仓库(含.claude/.github)，与 ui-ux-pro-max 重复 | 🗑️ 删除或归档 |
| **self-improving** vs **self-improving-agent** | 两个同名功能的技能，功能高度重叠 | 合并保留一个 |
| **nano-banana-2** vs **nano-banana-pro** | 旧版被新版完全替代 | 🗑️ 删除nano-banana-2 |
| **feishu-bitable** | SKILL.md仅361B，功能极简，OpenClaw已有内置bitable工具 | 考虑合并或废弃 |
| **scrapling-skill** | 仅1个文件(SKILL.md)，无任何脚本 | 补全脚本或标记为纯指令型 |

### 1.2 插件技能 (plugin-skills/) — 7个

| 技能 | 功能 | 状态 |
|------|------|------|
| feishu-doc | 飞书文档读写 | ✅ 符号链接正常 |
| feishu-drive | 飞书云盘 | ✅ 符号链接正常 |
| feishu-perm | 飞书权限 | ✅ 符号链接正常 |
| feishu-wiki | 飞书知识库 | ✅ 符号链接正常 |
| lossless-claw | 无损上下文管理 | ✅ 符号链接正常 |
| obsidian-vault-maintainer | Obsidian库维护 | ✅ 符号链接正常 |
| wiki-maintainer | Wiki维护 | ✅ 符号链接正常 |

### 1.3 内置技能 (bundled) — 关键状态

**✅ 就绪的内置技能 (13个)**:
1password, apple-reminders, blogwatcher, blucli, camsnap, canvas, clawhub, diagram-maker, eightctl, gemini, gh-issues, gifgrep, himalaya, imsg, mcporter, meme-maker, nano-pdf, node-connect, node-inspect-debugger, obsidian, openai-whisper, oracle, ordercli, peekaboo, python-debugpy, session-logs, skill-creator, songsee, sonoscli, spike, taskflow, taskflow-inbox-triage, things-mac, tmux, video-frames, wacli, weather, xurl

**❌ 禁用的内置技能 (17个)**:

| 技能 | 功能 | 禁用原因推测 | 是否需要启用 |
|------|------|-------------|-------------|
| apple-notes | Apple备忘录 | 未安装memo CLI | ⚠️ 可选 |
| bear-notes | Bear笔记 | 未安装grizzly | ❌ 不需要 |
| coding-agent | Codex编码代理 | 配置复杂 | ⚠️ 建议启用 |
| discord | Discord操作 | 无token配置 | ⚠️ 社区官需要 |
| distil | 网页内容提取 | 依赖缺失 | ⚠️ 可修复 |
| evolink-music | AI音乐 | 无API配置 | ⚠️ 可选 |
| evolink-video | AI视频 | 无API配置 | ⚠️ 可选 |
| goplaces | Google Places | 无API Key | ❌ 不需要 |
| model-usage | 模型用量统计 | 依赖CodexBar | ⚠️ 可选 |
| notion | Notion操作 | 无token | ❌ 不用Notion |
| openai-whisper-api | OpenAI语音识别 | 本地whisper已够 | ❌ 不需要 |
| sag | ElevenLabs TTS | Azure TTS已满足 | ❌ 不需要 |
| sherpa-onnx-tts | 本地TTS | Azure TTS已满足 | ❌ 不需要 |
| slack | Slack操作 | 不用Slack | ❌ 不需要 |
| spotify-player | Spotify播放 | 不用Spotify | ❌ 不需要 |
| trello | Trello看板 | 不用Trello | ❌ 不需要 |
| voice-call | 语音通话 | 无插件配置 | ❌ 不需要 |

---

## 二、功能覆盖度矩阵

| 功能领域 | 状态 | 工具/技能 | 备注 |
|----------|------|-----------|------|
| 🔍 **搜索引擎** | ✅ 完备 | SerpAPI + Tavily + DuckDuckGo + multi-search-engine(17源) | 三级搜索容灾，search.sh统一入口 |
| 📧 **邮件发送** | ✅ 完备 | email-manager + huawei_compatible_sender.py + send_*.py系列 | QQ邮箱+华为邮箱双通道 |
| 📅 **日历管理** | ✅ 完备 | feishu-calendar + schedule-feishu | 飞书日历全覆盖 |
| 📝 **飞书文档** | ✅ 完备 | feishu-doc/drive/wiki/perm(插件) + 内置feishu_doc工具 | 四位一体 |
| 📊 **多维表格** | ⚠️ 部分 | feishu-bitable(简陋) + 内置bitable工具 | 内置工具够用，技能可删 |
| 🌐 **网站管理** | ✅ 完备 | github技能 + scripts/git_push.py + scripts/push_github.py | Git推送链完整 |
| 🎨 **图片生成** | ✅ 完备 | nano-banana-pro(Gemini) + 内置image_generate | 支持编辑模式 |
| 🎵 **语音合成** | ✅ 完备 | Azure TTS(自建脚本) | ⚠️ 但禁止用内置tts工具 |
| 🎙️ **语音识别** | ✅ 完备 | local-whisper + 内置openai-whisper(bundled) | 本地+云端双通道 |
| 🎬 **视频生成** | ⚠️ 部分 | evolink-video(已禁用) + 内置video_generate | 内置工具可用，evolink无配置 |
| 📹 **视频摘要** | ✅ 完备 | video-summary(B站/抖音/YT/小红书) | 核心技能 |
| 📄 **PDF处理** | ✅ 完备 | md-to-pdf-cjk + 内置pdf工具 + nano-pdf(bundled) | 生成+分析都有 |
| 📊 **数据分析** | ✅ 完备 | ai-data-analyst-cn + stock-analysis(py=7) + stock-industry-analyzer(py=9) | 金融分析尤其强 |
| 🖥️ **浏览器自动化** | ✅ 完备 | openclaw-agent-browser + scrapling-skill | 但scrapling不完整 |
| 🔐 **密码管理** | ✅ 就绪 | 1password(bundled) | CLI已安装 |
| 💬 **Twitter/X** | ✅ 完备 | xurl(bundled, ready) | 发推/读/搜索/DM全支持 |
| 💬 **Discord** | ❌ 缺失 | discord(bundled, **disabled**) | 社区官缺工具 |
| 📈 **股票监控** | ✅ 强力 | stock-monitor + stock-monitor-hkus + stock-analysis + stock-industry-analyzer | 4个技能协同 |
| 🌤️ **天气** | ✅ 完备 | weather(workspace) + weather(bundled) | 双保险 |
| 🔒 **安全** | ✅ 强力 | clawsec + mayguard + security-auditor + oc-security-hardener + skill-vetter | 5层安全 |
| 📰 **新闻监控** | ✅ 强力 | bilibili-hot-monitor + tophot-chinese + ai_news_*.py系列 | 多源新闻 |
| 🧠 **记忆系统** | ✅ 强力 | memory-lancedb-hybrid + obsidian-ontology-sync + lossless-claw + wiki-maintainer | 向量+图谱+无损 |
| 📋 **任务管理** | ✅ 完备 | apple-reminders + things-mac + taskflow + reminder | 多系统覆盖 |
| 🎯 **主动服务** | ✅ 核心 | proactive-agent + self-improving-agent | WAL协议+自我进化 |
| 📑 **Office文档** | ⚠️ 冗余 | office + office-xyz + pptx(managed) + python-ppt-generator | 4个PPT/Office相关，可能重叠 |
| 🎮 **游戏** | ⚠️ 低优 | games | 偶尔用 |
| 🚂 **火车票** | ⚠️ 低优 | 12306 | 偶尔用 |

---

## 三、多Agent团队能力匹配

### AGENTS.md 定义的团队成员 vs 实际技能覆盖

| Agent | 角色 | 需要的能力 | 实际技能覆盖 | 缺口 |
|-------|------|-----------|-------------|------|
| **creator (笔杆子)** | 内容创作 | 写作、排版、图片 | content-writer ✅, copywriting ✅, diagram-generator ✅, nano-banana-pro ✅, humanizer ✅ | **无缺口** |
| **yunying (运营官)** | 日常运营 | 邮件、日程、追踪 | email-manager ✅, feishu-calendar ✅, schedule-feishu ✅, reminder ✅ | **无缺口** |
| **canmou (参谋)** | 深度研究 | 竞品、调研 | competitor-analysis ✅, competitor-research ✅, market-analysis-cn ✅, multi-search-engine ✅ | **无缺口** |
| **jinhua (进化官)** | 代码开发 | 编码、优化 | self-improving-agent ✅, coding-agent ❌(disabled) | ⚠️ coding-agent未启用 |
| **jiaoyi (交易官)** | 股票监控 | 股票分析、市场 | stock-analysis ✅, stock-monitor ✅, stock-monitor-hkus ✅, stock-industry-analyzer ✅ | **无缺口** |
| **shequ (社区官)** | 社区运营 | Twitter、Discord | xurl ✅, discord ❌(**disabled**) | ❌ Discord缺失 |
| **ascend_ai_officer** | 昇腾专家 | 算子、模型迁移 | 无专门技能 | ⚠️ 依赖通用能力 |
| **ppt_generator** | PPT生成 | 自动PPT | pptx(managed) ✅, python-ppt-generator(managed) ✅ | **无缺口** |
| **image_generator** | 图片处理 | 生成、优化、识别 | nano-banana-pro ✅, 内置image_generate ✅, image工具 ✅ | **无缺口** |

---

## 四、定时任务健康检查

### 4.1 系统Cron任务

| 任务 | 时间 | 脚本 | 存在 | 可执行 |
|------|------|------|------|--------|
| 每日祝福 | 07:40 | scripts/daily_blessing.sh | ✅ | ✅ |
| 技能更新 | 18:00 | scripts/cron_update_skills.sh | ✅ | ✅ |

### 4.2 OpenClaw管理的Cron任务 (MEMORY.md记录)

| 任务 | 时间 | 关键脚本 | 存在 |
|------|------|---------|------|
| OpenClaw每日新闻监控 | 06:00 | ai_news_daily.py / ai_news_search.py | ✅ |
| 高校分队-AI新闻简报 | 06:15 | send_daily_ai_news_*.py系列 | ✅ |
| 健康长寿科研监控 | 07:00 | health_longevity_monitor.sh | ✅ |
| 主动惊喜检查 | 每4h | proactive-agent | ✅ |
| AI新闻日报更新 | 08:00 | update_ai_news.py | ✅ |

### 4.3 scripts/目录健康度

- **总文件数**: 97个
- **问题**: 
  - 大量test_*.py测试文件残留（8个）
  - 多个send_*.py邮件发送脚本版本冗余（5+个）
  - install_day*.sh安装脚本已完成使命，可归档
  - fix_*.py一次性修复脚本可清理

---

## 五、系统配置警告

从 `openclaw skills list` 输出中发现：

1. **⚠️ 插件冲突**: `lossless-claw` 检测到重复插件ID（global plugin被另一个global plugin覆盖）
2. **⚠️ SQLite状态冲突**: codex, feishu, lossless-claw, openclaw-weixin 的安装元数据冲突
3. **⚠️ 状态目录迁移跳过**: 目标目录已存在，需手动合并
4. **⚠️ Memory Core短期记忆导入跳过**: SQLite行已存在

---

## 六、推荐改进方案

### 🔴 高优先级（立即执行）

| # | 改进项 | 原因 | 操作 |
|---|--------|------|------|
| 1 | **删除 ui-ux-pro-max-skill** | 废弃Git仓库，与ui-ux-pro-max重复，占用512B目录 | `rm -rf skills/ui-ux-pro-max-skill` |
| 2 | **删除 nano-banana-2** | 被nano-banana-pro完全替代 | `rm -rf skills/nano-banana-2` |
| 3 | **合并 self-improving 系列** | self-improving + self-improving-agent + self-improvement 三个高度重叠 | 保留self-improving-agent，删其余 |
| 4 | **启用 discord 技能** | 社区官(shequ)缺Discord工具 | 配置Discord token后启用 |
| 5 | **修复 lossless-claw 插件冲突** | 重复插件ID影响稳定性 | 清理重复安装记录 |

### 🟡 中优先级（本周完成）

| # | 改进项 | 原因 | 操作 |
|---|--------|------|------|
| 6 | **清理 scrapling-skill** | 仅1个SKILL.md，无实际脚本 | 补全或标记为纯指令型 |
| 7 | **删除 feishu-bitable 技能** | 内置bitable工具完全够用 | `rm -rf skills/feishu-bitable` |
| 8 | **归档 scripts/ 冗余文件** | 97个文件中大量一次性脚本 | 建scripts/archive/归档 |
| 9 | **启用 coding-agent** | 进化官(jinhua)需要编码代理 | 配置Codex后启用 |
| 10 | **精简 office 技能** | office + office-xyz 可能重叠 | 评估合并 |

### 🟢 低优先级（可选）

| # | 改进项 | 原因 | 操作 |
|---|--------|------|------|
| 11 | 评估 gog 技能必要性 | GOG游戏平台技能，与核心业务无关 | 考虑删除 |
| 12 | 评估 n8n-workflow-automation | 未使用n8n | 考虑删除 |
| 13 | 评估 12306 技能 | 偶尔用，但维护成本低 | 保留 |
| 14 | 评估 evolink-music/video | 已禁用，内置工具可替代 | 考虑删除 |

### 📦 推荐安装的ClawHub技能

基于 `clawhub search` 结果，按优先级排序：

| # | 技能名 | 功能 | 推荐理由 |
|---|--------|------|----------|
| 1 | **monitor** (score=3.69) | 通用监控 | 可增强系统监控能力 |
| 2 | **notification** (score=3.64) | 通知管理 | 统一通知渠道 |
| 3 | **office-automation-pro** (score=3.02) | Office自动化 | 可能比现有office技能更强 |
| 4 | **domain-monitor** (score=2.95) | 域名监控 | 网站运维有用 |
| 5 | **system-resource-monitor** (score=2.96) | 系统资源监控 | Mac mini资源监控 |
| 6 | **ping-monitor** (score=2.97) | Ping监控 | 网络健康检查 |
| 7 | **auto-monitor-zhouli** (score=3.00) | 自动监控 | 自动化监控方案 |

> ⚠️ 注意：ClawHub技能需通过 skill-vetter 安全审查后再安装。

---

## 七、总结与建议

### 系统健康度评分: **82/100** ✅

**强项:**
- 🔍 搜索能力极其丰富（3+引擎，17源聚合）
- 📈 股票/金融分析能力非常强（4个专项技能）
- 🔒 安全防护层层叠加（5个安全技能）
- 🧠 记忆系统先进（向量+图谱+无损上下文）
- 📰 新闻监控自动化程度高
- 🎯 主动服务能力（WAL协议+自我进化）

**弱项:**
- 💬 社交媒体覆盖不全（Twitter✅ Discord❌）
- 🧹 技能冗余严重（68个工作区技能中有~10个可清理）
- 📁 scripts/目录缺乏整理（97个文件，大量一次性脚本）
- ⚙️ 17个内置技能处于disabled状态（多数是不需要的，但coding-agent和discord值得启用）
- ⚠️ 系统有插件冲突和SQLite状态不一致问题

**一句话总结**: 旺财Jarvis核心功能非常强大，搜索/金融/安全/记忆/自动化都处于高水准。主要改进方向是**清理冗余**（约10个废弃技能+大量一次性脚本）和**补齐Discord社区能力**。

---

*报告生成: 2026-06-15 | 审计员: 功能完备性审计子Agent*

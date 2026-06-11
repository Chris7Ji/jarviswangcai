## 记忆管理原则

- 配置变更后 → 保存到 `memory/YYYY-MM-DD.md`
- 重要决策 → 记录结论和原因
- 发现主人偏好 → 记录到 `USER.md`

## 核心配置（重要）

### TTS（必须Azure TTS，2026-03-22永久保存，2026-03-23修正）
- API Key: `7eDraYD542t0TLbtmJHYGVzvOEp3rx57IWKv7YDikrUSwnzDaBt4JQQJ99CBAC3pKaRXJ3w3AAAYACOGc788`
- 端点: https://eastasia.tts.speech.microsoft.com/cognitiveservices/v1
- 音色: zh-CN-XiaoyiNeural
- 格式: audio-16khz-32kbitrate-mono-mp3
- 区域: East Asia
- ⚠️ 禁止使用OpenClaw内置tts工具，只用Azure TTS API
- ⚠️ SSML中禁止使用prosody rate="+30%"标签（会导致HTTP 400）
- 正确SSML格式：直接放文本，不加prosody标签

### 邮件授权码（全局）
- QQ邮箱: icxhfzuyzbhbbjie

### Tavily API（全局）
- API Key: tvly-dev…7MV5

## 模型配置
- 默认模型: deepseek/deepseek-v4-flash
- 备用: deepseek/deepseek-chat
- 已删除: minimax-portal/MiniMax-M2.7-highspeed（2026-05-30移除）

## 图片生成配置 (2026-03-21更新)
| 用途 | 方案 | 状态 |
|------|------|------|
| **图片生成（主力）** | Nano Banana Pro (Gemini API) + 本地脚本 | ✅ 已配置 |
| **API Key** | `AIzaSyB…uBCU（完整Key存于 openclaw.json）` | ✅ 已更新 (2026-05-30) |
| **脚本路径** | `~/.openclaw/workspace/skills/nano-banana-pro/scripts/generate_image.py` | ✅ |
| **安装命令** | `clawhub install nano-banana-pro --workdir ~/.openclaw/workspace` | ✅ |
| **默认分辨率** | 2K | ✅ |

### 图片生成优化官（image_generator）默认模型
- **默认模型**: Nano Banana Pro（Gemini 3.1 Flash Image Preview）
- **命令模板**: `uv run ~/.openclaw/workspace/skills/nano-banana-pro/scripts/generate_image.py --prompt "..." --filename "xxx.png" --resolution 2K --api-key "AIzaSyB…uBCU（完整Key存于 openclaw.json）"`
- **编辑模式**: 添加 `--input-image "原图路径"`

## 搜索与翻译配置（2026-03-20锁定）
| 用途 | 方案 | 状态 |
|------|------|------|
| **搜索（主力）** | SerpAPI: `b28c24…360f` | ✅ |
| **搜索（备用）** | Tavily API: `tvly-dev…7MV5` | ✅ |
| **搜索（最后备选）** | DuckDuckGo（无需Key） | ✅ |
| **翻译** | DeepSeek-Chat: `sk-451…8356（已失效）` (OpenClaw配置) | ✅ |
| **邮件格式** | 华为邮箱兼容版（无emoji、简化HTML） | ✅ |

### 搜索优先级
1. SerpAPI（主力）
2. Tavily（备用）
3. DuckDuckGo（最后备选）

### 翻译配置
- 统一使用当前默认大模型（deepseek/deepseek-v4-flash）翻译英文→中文
- 不再使用三级容灾机制

## 定时任务
| 任务 | 时间 | 状态 |
|------|------|------|
| 主动惊喜检查 | 每4小时 | ok (2026-03-20新增) |
| OpenClaw每日新闻监控 | 06:00 | ok |
| 高校分队-AI新闻每日简报 | 06:15 | ok |
| 健康长寿科研成果监控 | 07:00 | ok |

### 主动惊喜检查 Cron (2026-03-20新增)
- ID: 66c5d54b-8bec-4d79-9e8c-a21c275715c7
- 功能：扫描 proactive-tracker、recurring-patterns、outcome-journal、Skill更新、WAL检查
- 触发词：每4小时自动执行

## 已安装技能 (2026-03-20更新)
| 技能 | 用途 | 状态 |
|------|------|------|
| scrapling-skill | 网页抓取、动态渲染、Cloudflare绕过 | ✅ 新安装 |
| proactive-agent | 主动思考、WAL协议、记忆维护 | ✅ 已有 |

### 高校分队-AI新闻每日简报 收件人（2026-03-19更新）
| 序号 | 邮箱 |
|------|------|
| 1 | liuwei44259@huawei.com |
| 2 | tiankunyang@huawei.com |
| 3 | qinhongyi2@huawei.com |
| 4 | jiawei18@huawei.com |
| 5 | jiyingguo@huawei.com |
| 6 | linfeng67@huawei.com |
| 7 | lvluling1@huawei.com |
| 8 | suqi1@huawei.com |
| 9 | susha@huawei.com |
| 10 | wangdongxiao@huawei.com |
| 11 | xiongguifang@huawei.com |
| 12 | xushengsheng@huawei.com |
| 13 | zhangqianfeng2@huawei.com |
| 14 | zhangyexing2@huawei.com |
| 15 | 86940135@qq.com |

## 飞书消息发送（2026-03-25）
- **优先使用**：OpenClaw message 工具（如果 bug 修复则用这个）
- **备用方案**：curl 直接调用飞书 API
  - 获取 Token：`POST https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal`
  - 发图片：先 `POST /im/v1/images` 上传获取 image_key，再发消息
  - API 文档：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/create

## 已修复问题（2026-06-10）
- DeepSeek API Key 不一致导致 cron 任务连续失败：`auth-profiles.json` 中 Key 正确（`sk-c347…（隐去）...b10`），但 `catalog.json` 缓存了旧 Key（`sk-451...8356`，已失效），隔离 cron 会话初始化时读 catalog 旧 Key。
- 修复：更新 `~/.openclaw/agents/main/agent/plugins/deepseek/catalog.json` 中的 apiKey + `openclaw secrets reload`
- ✅ 手动触发验证：日记验证任务已成功运行

## 待处理问题
- 华为邮箱收件偶尔被拦截（QQ→Huawei）
- 自建网站统计方案已记录: `memory/archive/2026-03-29-自建Analytics方案.md`

## GitHub提交方式（2026-03-30）
- **默认使用Git命令**提交GitHub，而不是网页操作
- 网站目录：`/Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai`
- 常用命令：
  - `git -C /Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai status`
  - `git -C /Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai add .`
  - `git -C /Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai commit -m "描述"`
  - `git -C /Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai push`
- exec allowlist 已添加网站目录的git命令

## 记忆管理规范
- **图谱链接规范**: 写入核心日志时，主动使用 `[[WikiLink]]` 打标（如 `[[Gemini]]`、`[[报错_ETIMEDOUT]]`）以在图谱中自动关联
- **Cron任务规则**: 绝不使用 `--model` 硬编码绑定模型；核心任务追加 `--failure-alert --failure-alert-after 1`

## Compaction配置 (2026-04-16已生效)
- contextThreshold: 0.75 (原0.5→提升)
- freshTailCount: 32 (原12→提升)
- incrementalMaxDepth: 1 (原无限→限制)
- compaction.notifyUser: true
- contextPruning: cache-ttl 5m
- 参考: https://docs.openclaw.ai/concepts/compaction

## Memory-Search配置 (2026-04-16已生效)
- Provider: gemini / gemini-embedding-2-preview / 1536d
- temporalDecay: enabled (30天半衰期)
- MMR: enabled (减少重复)
- memory-lancedb-pro: ❌ 放弃（插件无法被发现），继续用内置memorySearch
- memory-wiki: bridge mode → ~/.openclaw/wiki/main
- CJK检索问题: `openclaw memory index --force`

## Wiki配置
- vault: ~/.openclaw/wiki/main (bridge mode)
- render: obsidian (CLI未安装)
- 结构: entities/ concepts/ sources/ syntheses/ reports/

## Codex集成
- Codex plugin: ✅ 已连接 (gpt-5.4 / gpt-5.4-mini / gpt-5.3-codex 等)
- 使用: `/model codex` 切换, `/codex status` 查看状态

## Promoted From Short-Term Memory (2026-06-02)

<!-- openclaw-memory-promotion:memory:memory/2026-05-29.md:20:20 -->
- 老板指令：三个故障翻译删除，统一翻译替换使用当前默认大模型 [score=0.858 recalls=0 avg=0.620 source=memory/2026-05-29.md:20-20]

## Promoted From Short-Term Memory (2026-06-06)

<!-- openclaw-memory-promotion:memory:memory/2026-05-29.md:40:41 -->
- 发现重复文件（需关注）: `MEMORY_backup_2026-03-10.md` 和 `MEMORY_backup_2026-03-11.md` 同时存在于 workspace 根目录和 `memory/archive/` 中，内容完全一致; 暂未处理，待老板确认后再删除 [score=0.923 recalls=0 avg=0.620 source=memory/2026-05-29.md:40-41]
<!-- openclaw-memory-promotion:memory:memory/2026-05-29.md:6:8 -->
- 变更内容: **AGENTS.md**: 第二核心原则由「翻译模型三级容灾机制」改为「翻译统一使用默认大模型」; **USER.md**: Context中模型使用偏好由三级降级改为统一使用默认大模型; **MEMORY.md**: 翻译配置由DeepSeek-Chat改为统一使用默认大模型（deepseek/deepseek-v4-flash） [score=0.923 recalls=0 avg=0.620 source=memory/2026-05-29.md:6-8]
<!-- openclaw-memory-promotion:memory:memory/2026-05-30.md:12:15 -->
- Minimax 大模型配置已删除: 删除原因: 老板要求; 涉及: minimax-portal, minimax-cn provider, auth profiles, plugins, agent fallbacks; imageModel.primary → 改为 google/gemini-3.1-flash-lite; minimax 模型引用从 creator 和 canmou 的 fallbacks 中移除 [score=0.906 recalls=0 avg=0.620 source=memory/2026-05-30.md:12-15]
<!-- openclaw-memory-promotion:memory:memory/2026-05-30.md:4:5 -->
- Gemini API Key 更新: 旧 Key（已泄露）: `AIzaSyD…pN9s（已废弃）`; 新 Key: `AIzaSyB…uBCU（完整Key存于 openclaw.json）` [score=0.906 recalls=0 avg=0.620 source=memory/2026-05-30.md:4-5]
<!-- openclaw-memory-promotion:memory:memory/2026-05-30.md:7:9 -->
- Gemini API Key 更新: [x] openclaw.json → models.providers.google.apiKey; [x] MEMORY.md （图片生成配置 + 命令模板）; [x] Gateway 已重启生效 [score=0.906 recalls=0 avg=0.620 source=memory/2026-05-30.md:7-9]
<!-- openclaw-memory-promotion:memory:memory/2026-05-29.md:11:13 -->
- 旧方案（已删除）: google/gemini-3.1-flash-lite-preview（优先）; minimax-portal/MiniMax-M2.7-highspeed（降级）; deepseek-chat（兜底） [score=0.899 recalls=0 avg=0.620 source=memory/2026-05-29.md:11-13]
<!-- openclaw-memory-promotion:memory:memory/2026-05-29.md:16:17 -->
- 新方案: 任何英文翻译任务统一使用当前运行的默认大模型进行翻译; 当前默认模型: deepseek/deepseek-v4-flash [score=0.899 recalls=0 avg=0.620 source=memory/2026-05-29.md:16-17]
<!-- openclaw-memory-promotion:memory:memory/2026-05-29.md:25:28 -->
- 归档脚本逻辑检查: 检查 `memory/` 下所有 `.md` 文件; 30天阈值：2026-04-29 之前; **内存根目录文件年龄**:; `2026-05-04.md` → 25天 ✅ 未到期 [score=0.899 recalls=0 avg=0.620 source=memory/2026-05-29.md:25-28]
<!-- openclaw-memory-promotion:memory:memory/2026-05-29.md:29:32 -->
- 归档脚本逻辑检查: `2026-05-29.md` → 0天 ✅; `MEMORY_SYSTEM_BUILD_GUIDE.md` → 5天 ✅; `domain-jarviswangcai-top.md` → 0天 ✅; `user_preferences.md` → 14天 ✅ [score=0.899 recalls=0 avg=0.620 source=memory/2026-05-29.md:29-32]
<!-- openclaw-memory-promotion:memory:memory/2026-05-29.md:33:33 -->
- 归档脚本逻辑检查: **结论**: 无文件需自动归档 [score=0.899 recalls=0 avg=0.620 source=memory/2026-05-29.md:33-33]

## Promoted From Short-Term Memory (2026-06-07)

<!-- openclaw-memory-promotion:memory:memory/2026-05-30.md:18:19 -->
- 定风波图片生成: 使用 xAI/grok-imagine-image 成功生成中国风图片; OpenAI GPT-Image-2 因 Codex 限制不可用 [score=0.891 recalls=0 avg=0.620 source=memory/2026-05-30.md:18-19]
<!-- openclaw-memory-promotion:memory:memory/2026-05-29.md:36:37 -->
- 碎片清理: **发现** `working-buffer.md`（39天前，2026-03-19会话工作缓冲）存在于workspace根目录; **处理**：已归档至 `memory/archive/working-buffer_2026-03-19.md`，删除原始文件 [score=0.890 recalls=0 avg=0.620 source=memory/2026-05-29.md:36-37]
<!-- openclaw-memory-promotion:memory:memory/2026-05-29.md:44:45 -->
- 归档目录现状: `archive/` 中共 58 个文件：2月3个，3月32个，4月16个，5月3个（含刚归档的working-buffer）; 本体论知识图谱: 412KB（ontology/下graph.jsonl + knowledge_graph.json） [score=0.890 recalls=0 avg=0.620 source=memory/2026-05-29.md:44-45]

# 学习记录
# 注意: 详细记录已分类存储到by-topic/目录
# 本文件仅保留最新5条记录和索引

## 最新学习记录（最近5条）

## 2026-04-02 23:30:00
**ID**: learn-015
**优先级**: MEDIUM
**类别**: knowledge_graph
**摘要**: [[私有知识星图自动构建]] 揭示连接密度提升
**场景**: 定时任务自动构建知识图谱
**经验**: 本次构建提取了 445 个节点和 188 个连接。节点数量小幅增长（+14），但连接数量大幅增加（+44），表明 [[Obsidian 知识库]] 中 [[概念关联]] 正在深化。这反映了 [[知识网络]] 的成熟度提升，也验证了星图构建脚本能够有效捕捉 [[关系密度]] 的变化，为 [[知识发现]] 提供了更丰富的拓扑结构。
**状态**: ✅ 已验证并记录

## 2026-04-02 00:18:00
**ID**: learn-014
**优先级**: HIGH
**类别**: knowledge_graph
**摘要**: [[私有知识星图自动构建]] 捕获大规模节点增长
**场景**: 定时任务自动构建知识图谱
**经验**: 本次构建提取了 431 个节点和 144 个连接。从前一日的 336 个节点大幅跃升，表明 [[Obsidian 知识库]] 发生了集中输入或批量更新。这也验证了星图构建脚本对于大规模新增数据依然保持着稳定高效的解析能力，确保证了 [[本体图谱]] 对突发知识流的兼容。
**状态**: ✅ 已验证并记录

## 2026-04-01 00:14:00
**ID**: learn-013
**优先级**: MEDIUM
**类别**: knowledge_graph
**摘要**: 持续验证 [[私有知识星图自动构建]] 脚本的增量更新能力
**场景**: 定时任务自动构建知识图谱
**经验**: 脚本 `build_star_graph.py` 的定期执行有效捕获了新增内容，节点从332个增加至336个，连接从107个增加至115个。这证明了其作为 [[本体图谱]] 动态更新引擎的可靠性，进一步充实了 [[知识检索]] 的数据库。
**状态**: ✅ 已验证并记录

## 2026-03-31 23:30:00
**ID**: learn-012
**优先级**: MEDIUM
**类别**: knowledge_graph
**摘要**: 成功运行 [[私有知识星图自动构建]] 脚本
**场景**: 定时任务自动构建知识图谱
**经验**: 脚本 `build_star_graph.py` 可自动解析笔记生成 [[本体图谱]]，本次成功提取 332 个节点和 107 个连接，为后续的 [[知识检索]] 和 [[AI分析]] 提供了结构化数据基础。
**状态**: ✅ 已验证并记录

## 2026-03-23 23:19:00
**ID**: learn-011
**优先级**: CRITICAL
**类别**: azure_tts
**摘要**: Azure TTS 正确用法 - 禁止使用 prosody rate 标签
**场景**: 老板测试 Azure TTS，发现 HTTP 400 错误
**错误原因**: SSML 中使用 `<prosody rate="+30%">` 标签，eastasia 区域不支持此参数
**正确做法**:
1. 不使用 prosody 标签，直接放文本内容
2. 端点: https://eastasia.tts.speech.microsoft.com/cognitiveservices/v1
3. 音色: zh-CN-XiaoyiNeural
4. 格式: audio-16khz-32kbitrate-mono-mp3
**正确 SSML 模板**:
```xml
<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='zh-CN'>
    <voice name='zh-CN-XiaoyiNeural'>
        要转换的文本内容
    </voice>
</speak>
```
**状态**: ✅ 已验证并记录

## 2026-03-10 23:24:00
**ID**: learn-010
**优先级**: CRITICAL
**类别**: system_optimization
**摘要**: 优化记忆检索效率，解决响应慢问题
**场景**: 老板反馈响应有点慢，要求优化记忆系统
**优化措施**:
1. 创建关键词索引 INDEX.md - 快速定位信息
2. 分类存储学习记录 by-topic/*.md - 减少单文件大小
3. 建立快速响应策略 - 避免慢速操作
4. 预加载核心文件 - 减少读取延迟
**相关文件**:
- INDEX.md - 关键词索引
- by-topic/email.md - 邮件相关
- by-topic/model-config.md - 模型配置
- by-topic/skills.md - 技能安装
- by-topic/cron.md - 定时任务
- PERFORMANCE.md - 性能优化配置
**状态**: ✅ 已实施

## 2026-03-10 23:18:00
**ID**: learn-002
**优先级**: CRITICAL
**类别**: identity
**摘要**: 明确与老板（季）的关系和工作原则
**详情**: 见SOUL.md#L28-35
**状态**: ✅ 已记录

## 2026-03-10 14:00:00
**ID**: learn-001
**优先级**: MEDIUM
**类别**: best_practice
**摘要**: OpenClaw gateway restart 命令不需要sudo权限
**详情**: 见by-topic/cron.md
**状态**: ✅ 已验证

---

## 📚 完整学习记录索引

按主题分类存储:
- **邮件相关**: by-topic/email.md
- **模型配置**: by-topic/model-config.md
- **技能安装**: by-topic/skills.md
- **定时任务**: by-topic/cron.md

## 🔍 快速查找指南

1. **找关键词** → 查 INDEX.md
2. **找邮件配置** → 读 by-topic/email.md
3. **找模型信息** → 读 by-topic/model-config.md
4. **找技能信息** → 读 by-topic/skills.md
5. **找定时任务** → 读 by-topic/cron.md
6. **找性能优化** → 读 PERFORMANCE.md

---
**维护说明**: 本文件只保留最近5条记录，旧记录自动归档到by-topic/或archive/2026-03-31: cron任务务必不绑定模型，如果绑定特定模型会在模型更替或限流时导致后台定时任务失效挂起。建议解绑系统级cron的模型限制并增加重试与环境检查机制。


## 2026-04-01 21:00:00
**ID**: learn-020
**优先级**: CRITICAL
**类别**: system_reliability
**摘要**: 自动化Cron任务中的外部网络访问必须显式接管网络异常
**场景**: Cron日记生成任务中调用 Git push，因网络原因遇到 Connection reset by peer / Broken pipe 直接失败导致流程挂起
**错误原因**: 没有捕获或容忍基础网络工具的网络超时与断连，导致数据虽已提交但未推送成功。
**正确做法**:
1. 对于执行 `git push` 等依赖外部网络的指令，必须设计自动重试或错误吞没（挂起续传）机制。
2. 背景执行Git操作前，先通过 `git config` 注入全局身份参数。
**状态**: ✅ 已记录并更新


## 2026-04-02 21:00:00
**ID**: learn-021
**优先级**: HIGH
**类别**: system_reliability
**摘要**: Git推送网络异常诊断与心跳检查系统优化
**场景**: 夜间Git推送因Surfshark.dmg大文件触发Git LFS限制，随后HTTP2 framing layer和Connection reset by peer网络异常导致推送失败
**解决方案**:
1. 大文件处理：git reset HEAD~1 --soft + git rm --cached + .gitignore
2. 网络协议优化：git config http.version HTTP/1.1 + http.postBuffer 524288000
3. 心跳检查增强：Python脚本workaround更新PROGRESS.md
**状态**: ✅ 已记录并实施

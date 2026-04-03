# HEARTBEAT.md - 心跳监控
# Proactive Agent v3.1.0

## 心跳状态
- **状态**: 🔧 修复中（Google模型位置错误，已切换到MiniMax模型）
- **最后检查**: 2026-04-03 08:02

## 系统恢复记录
- **离线时间**: 2026-03-27 16:02 → 2026-03-28 08:57 (约17小时)
- **恢复时间**: 2026-03-28 08:57
- **任务延迟**: 新闻任务延迟到11:20-13:05执行（比正常晚5-6小时）

## Cron任务监控 ✅
| 任务 | ID | 状态 | 上次运行 | 下次运行 |
|------|-----|------|----------|----------|
| 主动惊喜检查 | 66c5d54b | ✅ OK | 04:02 (3日) | 08:02 |
| OpenClaw新闻 | 5aa186d0 | ✅ OK | 06:00 (2日) | 今天06:00 |
| 高校AI新闻 | 06c90fe1 | ✅ OK | 06:15 (2日) | 今天06:15 |
| 健康长寿 | 6502ba52 | ✅ OK | 07:00 (2日) | 今天07:00 |
| 每日祝福 | 2503fac6 | ✅ OK | 07:45 (2日) | 今天07:45 |
| 每日工作日记 | 441ffa7e | ✅ OK | 21:00 (2日) | 今天21:00 |
| **AI新闻日报更新** | **777908f9** | **❌ 超时** | **22:15 (2日)** | **今天22:00** |
| 自动记忆归档 | 3ac20321 | ✅ OK | 23:00 (2日) | 今天23:00 |
| 私有知识星图 | 18f3713c | ✅ OK | 23:30 (2日) | 今天23:30 |

## 收件人列表（高校分队）
liuwei44259@huawei.com, tiankunyang@huawei.com, qinhongyi2@huawei.com, jiawei18@huawei.com, jiyingguo@huawei.com, linfeng67@huawei.com, lvluling1@huawei.com, suqi1@huawei.com, susha@huawei.com, wangdongxiao@huawei.com, xiongguifang@huawei.com, xushengsheng@huawei.com, zhangqianfeng2@huawei.com, zhangyexing2@huawei.com, 86940135@qq.com

## 系统事件记录
- 🔧 2026-04-03 08:02: 发现google/gemini-3.1-pro-preview位置错误，导致3个早晨任务全部失败。已切换所有cron任务到minimax-portal/MiniMax-M2.7-highspeed模型。
- ⚠️ 2026-04-03 04:02: AI新闻日报更新-22:00执行超时（lastDurationMs: 1037027 > 900s），consecutiveErrors=1，下次22:00自动重试。
- ✅ 2026-04-02 20:02: 主动惊喜检查成功完成（lastRunStatus: ok, consecutiveErrors: 0），主动惊喜检查超时问题已恢复。
- ⚠️ 2026-04-02 12:10: 主动惊喜检查执行超时（consecutiveErrors=1），核心定时任务全部正常。
- ✅ 2026-04-02 08:02: 早间瀑布流（新闻与祝福任务）全部零失误通过。
- ✅ 2026-04-02 00:02: LiveSessionModelSwitchError危机爆发后于00:09~00:18奇迹般自动重试恢复。
- ✅ 2026-03-29 08:02: 系统完全恢复，4个任务全部成功执行
- ✅ 2026-03-28 11:20-13:05: 新闻任务延迟执行但全部成功

---
*每4小时由主动惊喜检查自动更新*
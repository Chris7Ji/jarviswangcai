# HEARTBEAT.md - 心跳监控
# Proactive Agent v3.1.0

## 心跳状态
- **状态**: ✅ 系统运行中
- **最后检查**: 2026-06-15 10:25 (北京时间)
- **WAL状态**: ✅ 正常

## 系统恢复记录
- **离线时间**: 2026-03-27 16:02 → 2026-03-28 08:57 (约17小时)
- **模型切换**: 2026-04-03 08:05 (google/gemini-3.1-pro-preview → minimax-portal/MiniMax-M2.7-highspeed)
- **安全修复**: 2026-04-06 23:06 (飞书allowFrom移除*通配符，.gitignore更新)

## Cron任务监控 ✅
| 任务 | ID | 状态 | 上次运行 | consecutiveErrors |
|------|-----|------|----------|------------------|
| 主动惊喜检查 | 66c5d54b | 🟢 运行中 | 06-15 10:25 | 3 (超时) |
| macOS daily_blessing | 系统crontab | ✅ | 07:40 daily | 0 |
| macOS cron_update_skills | 系统crontab | ✅ | 18:00 daily | 0 |

> 注：OpenClaw cron已精简至仅剩主动惊喜检查任务（周一/三/五10:00）。之前的所有新闻任务（OpenClaw新闻、高校AI新闻、健康长寿、AI新闻日报等）均已从OpenClaw cron中移除。

## 新闻产出状态 (2026-06-15)
| 品类 | 最新 | 状态 |
|------|------|------|
| raw_news (原始新闻采集) | 2026-06-15 08:02 | ✅ 今日已采集 |
| gaoxiao_news (高校AI新闻) | 2026-06-10 | ⚠️ 5天中断 |
| openclaw_news (高质量新闻) | 2026-06-02 | ⚠️ 13天中断 |
| opc_daily (OPC日报) | 2026-06-11 | ⚠️ 4天中断 |
| health_longevity (健康长寿) | 2026-03-20 | 🔴 87天停摆 |

## 收件人列表（高校分队）
liuwei44259@huawei.com, tiankunyang@huawei.com, qinhongyi2@huawei.com, jiawei18@huawei.com, jiyingguo@huawei.com, linfeng67@huawei.com, lvluling1@huawei.com, suqi1@huawei.com, susha@huawei.com, wangdongxiao@huawei.com, xiongguifang@huawei.com, xushengsheng@huawei.com, zhangqianfeng2@huawei.com, zhangyexing2@huawei.com, 86940135@qq.com

## 技能状态
- workspace/skills/: 61个
- 系统skills: 57个
- 无新技能需安装

## 主动惊喜检查自身问题
- ⚠️ 超时问题: consecutiveErrors=3（timeoutSeconds=300过短）
- 建议: 增大timeoutSeconds至600s

---
*每4小时由主动惊喜检查自动更新*
*最后更新: 2026-06-15 10:25*

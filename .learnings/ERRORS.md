# Errors & Lessons Learned

## 2026-06-15: 系统全面体检 - 多项关键错误修复

### 错误1: diary.js 语法错误导致网站日记页面空白
- **时间**: 2026-06-15 22:30
- **现象**: www.jarviswangcai.top/diary.html 打开后页面空白
- **根因**: `js/diary.js` 第195-196行有重复的 `{id: '20260610'}` 代码，导致 JavaScript SyntaxError: Unexpected token '{'
- **影响**: 整个 allPosts 数组无法加载，80篇日记全部不显示
- **修复**: 删除重复的2行代码
- **预防措施**:
  1. ⚠️ **修改 JS 文件后必须运行 `node --check filename.js` 验证语法**
  2. ⚠️ **修改后必须 curl 线上版本验证部署成功**
  3. ⚠️ **写入 allPosts 数组时，检查是否有重复的 id 或重复的对象开头 `{`**
- **状态**: ✅ 已修复并推送

### 错误2: 5个 cron 定时任务连续超时失败
- **时间**: 2026-06-15 18:54 发现
- **现象**: 日记生成(4次)、新闻监控(14次)、记忆归档(9次)、健康长寿(11次)、主动惊喜(4次) 全部超时
- **根因**: 默认模型从 deepseek-v4-flash 切换到 qwen3.7-max 后，隔离 session 推理太重，120s 内无法完成
- **数据**: deepseek-v4-flash 成功耗时 48-130s；qwen3.7-max 成功耗时 102-136s 或直接超时
- **修复**:
  1. 所有5个任务指定 `model: deepseek-v4-flash`
  2. 超时从 120s 提升到 300s
  3. 添加 fallback 链: deepseek → gemini-flash-lite → qwen-max
  4. 精简指令，去掉不必要的步骤
- **预防措施**:
  1. ⚠️ **切换默认模型后，必须检查所有 cron 任务是否受影响**
  2. ⚠️ **cron 任务应显式指定 model，不依赖默认模型**
  3. ⚠️ **修改后手动触发一次验证，观察实际耗时**
- **状态**: ✅ 已修复，日记任务21:00首次运行成功（54s）

### 错误3: lossless-claw 插件重复安装
- **时间**: 2026-06-15 19:16 发现
- **现象**: `openclaw skills check` 报 duplicate plugin id 警告
- **根因**: lossless-claw 同时存在于 `extensions/lossless-claw/` 和 `npm/node_modules/@martian-engineering/lossless-claw/` 两个位置
- **修复**: 删除 extensions/ 下的旧副本，保留 npm/projects/ 下的最新版
- **预防措施**:
  1. ⚠️ **安装插件前检查是否已有同名插件存在**
  2. ⚠️ **定期运行 `openclaw skills check` 检查 duplicate 警告**
- **状态**: ✅ 已修复

### 错误4: Google Gemini API Key 泄露
- **时间**: 2026-06-15 22:30 发现
- **现象**: 图片识别调用报 403: "Your API key was reported as leaked"
- **根因**: API Key 可能被提交到公开仓库或被扫描发现
- **修复**: 需要更换新的 API Key
- **预防措施**:
  1. ⚠️ **API Key 不要硬编码在代码文件中**
  2. ⚠️ **使用 .env.secrets 或 openclaw secrets 管理密钥**
  3. ⚠️ **确保 .gitignore 包含 .env.secrets**
- **状态**: ❌ 待修复（需老板生成新 Key）

### 错误5: exec.ask 安全配置过于宽松
- **时间**: 2026-06-15 19:16
- **现象**: exec.ask = "off"，所有命令无需审批直接执行
- **修复**: 改为 "on-miss"，非白名单命令需要老板审批
- **预防措施**: 保持 on-miss 模式，定期检查白名单合理性
- **状态**: ✅ 已修复

---

## 2026-03-10: 技能安装错误
- **时间**: 2026-03-10 13:54
- **现象**: 安装了不存在的技能名称
- **解决方案**: 
  1. 使用 `clawhub search` 搜索正确的技能名称
  2. 检查已安装技能中是否有类似功能
  3. 使用现有技能或寻找替代方案
- **预防措施**:
  1. 安装技能前先搜索确认名称
  2. 检查是否已有类似功能的技能
- **状态**: ✅ 已解决

---

## 📋 执行前检查清单（Pre-Flight Checklist）

### 修改 JS/HTML 文件前
- [ ] `node --check filename.js` 验证语法
- [ ] 检查是否有重复的 id 或对象定义
- [ ] 修改后 curl 线上版本确认部署

### 修改 cron 任务前
- [ ] 检查任务的 model 是否显式指定
- [ ] 检查 timeoutSeconds 是否合理
- [ ] 检查 fallback 链是否配置
- [ ] 修改后手动触发一次验证

### 安装插件/技能前
- [ ] `openclaw skills check` 检查是否有 duplicate
- [ ] 检查 extensions/ 和 npm/ 下是否已有同名插件
- [ ] 安装后再次运行 check 确认无警告

### 涉及 API Key 的操作
- [ ] 不硬编码在代码中
- [ ] 使用 .env.secrets 管理
- [ ] 确认 .gitignore 包含密钥文件
- [ ] 推送前检查是否有密钥泄漏

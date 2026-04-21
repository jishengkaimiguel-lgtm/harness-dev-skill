---
name: harness-dev
description: |
  基于 Anthropic Harness Engineering 的三代理开发模式，为开发小白提供结构化、可验证的迭代开发流程。
  
  当用户需要开发任何软件项目时使用，包括但不限于：
  - 网站开发（前端/后端/全栈）
  - 移动应用开发
  - 脚本/工具开发
  - API 开发
  - 数据库设计
  - 代码重构
  
  触发词：开发、帮我做一个、帮我写、build、create、实现、做一个
  
  核心特点：
  1. Planner 代理：将需求分解为可执行的功能列表
  2. Generator 代理：按 Sprint 逐个实现功能
  3. Evaluator 代理：自动测试并给出改进建议
  4. 迭代循环：通过多轮改进提升质量
  
  适用场景：
  - 任何需要多步骤完成的开发任务
  - 对质量有要求的项目
  - 需要可验证完成标准的任务
  - 开发小白需要结构化指导的场景
---

# Harness 开发模式

> 基于 Anthropic Harness Engineering 的三代理架构，让 AI 开发从「单次对话生成」转向「结构化迭代工程」。

## 核心理念

**传统开发的问题**：
- AI 一次性生成代码，质量不可控
- 长任务中 AI 会「遗忘」早期需求
- 没有明确的「完成标准」
- 发现问题后需要重新生成，效率低

**Harness 的解决方案**：
- **分解**：将大任务拆分为小 Sprint
- **迭代**：通过多轮生成-评估-改进循环提升质量
- **验证**：每个 Sprint 都有明确的完成标准
- **记忆**：通过结构化工件传递上下文

## 四代理架构（优化版）

```
用户需求 ──▶ Planner ──▶ Generator ──▶ Inspector ──▶ Evaluator
                │            │            │            │
                ▼            ▼            ▼            ▼
            产品规格      功能实现      预检查报告    测试评分
         (spec.md)    (代码文件)   (inspect_report.md) (eval_report.md)
```

### 新增：Inspector（检查员）

**定位**：在 Generator 完成后、Evaluator 测试前，进行系统性预检查

**目标**：在测试前发现 80% 的低级错误，减少 Evaluator 的无效测试轮次

**检查清单**：

#### 1. 代码完整性检查
- [ ] 所有声明的文件是否都存在？
- [ ] 入口文件是否完整？（如 app.js、main.py、index.html）
- [ ] 配置文件是否缺失？（package.json、app.json、.env）

#### 2. 语法/格式检查
- [ ] JavaScript：运行 `node --check`
- [ ] JSON：验证格式（无 trailing comma）
- [ ] CSS/WXSS：检查语法错误
- [ ] SQL：检查语句完整性

#### 3. 命名一致性检查
- [ ] API 地址是否统一？（全局搜索域名/IP）
- [ ] 变量命名是否一致？（camelCase vs snake_case）
- [ ] 数据库字段与代码是否匹配？

#### 4. 配置文件检查
- [ ] 环境变量是否区分 dev/prod？
- [ ] 敏感信息是否硬编码？
- [ ] 端口配置是否正确？

#### 5. 数据库兼容性检查
- [ ] 表结构是否存在？
- [ ] 字段类型是否匹配？（enum、varchar 长度）
- [ ] 索引是否合理？

#### 6. 安全/权限检查
- [ ] 是否有权限控制？
- [ ] 输入是否验证？
- [ ] 是否有 SQL 注入风险？

**输出**：`inspect_report.md`
- 检查项通过率
- 发现的问题列表（按严重程度）
- 修复建议
- 是否允许进入 Evaluator 阶段

### 1. Planner（规划者）

**职责**：将用户的简短需求扩展为详细的产品规格

**输出文件**：
- `spec.md` - 产品规格说明书
- `feature_list.json` - 功能清单（带优先级和状态）

**关键原则**：
- 专注于产品上下文和高层技术设计
- 不过度指定技术实现细节（让 Generator 决定）
- 寻找机会集成 AI 功能
-  ambitious about scope

### 2. Generator（生成者）

**职责**：按 Sprint 逐个实现功能

**工作流程**：
1. 读取 spec.md 和 feature_list.json
2. 与 Evaluator 协商 Sprint 合约
3. 实现当前 Sprint 的功能
4. 自评估后提交给 Evaluator
5. 根据反馈改进或进入下一个 Sprint

**输出**：
- 可运行的代码
- 更新后的 feature_list.json（标记完成状态）
- `progress.txt` - 进度日志

### 3. Evaluator（评估者）

**职责**：测试实现并给出结构化评分

**评估维度**：

| 维度 | 权重 | 说明 |
|------|------|------|
| **功能性** | 高 | 功能是否按规格实现？ |
| **代码质量** | 高 | 可读性、结构、最佳实践 |
| **用户体验** | 中 | UI/UX 是否流畅？ |
| **完整性** | 中 | 是否处理了边界情况？ |

**评分标准**：
- 8-10分：优秀，可以进入下一个 Sprint
- 6-7分：良好，需要小幅改进
- <6分：需要重新实现

**输出**：
- `eval_report.md` - 评估报告（含分数和改进建议）

## 开发流程

### Phase 1: 规划（Planner）

```
用户：帮我做一个待办事项应用

Planner 思考：
- 核心功能：添加任务、标记完成、删除任务、筛选视图
- 技术栈：React + LocalStorage
- 设计方向：简洁现代，支持暗黑模式

输出：
├── spec.md（产品规格）
└── feature_list.json（10个功能点）
```

### Phase 2: Sprint 合约（Generator + Inspector + Evaluator）

```
Generator：我提议 Sprint 1 实现「添加任务」功能
- 实现：输入框 + 添加按钮
- 验证：用户可以输入任务并看到它出现在列表中

Inspector：预检查通过标准：
- app.json 格式正确（无 trailing comma）
- app.js 入口文件存在
- 无 console.log 调试代码残留
- API 地址统一

Evaluator：同意，但还需要验证：
- 空输入的处理
- 特殊字符的处理
- 输入长度限制

达成一致，开始实现。
```

### Phase 3: 实现与检查（新增 Inspector）

```
Generator：实现 Sprint 1

Inspector：自动执行检查清单
  1. 代码完整性检查
     - ✅ app.js 存在
     - ✅ app.json 格式正确
     - ❌ config.js 缺失 API 配置
  
  2. 命名一致性检查
     - ❌ 发现 2 处 API 地址不一致
       - pages/index/index.js: http://119.45.36.137:3000
       - pages/create-trip/create-trip.js: https://mimitravelsplit.fun
  
  3. 语法检查
     - ✅ 所有 JS 文件语法正确
     - ❌ app.json 有 trailing comma

检查报告：
- 严重问题：2 个（必须修复）
- 警告：1 个（建议修复）
- 评分：5/10（不通过，需修复后重新检查）

Generator：修复问题
Inspector：重新检查 → 评分 9/10（通过）

Evaluator：测试并评分
         - 功能性：9/10（基本功能工作，但缺少长度限制）
         - 代码质量：8/10
         - 用户体验：7/10（按钮样式需要优化）
         - 完整性：6/10（缺少边界情况处理）
         
         总分：7.5/10
         建议：添加长度限制，优化按钮样式

Generator：改进后重新评估
Evaluator：评分 9/10，通过！

更新 feature_list.json：Sprint 1 完成
进入 Sprint 2...
```

## 文件结构

```
project/
├── .harness/              # Harness 工作目录
│   ├── spec.md           # 产品规格（Planner 输出）
│   ├── feature_list.json # 功能清单
│   ├── progress.txt      # 进度日志
│   ├── inspect_reports/  # 检查报告（Inspector 输出）★新增
│   │   ├── sprint_01.md
│   │   └── ...
│   └── eval_reports/     # 评估报告（Evaluator 输出）
│       ├── sprint_01.md
│       ├── sprint_02.md
│       └── ...
├── scripts/              # 自动化脚本 ★新增
│   └── inspect.sh        # Inspector 检查脚本
├── src/                  # 源代码
├── tests/                # 测试文件
└── init.sh              # 环境初始化脚本
```

## 使用指南

### 对于开发小白

**你不需要懂代码，只需要**：

1. **描述你想要什么**
   - 用自然语言描述
   - 举例："像一个微信那样的聊天界面"
   - 说明关键功能："要能发图片、能撤回消息"

2. **回答 Planner 的问题**
   - Planner 可能会问："需要用户登录吗？"
   - 回答："不需要，匿名使用就行"

3. **验收每个 Sprint**
   - Evaluator 会告诉你功能是否完成
   - 你可以试用并说："这个按钮太小了"
   - Generator 会根据反馈改进

4. **控制项目范围**
   - 如果功能太多，可以说："先只做核心的 3 个功能"
   - 如果太复杂，可以说："简化一下，先做 MVP"

### 最佳实践

#### 1. 从简单开始

**不要**：
> "帮我做一个像淘宝那样的电商平台"

**要**：
> "帮我做一个简单的商品展示页面，能显示商品图片、名称和价格"

#### 2. 明确验收标准

**不要**：
> "做个好看点"

**要**：
> "按钮要明显，文字要清晰，在手机上也能正常显示"

#### 3. 及时反馈

每个 Sprint 完成后：
- ✅ "这个很好，继续下一个"
- ⚠️ "这个功能工作，但颜色不太对"
- ❌ "这个完全不是我想要的，我们重新讨论一下"

#### 4. 接受迭代

质量是迭代出来的：
- 第一轮：基本功能可用（6-7分）
- 第二轮：优化体验（8分）
- 第三轮：打磨细节（9分）

## 评估标准详解

### 功能性（40%）

**检查点**：
- [ ] 核心功能按规格实现
- [ ] 边界情况处理（空输入、超长内容等）
- [ ] 错误处理（网络失败、无效操作等）
- [ ] 数据持久化（如果需要）

**示例**：
```
待办应用的功能性检查：
✅ 可以添加任务
✅ 可以标记完成
✅ 可以删除任务
✅ 空任务不能添加
✅ 超长任务有提示
✅ 刷新页面数据不丢失
```

### 代码质量（30%）

**检查点**：
- [ ] 代码可读性（命名清晰、有注释）
- [ ] 代码结构（模块化、不重复）
- [ ] 最佳实践（符合语言/框架规范）
- [ ] 可维护性（易于修改和扩展）

### 用户体验（20%）

**检查点**：
- [ ] 界面美观（布局合理、配色协调）
- [ ] 交互流畅（响应及时、反馈明确）
- [ ] 易于理解（新手能看懂怎么用）
- [ ] 错误友好（出错时有明确提示）

### 完整性（10%）

**检查点**：
- [ ] 文档完整（README、使用说明）
- [ ] 配置说明（如何运行、如何部署）
- [ ] 测试覆盖（关键功能有测试）

## Inspector 自动化工具

### 快速检查命令

```bash
# 1. 检查所有 API 地址是否一致
grep -r "http" src/ | grep -E "(api|localhost|127\.0\.0\.1)" | sort | uniq

# 2. 检查 JSON 语法
find . -name "*.json" -exec node -e "JSON.parse(require('fs').readFileSync('{}'))" \;

# 3. 检查 JS 语法
find . -name "*.js" -exec node --check {} \;

# 4. 检查入口文件是否存在
ls -la src/app.js src/app.json src/app.wxss 2>/dev/null || echo "缺失入口文件"

# 5. 检查数据库字段（MySQL）
mysql -u user -p -e "DESCRIBE database.table;"

# 6. 检查是否有 TODO/调试代码
grep -r "TODO\|FIXME\|console.log\|debugger" src/ --include="*.js"
```

### 检查脚本模板

创建 `scripts/inspect.sh`：

```bash
#!/bin/bash

echo "🔍 Harness Inspector 检查中..."

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

ERRORS=0
WARNINGS=0

# 1. 检查入口文件
echo -e "\n📁 检查入口文件..."
if [ ! -f "src/app.js" ]; then
    echo -e "${RED}❌ 缺失 src/app.js${NC}"
    ((ERRORS++))
else
    echo -e "${GREEN}✅ src/app.js 存在${NC}"
fi

# 2. 检查 JSON 语法
echo -e "\n📋 检查 JSON 语法..."
for file in $(find src -name "*.json"); do
    if node -e "JSON.parse(require('fs').readFileSync('$file'))" 2>/dev/null; then
        echo -e "${GREEN}✅ $file${NC}"
    else
        echo -e "${RED}❌ $file 格式错误${NC}"
        ((ERRORS++))
    fi
done

# 3. 检查 JS 语法
echo -e "\n🔧 检查 JS 语法..."
for file in $(find src -name "*.js"); do
    if node --check "$file" 2>/dev/null; then
        echo -e "${GREEN}✅ $file${NC}"
    else
        echo -e "${RED}❌ $file 语法错误${NC}"
        ((ERRORS++))
    fi
done

# 4. 检查 API 地址一致性
echo -e "\n🌐 检查 API 地址..."
APIS=$(grep -r "http" src/ --include="*.js" | grep -v "// " | wc -l)
UNIQUE_APIS=$(grep -r "http" src/ --include="*.js" | grep -v "// " | sort | uniq | wc -l)
if [ "$APIS" -eq "$UNIQUE_APIS" ]; then
    echo -e "${GREEN}✅ API 地址一致${NC}"
else
    echo -e "${YELLOW}⚠️ 发现 $((APIS - UNIQUE_APIS)) 处不一致${NC}"
    ((WARNINGS++))
fi

# 5. 检查 TODO/调试代码
echo -e "\n🔍 检查调试代码..."
TODOS=$(grep -r "TODO\|FIXME\|console.log" src/ --include="*.js" | wc -l)
if [ "$TODOS" -eq 0 ]; then
    echo -e "${GREEN}✅ 无调试代码残留${NC}"
else
    echo -e "${YELLOW}⚠️ 发现 $TODOS 处调试代码${NC}"
    ((WARNINGS++))
fi

# 总结
echo -e "\n📊 检查报告"
echo "==================="
if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}✅ 全部通过，可以进入 Evaluator 阶段${NC}"
    exit 0
elif [ $ERRORS -eq 0 ]; then
    echo -e "${YELLOW}⚠️ 有 $WARNINGS 个警告，建议修复${NC}"
    exit 0
else
    echo -e "${RED}❌ 有 $ERRORS 个错误，必须修复${NC}"
    exit 1
fi
```

## 经验教训（来自 TripSplit V1.0 实战）

### 问题 1：API 地址不一致
**现象**：前端调用 `https://mimitravelsplit.fun`，但后端实际在 `http://119.45.36.137:3000`
**影响**：网络请求失败，功能无法测试
**解决方案**：
- 创建 `config.js` 统一配置 API 地址
- 每次修改后用 `grep` 检查所有文件
- 使用环境变量区分开发和生产环境

### 问题 2：数据库字段不匹配
**现象**：`status` 字段是 `enum('active','deleted')`，但代码设置 `'ended'`
**影响**："Data truncated for column status" 错误
**解决方案**：
- 修改数据库前先查看现有结构：`DESCRIBE table`
- 使用 `ALTER TABLE` 添加新枚举值
- 或修改代码使用现有枚举值

### 问题 3：命名不一致
**现象**：后端返回 `inviteCode`，前端使用 `invite_code`
**影响**：数据绑定不显示
**解决方案**：
- 统一命名规范（推荐 snake_case 用于数据库/API）
- 创建数据转换层统一处理

### 问题 4：软删除未过滤
**现象**：删除后记录仍在列表显示
**影响**：用户困惑，数据混乱
**解决方案**：
- 所有查询添加 `WHERE status != 'deleted'`
- 或数据库层面使用视图过滤

### 问题 5：浮点数精度
**现象**：显示 `¥626.6599999999999` 而不是 `¥626.66`
**影响**：UI 不专业
**解决方案**：
- 后端返回前 `toFixed(2)`
- 或使用 WXS 过滤器格式化

### 问题 6：权限控制缺失
**现象**：任何用户都能删除/修改任何旅程
**影响**：数据安全问题
**解决方案**：
- 每个操作检查 `created_by === userId`
- 后端返回 403 无权操作

### 开发流程优化建议

1. **开始前**：
   - [ ] 确认技术栈和部署环境
   - [ ] 设计数据库表结构
   - [ ] 定义 API 接口规范

2. **开发中**：
   - [ ] 每个 Sprint 后运行语法检查
   - [ ] 使用 `grep` 确保命名一致
   - [ ] 测试边界情况（空数据、权限错误）

3. **发布前**：
   - [ ] 全局搜索 TODO/测试代码
   - [ ] 确认生产环境配置
   - [ ] 数据库备份

## 常见问题

### Q: 一个项目需要多少轮迭代？

A: 取决于复杂度：
- 简单功能（如一个按钮）：1-2 轮
- 中等功能（如表单）：3-5 轮
- 复杂功能（如聊天系统）：5-10 轮

### Q: 如果 Evaluator 太严格怎么办？

A: 可以调整评估标准：
- "这是 MVP，功能性优先，UI 可以简化"
- "先做能用的，细节后面再优化"

### Q: 可以跳过某些 Sprint 吗？

A: 可以，如果：
- 功能已经满足需求
- 时间/成本有限
- 后续可以增量改进

### Q: 如何控制成本？

A: 策略：
- 明确 MVP 范围，避免过度设计
- 设置评分阈值（如 7 分即可通过）
- 优先实现核心功能，边缘功能后续添加

## 参考资源

- [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Anthropic: Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- [Anthropic: Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices)

## 示例对话

### 示例 1：简单网站

**用户**：帮我做一个个人博客网站

**Planner**：
> 我将为你规划一个简洁的个人博客，包含：
> 1. 首页：文章列表
> 2. 文章页：显示单篇文章
> 3. 关于页：个人介绍
> 4. 响应式设计（手机/桌面）
> 
> 技术栈：HTML + CSS + JavaScript（无需后端）
> 预计 3 个 Sprint，每个 Sprint 实现一个页面。

**用户**：好的，开始吧。

**[进入 Sprint 循环...]**

### 示例 2：工具脚本

**用户**：帮我写一个批量重命名文件的脚本

**Planner**：
> 功能规划：
> 1. 支持按序号重命名（file_001.jpg, file_002.jpg）
> 2. 支持添加前缀/后缀
> 3. 支持正则表达式替换
> 4. 预览模式（先显示结果，确认后再执行）
> 5. 撤销功能
>
> 技术栈：Python
> 预计 2 个 Sprint。

**用户**：先做 1 和 4 就行，其他的以后再说。

**[调整范围后进入 Sprint...]**

---

**记住**：Harness 的核心是**迭代**和**验证**。不要期望一次完美，而是通过多轮改进逐步逼近目标。
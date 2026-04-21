# Harness Dev Skill V2.0

基于 [Anthropic Harness Engineering](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) 的四代理开发模式，为开发小白提供结构化、可验证的迭代开发流程。

**V2.0 更新**：新增 Inspector（检查员）代理，在测试前自动发现 80% 的低级错误。

[English](#english) | [中文](#中文)

---

## 中文

### 🎯 核心理念

**传统开发的问题**：
- AI 一次性生成代码，质量不可控
- 长任务中 AI 会「遗忘」早期需求
- 没有明确的「完成标准」
- 低级错误反复出现（API 不一致、语法错误、文件缺失）

**Harness V2.0 的解决方案**：
- **分解**：将大任务拆分为小 Sprint
- **预检查**：Inspector 在测试前系统性检查代码
- **迭代**：通过多轮生成-检查-评估-改进循环提升质量
- **验证**：每个 Sprint 都有明确的完成标准

### 🏗️ 四代理架构（V2.0）

```
用户需求 ──▶ Planner ──▶ Generator ──▶ Inspector ──▶ Evaluator
                │            │            │            │
                ▼            ▼            ▼            ▼
            产品规格      功能实现      预检查报告    测试评分
                      (代码文件)   (inspect_report.md) (eval_report.md)
```

| 代理 | 职责 | 输出 |
|------|------|------|
| **Planner** | 将需求分解为可执行的功能列表 | `spec.md`, `feature_list.json` |
| **Generator** | 按 Sprint 逐个实现功能 | 可运行的代码 |
| **Inspector** ★新增 | 系统性预检查（完整性、语法、一致性） | `inspect_report.md` |
| **Evaluator** | 测试并给出结构化评分 | `eval_report.md` |

### 🔍 Inspector 检查清单

在 Generator 完成后、Evaluator 测试前，Inspector 自动执行：

| 检查维度 | 检查内容 | 工具 |
|---------|---------|------|
| **代码完整性** | 入口文件、配置文件是否存在 | `ls`, `find` |
| **语法检查** | JS/JSON/CSS 语法正确性 | `node --check` |
| **命名一致性** | API 地址、变量命名是否统一 | `grep` |
| **配置检查** | 环境变量、敏感信息处理 | 正则匹配 |
| **数据库兼容** | 字段类型、枚举值匹配 | `DESCRIBE` |
| **安全检查** | 权限控制、输入验证 | 代码审查 |

**一键检查**：
```bash
./scripts/inspect.sh
```

### 📊 评估标准

| 维度 | 权重 | 说明 |
|------|------|------|
| **功能性** | 40% | 功能是否按规格实现 |
| **代码质量** | 30% | 可读性、结构、最佳实践 |
| **用户体验** | 20% | UI/UX 是否流畅 |
| **完整性** | 10% | 文档、配置、测试 |

### 🚀 使用方法

#### 1. 安装 Skill

将本仓库克隆到 OpenClaw 的 skills 目录：

```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/jishengkaimiguel-lgtm/harness-dev-skill.git harness-dev
```

#### 2. 触发开发

对 AI 说：
> "帮我做一个待办事项应用"

AI 会自动进入 Harness 模式：
1. **Planner** 创建产品规格
2. **Generator** 按 Sprint 实现代码
3. **Inspector** ★ 自动检查代码问题
4. **Evaluator** 测试并评分
5. **迭代** 直到质量达标

#### 3. 项目结构

```
project/
├── .harness/                 # Harness 工作目录
│   ├── spec.md              # 产品规格
│   ├── feature_list.json    # 功能清单
│   ├── progress.txt         # 进度日志
│   ├── inspect_reports/     # ★ 检查报告（Inspector 输出）
│   │   └── sprint_01.md
│   └── eval_reports/        # 评估报告（Evaluator 输出）
│       └── sprint_01.md
├── scripts/                 # ★ 自动化脚本
│   └── inspect.sh          # Inspector 检查脚本
├── src/                     # 源代码
├── tests/                   # 测试文件
└── init.sh                  # 环境初始化
```

### 💡 为开发小白优化

- ✅ 用自然语言描述需求
- ✅ 每个 Sprint 都有明确的验收标准
- ✅ 不懂代码也能评估（"这个按钮太小了"）
- ✅ 控制项目范围（MVP → 迭代增强）
- ✅ ★ Inspector 自动发现低级错误，减少返工

### 🛠️ 快速修复命令

```bash
# 检查所有 API 地址是否一致
grep -r "http" src/ | grep -E "(api|localhost)" | sort | uniq

# 检查 JSON 语法
find . -name "*.json" -exec node -e "JSON.parse(require('fs').readFileSync('{}'))" \;

# 检查是否有 TODO/调试代码
grep -r "TODO\|FIXME\|console.log\|debugger" src/ --include="*.js"
```

### 📚 参考资源

- [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Anthropic: Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- [Anthropic: Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices)

---

## English

### 🎯 Core Concept

**Problems with traditional development**:
- AI generates code in one shot, quality is uncontrollable
- AI "forgets" early requirements in long tasks
- No clear "definition of done"
- Low-level errors recur (API inconsistency, syntax errors, missing files)

**Harness V2.0 solution**:
- **Decompose**: Break large tasks into small Sprints
- **Pre-check**: Inspector systematically checks code before testing
- **Iterate**: Improve quality through multiple generate-inspect-evaluate-improve cycles
- **Verify**: Each Sprint has clear acceptance criteria

### 🏗️ Four-Agent Architecture (V2.0)

```
User Request ──▶ Planner ──▶ Generator ──▶ Inspector ──▶ Evaluator
                    │            │            │            │
                    ▼            ▼            ▼            ▼
               Product Spec   Implementation Pre-check    Test & Score
                           (code files)   (inspect_report) (eval_report)
```

| Agent | Responsibility | Output |
|-------|---------------|--------|
| **Planner** | Decompose requirements into executable feature list | `spec.md`, `feature_list.json` |
| **Generator** | Implement features Sprint by Sprint | Working code |
| **Inspector** ★NEW | Systematic pre-check (completeness, syntax, consistency) | `inspect_report.md` |
| **Evaluator** | Test and give structured scores | `eval_report.md` |

### 🔍 Inspector Checklist

After Generator completes and before Evaluator tests, Inspector automatically runs:

| Check Dimension | Content | Tool |
|----------------|---------|------|
| **Code Completeness** | Entry files, config files exist | `ls`, `find` |
| **Syntax Check** | JS/JSON/CSS syntax correctness | `node --check` |
| **Naming Consistency** | API addresses, variable naming uniform | `grep` |
| **Config Check** | Environment variables, sensitive info | Regex |
| **DB Compatibility** | Field types, enum values match | `DESCRIBE` |
| **Security Check** | Permission control, input validation | Code review |

**One-click check**:
```bash
./scripts/inspect.sh
```

### 📊 Evaluation Criteria

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Functionality** | 40% | Features implemented as specified |
| **Code Quality** | 30% | Readability, structure, best practices |
| **User Experience** | 20% | UI/UX smoothness |
| **Completeness** | 10% | Documentation, configuration, tests |

### 🚀 Usage

#### 1. Install Skill

Clone this repo to OpenClaw's skills directory:

```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/jishengkaimiguel-lgtm/harness-dev-skill.git harness-dev
```

#### 2. Trigger Development

Say to AI:
> "Help me build a todo app"

AI will automatically enter Harness mode:
1. **Planner** creates product specification
2. **Generator** implements Sprint by Sprint
3. **Inspector** ★ automatically checks code issues
4. **Evaluator** tests and scores
5. **Iterate** until quality meets standard

#### 3. Project Structure

```
project/
├── .harness/                 # Harness working directory
│   ├── spec.md              # Product specification
│   ├── feature_list.json    # Feature list
│   ├── progress.txt         # Progress log
│   ├── inspect_reports/     # ★ Inspect reports (Inspector output)
│   │   └── sprint_01.md
│   └── eval_reports/        # Eval reports (Evaluator output)
│       └── sprint_01.md
├── scripts/                 # ★ Automation scripts
│   └── inspect.sh          # Inspector check script
├── src/                     # Source code
├── tests/                   # Test files
└── init.sh                  # Environment init
```

### 💡 Optimized for Coding Beginners

- ✅ Describe requirements in natural language
- ✅ Each Sprint has clear acceptance criteria
- ✅ No coding knowledge needed for evaluation ("this button is too small")
- ✅ Control project scope (MVP → iterative enhancement)
- ✅ ★ Inspector automatically finds low-level errors, reduces rework

### 🛠️ Quick Fix Commands

```bash
# Check if all API addresses are consistent
grep -r "http" src/ | grep -E "(api|localhost)" | sort | uniq

# Check JSON syntax
find . -name "*.json" -exec node -e "JSON.parse(require('fs').readFileSync('{}'))" \;

# Check for TODO/debug code
grep -r "TODO\|FIXME\|console.log\|debugger" src/ --include="*.js"
```

---

## Changelog

### V2.0 (2026-04-22)
- ★ **新增 Inspector 代理**：系统性预检查，减少低级错误
- ★ **新增自动化检查脚本**：`scripts/inspect.sh` 一键检查
- ★ **新增检查清单**：6 大维度（完整性、语法、一致性、配置、数据库、安全）
- ★ **新增经验教训章节**：来自 TripSplit V1.0 实战经验

### V1.0 (2026-04-20)
- 基础三代理架构（Planner + Generator + Evaluator）
- Sprint 合约机制
- 结构化评估标准

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Inspired by [Anthropic's Harness Engineering](https://www.anthropic.com/engineering)
- Built for [OpenClaw](https://github.com/openclaw/openclaw) AI assistant platform
- V2.0 实战经验来自 [TripSplit](https://github.com/jishengkaimiguel-lgtm/openclaw-workspace) 项目

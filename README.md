# Harness Dev Skill

基于 [Anthropic Harness Engineering](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) 的三代理开发模式，为开发小白提供结构化、可验证的迭代开发流程。

[English](#english) | [中文](#中文)

---

## 中文

### 🎯 核心理念

**传统开发的问题**：
- AI 一次性生成代码，质量不可控
- 长任务中 AI 会「遗忘」早期需求
- 没有明确的「完成标准」

**Harness 的解决方案**：
- **分解**：将大任务拆分为小 Sprint
- **迭代**：通过多轮生成-评估-改进循环提升质量
- **验证**：每个 Sprint 都有明确的完成标准

### 🏗️ 三代理架构

```
用户需求 ──▶ Planner ──▶ Generator ──▶ Evaluator
                │            │            │
                ▼            ▼            ▼
            产品规格      功能实现      测试评分
```

| 代理 | 职责 | 输出 |
|------|------|------|
| **Planner** | 将需求分解为可执行的功能列表 | `spec.md`, `feature_list.json` |
| **Generator** | 按 Sprint 逐个实现功能 | 可运行的代码 |
| **Evaluator** | 测试并给出结构化评分 | `eval_report.md` |

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
git clone https://github.com/YOUR_USERNAME/harness-dev-skill.git harness-dev
```

#### 2. 触发开发

对 AI 说：
> "帮我做一个待办事项应用"

AI 会自动进入 Harness 模式：
1. **Planner** 创建产品规格
2. **Generator** 按 Sprint 实现
3. **Evaluator** 测试并评分
4. **迭代** 直到质量达标

#### 3. 项目结构

```
project/
├── .harness/              # Harness 工作目录
│   ├── spec.md           # 产品规格
│   ├── feature_list.json # 功能清单
│   ├── progress.txt      # 进度日志
│   └── eval_reports/     # 评估报告
├── src/                   # 源代码
├── tests/                 # 测试文件
└── init.sh               # 环境初始化
```

### 💡 为开发小白优化

- ✅ 用自然语言描述需求
- ✅ 每个 Sprint 都有明确的验收标准
- ✅ 不懂代码也能评估（"这个按钮太小了"）
- ✅ 控制项目范围（MVP → 迭代增强）

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

**Harness solution**:
- **Decompose**: Break large tasks into small Sprints
- **Iterate**: Improve quality through multiple generate-evaluate-improve cycles
- **Verify**: Each Sprint has clear acceptance criteria

### 🏗️ Three-Agent Architecture

```
User Request ──▶ Planner ──▶ Generator ──▶ Evaluator
                    │            │            │
                    ▼            ▼            ▼
               Product Spec   Implementation  Test & Score
```

| Agent | Responsibility | Output |
|-------|---------------|--------|
| **Planner** | Decompose requirements into executable feature list | `spec.md`, `feature_list.json` |
| **Generator** | Implement features Sprint by Sprint | Working code |
| **Evaluator** | Test and give structured scores | `eval_report.md` |

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
git clone https://github.com/YOUR_USERNAME/harness-dev-skill.git harness-dev
```

#### 2. Trigger Development

Say to AI:
> "Help me build a todo app"

AI will automatically enter Harness mode:
1. **Planner** creates product specification
2. **Generator** implements Sprint by Sprint
3. **Evaluator** tests and scores
4. **Iterate** until quality meets standard

### 💡 Optimized for Coding Beginners

- ✅ Describe requirements in natural language
- ✅ Each Sprint has clear acceptance criteria
- ✅ No coding knowledge needed for evaluation ("this button is too small")
- ✅ Control project scope (MVP → iterative enhancement)

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Inspired by [Anthropic's Harness Engineering](https://www.anthropic.com/engineering)
- Built for [OpenClaw](https://github.com/openclaw/openclaw) AI assistant platform

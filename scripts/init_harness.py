#!/usr/bin/env python3
"""
Harness 项目初始化脚本
创建项目结构和初始文件
"""

import os
import json
import sys
from datetime import datetime

def init_harness_project(project_path="."):
    """初始化 Harness 项目结构"""
    
    # 创建目录结构
    dirs = [
        ".harness/eval_reports",
        "src",
        "tests",
        "docs"
    ]
    
    for d in dirs:
        os.makedirs(os.path.join(project_path, d), exist_ok=True)
        print(f"✅ 创建目录: {d}")
    
    # 创建初始文件
    
    # 1. feature_list.json 模板
    feature_list = {
        "project_name": "",
        "created_at": datetime.now().isoformat(),
        "sprints": [],
        "current_sprint": 0,
        "status": "planning"
    }
    
    with open(os.path.join(project_path, ".harness/feature_list.json"), "w") as f:
        json.dump(feature_list, f, indent=2)
    print("✅ 创建: .harness/feature_list.json")
    
    # 2. progress.txt 模板
    progress_template = f"""# Harness 项目进度日志

项目启动时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Sprint 记录

"""
    
    with open(os.path.join(project_path, ".harness/progress.txt"), "w") as f:
        f.write(progress_template)
    print("✅ 创建: .harness/progress.txt")
    
    # 3. spec.md 模板
    spec_template = """# 产品规格说明书

## 项目概述

- **项目名称**: 
- **目标用户**: 
- **核心功能**: 

## 功能列表

### Sprint 1
- [ ] 功能 1
- [ ] 功能 2

### Sprint 2
- [ ] 功能 3
- [ ] 功能 4

## 技术栈

- 前端: 
- 后端: 
- 数据库: 

## 设计方向

- 风格: 
- 配色: 
- 布局: 

## 验收标准

1. 
2. 
3. 
"""
    
    with open(os.path.join(project_path, ".harness/spec.md"), "w") as f:
        f.write(spec_template)
    print("✅ 创建: .harness/spec.md")
    
    # 4. init.sh 模板
    init_sh = """#!/bin/bash
# 项目初始化脚本

echo "🚀 初始化 Harness 项目..."

# 安装依赖（根据技术栈修改）
# npm install
# pip install -r requirements.txt

echo "✅ 初始化完成"
echo "📋 下一步:"
echo "  1. 编辑 .harness/spec.md 完善产品规格"
echo "  2. 开始 Sprint 1"
"""
    
    with open(os.path.join(project_path, "init.sh"), "w") as f:
        f.write(init_sh)
    os.chmod(os.path.join(project_path, "init.sh"), 0o755)
    print("✅ 创建: init.sh")
    
    # 5. README.md
    readme = """# Harness 项目

使用 [Harness 开发模式](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) 构建的项目。

## 快速开始

```bash
# 1. 初始化环境
./init.sh

# 2. 查看产品规格
cat .harness/spec.md

# 3. 查看功能清单
cat .harness/feature_list.json
```

## 项目结构

```
.
├── .harness/          # Harness 工作目录
│   ├── spec.md       # 产品规格
│   ├── feature_list.json  # 功能清单
│   ├── progress.txt  # 进度日志
│   └── eval_reports/ # 评估报告
├── src/              # 源代码
├── tests/            # 测试文件
└── docs/             # 文档
```

## 开发流程

1. **Planner**: 创建产品规格和功能清单
2. **Generator**: 按 Sprint 实现功能
3. **Evaluator**: 测试并给出改进建议
4. **迭代**: 重复直到质量达标

## 评估标准

- **功能性** (40%): 功能是否按规格实现
- **代码质量** (30%): 可读性、结构、最佳实践
- **用户体验** (20%): UI/UX 是否流畅
- **完整性** (10%): 文档、配置、测试
"""
    
    with open(os.path.join(project_path, "README.md"), "w") as f:
        f.write(readme)
    print("✅ 创建: README.md")
    
    print("\n🎉 Harness 项目初始化完成!")
    print("\n📋 下一步:")
    print("  1. 编辑 .harness/spec.md 完善产品规格")
    print("  2. 编辑 .harness/feature_list.json 添加功能点")
    print("  3. 运行 ./init.sh 安装依赖")
    print("  4. 开始第一个 Sprint!")

if __name__ == "__main__":
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    init_harness_project(project_path)

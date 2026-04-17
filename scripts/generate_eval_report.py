#!/usr/bin/env python3
"""
生成 Sprint 评估报告
"""

import json
import sys
from datetime import datetime

def generate_eval_report(sprint_num, scores, feedback, project_path="."):
    """生成评估报告"""
    
    report = f"""# Sprint {sprint_num} 评估报告

**评估时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## 评分

| 维度 | 权重 | 得分 | 加权得分 |
|------|------|------|----------|
| 功能性 | 40% | {scores.get('functionality', 0)}/10 | {scores.get('functionality', 0) * 0.4:.1f} |
| 代码质量 | 30% | {scores.get('code_quality', 0)}/10 | {scores.get('code_quality', 0) * 0.3:.1f} |
| 用户体验 | 20% | {scores.get('ux', 0)}/10 | {scores.get('ux', 0) * 0.2:.1f} |
| 完整性 | 10% | {scores.get('completeness', 0)}/10 | {scores.get('completeness', 0) * 0.1:.1f} |
| **总分** | 100% | - | **{sum([
    scores.get('functionality', 0) * 0.4,
    scores.get('code_quality', 0) * 0.3,
    scores.get('ux', 0) * 0.2,
    scores.get('completeness', 0) * 0.1
]):.1f}/10** |

## 详细反馈

### ✅ 优点

{chr(10).join([f"- {item}" for item in feedback.get('pros', [])]) or "- （待填写）"}

### ⚠️ 需要改进

{chr(10).join([f"- {item}" for item in feedback.get('cons', [])]) or "- （待填写）"}

### 🎯 改进建议

{chr(10).join([f"{i+1}. {item}" for i, item in enumerate(feedback.get('suggestions', []))]) or "1. （待填写）"}

## 决策

- [ ] **通过** (>= 8.0 分) - 可以进入下一个 Sprint
- [ ] **改进** (6.0-7.9 分) - 需要小幅改进后重新评估
- [ ] **重做** (< 6.0 分) - 需要重新实现

## 下一步行动

{feedback.get('next_action', '（根据决策填写）')}

---
*由 Evaluator 代理生成*
"""
    
    # 保存报告
    report_path = f"{project_path}/.harness/eval_reports/sprint_{sprint_num:02d}.md"
    with open(report_path, "w") as f:
        f.write(report)
    
    print(f"✅ 评估报告已保存: {report_path}")
    
    # 计算总分
    total = (
        scores.get('functionality', 0) * 0.4 +
        scores.get('code_quality', 0) * 0.3 +
        scores.get('ux', 0) * 0.2 +
        scores.get('completeness', 0) * 0.1
    )
    
    print(f"\n📊 Sprint {sprint_num} 评分: {total:.1f}/10")
    
    if total >= 8.0:
        print("🎉 评估结果: 通过! 可以进入下一个 Sprint")
    elif total >= 6.0:
        print("⚠️ 评估结果: 需要改进")
    else:
        print("❌ 评估结果: 需要重做")
    
    return total

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python generate_eval_report.py <sprint_num>")
        print("示例: python generate_eval_report.py 1")
        sys.exit(1)
    
    sprint_num = int(sys.argv[1])
    
    # 示例评分（实际使用时由 Evaluator 填写）
    scores = {
        'functionality': 8,
        'code_quality': 7,
        'ux': 8,
        'completeness': 6
    }
    
    feedback = {
        'pros': ['核心功能工作正常', '代码结构清晰'],
        'cons': ['缺少边界情况处理', '文档不完整'],
        'suggestions': ['添加输入验证', '补充 README', '添加错误处理'],
        'next_action': '根据改进建议优化后重新评估'
    }
    
    generate_eval_report(sprint_num, scores, feedback)

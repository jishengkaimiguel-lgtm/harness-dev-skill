#!/bin/bash
# 自动安装 GitHub CLI 并推送仓库

set -e

echo "🚀 开始推送 Harness Dev Skill 到 GitHub..."

# 检查是否已安装 gh
if command -v gh &> /dev/null; then
    echo "✅ GitHub CLI 已安装"
else
    echo "📦 安装 GitHub CLI..."
    
    # 检测操作系统
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        if command -v brew &> /dev/null; then
            brew install gh
        else
            echo "❌ 请先安装 Homebrew: https://brew.sh"
            exit 1
        fi
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        if command -v apt &> /dev/null; then
            sudo apt update && sudo apt install -y gh
        elif command -v yum &> /dev/null; then
            sudo yum install -y gh
        else
            echo "❌ 不支持的包管理器，请手动安装: https://github.com/cli/cli#installation"
            exit 1
        fi
    else
        echo "❌ 不支持的操作系统，请手动安装: https://github.com/cli/cli#installation"
        exit 1
    fi
    
    echo "✅ GitHub CLI 安装完成"
fi

# 检查是否已登录
echo "🔐 检查 GitHub 登录状态..."
if ! gh auth status &> /dev/null; then
    echo "📝 请登录 GitHub..."
    gh auth login
else
    echo "✅ 已登录 GitHub"
fi

# 获取当前用户名
echo "👤 获取 GitHub 用户名..."
USERNAME=$(gh api user -q '.login')
echo "✅ 用户名: $USERNAME"

# 进入项目目录
cd "$(dirname "$0")"

# 检查是否已有远程仓库
if git remote get-url origin &> /dev/null; then
    echo "🔄 远程仓库已存在，直接推送..."
    git push -u origin main
else
    echo "📁 创建 GitHub 仓库..."
    
    # 创建仓库
    gh repo create harness-dev-skill \
        --public \
        --description "基于 Anthropic Harness Engineering 的三代理开发模式 Skill，为开发小白提供结构化、可验证的迭代开发流程" \
        --source=. \
        --remote=origin \
        --push
fi

echo ""
echo "🎉 推送成功！"
echo ""
echo "📎 仓库地址: https://github.com/$USERNAME/harness-dev-skill"
echo ""
echo "📋 下一步："
echo "  1. 访问仓库查看代码"
echo "  2. 在 README 中添加你的用户名"
echo "  3. 分享给社区"

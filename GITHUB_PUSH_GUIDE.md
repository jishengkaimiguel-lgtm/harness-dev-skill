# GitHub 推送指南

## 方法 1: 使用 GitHub CLI（推荐）

### 1. 安装 GitHub CLI
```bash
# macOS
brew install gh

# 其他系统见 https://github.com/cli/cli#installation
```

### 2. 登录 GitHub
```bash
gh auth login
```

### 3. 创建仓库并推送
```bash
cd /Users/miguelji/.openclaw/workspace/skills/harness-dev

# 创建仓库
gh repo create harness-dev-skill \
  --public \
  --description "基于 Anthropic Harness Engineering 的三代理开发模式 Skill" \
  --source=. \
  --remote=origin \
  --push
```

## 方法 2: 手动创建仓库

### 1. 在 GitHub 上创建仓库
1. 访问 https://github.com/new
2. 填写信息：
   - Repository name: `harness-dev-skill`
   - Description: `基于 Anthropic Harness Engineering 的三代理开发模式 Skill`
   - 选择 Public
   - 不要勾选 "Initialize this repository with a README"
3. 点击 Create repository

### 2. 推送本地代码
```bash
cd /Users/miguelji/.openclaw/workspace/skills/harness-dev

# 添加远程仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/harness-dev-skill.git

# 推送代码
git branch -M main
git push -u origin main
```

## 方法 3: 使用 GitHub Web 界面

如果你不想用命令行：

1. 在 GitHub 创建空仓库
2. 点击 "uploading an existing file"
3. 拖拽上传所有文件
4. 提交更改

## 验证推送成功

访问 `https://github.com/YOUR_USERNAME/harness-dev-skill` 查看代码是否已上传。

## 后续更新

```bash
# 修改代码后
git add .
git commit -m "描述你的更改"
git push origin main
```

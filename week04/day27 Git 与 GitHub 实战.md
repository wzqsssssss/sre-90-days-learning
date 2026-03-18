# 📖 Day 27 笔记：Git 与 GitHub 实战

---

## ✅ 今日任务完成情况

- [X] 安装 Git 并配置用户名/邮箱
- [X] **创建 GitHub 仓库** `sre-90-days-learning`
- [X] **将本周所有** `.py` **文件 push 成功**

---

## 🔧 关键操作记录

```bash
# 首次配置
git config --global user.name "YourName"
git config --global user.email "you@example.com"

# 初始化 & 提交
git init
git add .
git commit -m "feat: add week4 python scripts"

# 关联远程仓库（替换 YOUR_REPO_URL）
git remote add origin https://github.com/yourname/sre-90days.git
git push -u origin main
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**`git push` **被拒绝（non-fast-forward）**
  **解决** **：先** `git pull --rebase`，或新建空仓库再 push
* **问题** **：每次都要输密码**
  **解决** **：用 HTTPS 凭据管理 或 改用 SSH 密钥（进阶）**

---

## 💡 小技巧 / 收获

* `git log --oneline` **查看简洁提交历史**
* `.gitignore` **可忽略日志/缓存文件（如** `*.log`, `__pycache__/`）

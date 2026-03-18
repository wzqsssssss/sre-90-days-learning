# Week 1 - Python & Git 运维速查表

> ✅ 所有命令均在 Ubuntu 24.04 验证 + Python 3.12.3 验证
> 💡 使用原则：能复制、能执行、能解决问题

---

## 🔹 Python 基础与开发环境

```bash
# 查看 Python 版本
python3 --version

# 安装 pip（若未预装）
sudo apt install python3-pip -y

# 创建虚拟环境（推荐）
python3 -m venv sre-env
source sre-env/bin/activate   # 激活
deactivate                    # 退出

# 安装第三方库
pip install requests psutil

# 运行脚本
python3 system_monitor.py
```

---

## 🔹 常用 Python 内置模块速用

```python
# 获取当前时间（time）
import time
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# 路径操作（os.path / pathlib）
import os
full_path = os.path.join("/var", "log", "app.log")

# 执行系统命令（subprocess）
import subprocess
output = subprocess.run(["df", "-h"], capture_output=True, text=True).stdout

# 读写文件（with 自动关闭）
with open("output.log", "w") as f:
    f.write("Disk check OK\n")
```

---

## 🔹 系统监控常用技巧（Python 实现）

```python
# 方法1：用 shutil 获取磁盘使用率
import shutil
import psutil
total, used, free = shutil.disk_usage("/")
pct_used = used / total * 100
if pct_used > 80:
    print(f"⚠️ 磁盘使用率: {pct_used:.1f}%")

# 方法2：用 psutil 获取内存使用率
print(psutil.virtual_memory().percent)  # 内存使用百分比
print(psutil.disk_usage('/').percent)  # 根分区使用百分比

# 方法3：HTTP 健康检查（requests）
import requests
try:
    r = requests.get("https://example.com", timeout=5)
    ok = r.status_code == 200
except requests.RequestException:
    ok = False
```

---

## 🔹 Git 基础命令速查

```bash
# 配置身份（首次使用）
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# 初始化仓库
git init

# 查看状态
git status

# 添加文件到暂存区
git add .
git add script.py

# 提交更改
git commit -m "feat: add disk monitor script"

# 查看提交历史
git log --oneline -5

# 连接远程仓库（GitHub）
git remote add origin https://github.com/yourname/sre-90days.git

# 推送到 GitHub（首次）
git push -u origin main

# 后续推送
git push

# 克隆已有项目
git clone https://github.com/yourname/sre-90days.git
```

---

## 🔹 GitHub 工作流最佳实践

```python
# 每次提交前先拉取最新代码（避免冲突）
git pull origin main

# 忽略日志/缓存文件（创建 .gitignore）
echo -e "*.log\n__pycache__/\n.env" > .gitignore

# 查看差异
git diff          # 工作区 vs 暂存区
git diff --staged # 暂存区 vs 最近提交

# 撤销修改（危险！慎用）
git checkout -- file.txt      # 丢弃工作区修改
git reset HEAD file.txt       # 取消暂存
```

---

## 🔹 脚本调试与排错

```python
# 查看 Python 报错堆栈
python3 -u script.py  # -u 强制刷新输出（适合日志跟踪）

# 在脚本中加日志（简单版）
import sys
print("[DEBUG] Disk check starting...", file=sys.stderr)

# 检查依赖是否安装
pip list | grep requests

# 查看 Python 模块路径
python3 -c "import requests; print(requests.__file__)"
```

**✨**  **小技巧** 

```bash
# 1. 快速创建带 shebang 的 Python 脚本
echo '#!/usr/bin/env python3
print("Hello SRE!")' > hello.py
chmod +x hello.py
./hello.py

# 2. 一行运行临时 Python 命令
python3 -c "import shutil; print(shutil.disk_usage('/').percent)"

# 3. Git 别名提速（永久生效）
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
# 之后可用 git st 代替 git status

# 4. 查看本周写了多少行代码（粗略统计）
wc -l *.py
```

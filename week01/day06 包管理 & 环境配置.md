# 📖 Day 6 笔记：软件安装 & 环境变量

---

## ✅ 今日任务完成情况

- [X] 用 apt 安装 vim/curl/tree
- [X] 成功将自定义脚本加入 PATH

---

## 🔧 关键操作记录

```bash
# 安装工具
sudo apt update
sudo apt install -y vim curl tree net-tools

# 创建可全局运行的脚本
mkdir -p ~/bin
echo '#!/bin/bash\necho "My SRE Tool"' > ~/bin/mysre
chmod +x ~/bin/mysre

# 永久加入 PATH
echo 'export PATH=" $ HOME/bin: $ PATH"' >> ~/.bashrc
source ~/.bashrc

# 测试
mysre  # 应输出 "My SRE Tool"
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**修改 ~/.bashrc 后命令仍找不到
  **解决** **：**新终端才加载 .bashrc；当前终端需手动** `source ~/.bashrc`******

---

## 💡 小技巧 / 收获

* **Ubuntu 用** `apt`，CentOS 用 `dnf` **或** `yum`
* `man command` **是最权威帮助**
* **自定义脚本统一放** `~/bin` **是社区惯例**

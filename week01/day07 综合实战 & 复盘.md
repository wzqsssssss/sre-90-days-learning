# 📖 Day 7 笔记：综合练习 & 第1周复盘

---

## ✅ 今日任务完成情况

- [X] 完成“myapp”运维小项目
- [X] 整理本周命令速查表
- [X] 能在 30 分钟内独立复现核心操作

---

## 🔧 关键操作记录

```bash
# 1. 创建目录与用户
sudo mkdir /opt/myapp
sudo useradd -m -s /bin/bash appuser
sudo chown appuser:appuser /opt/myapp
sudo chmod 700 /opt/myapp

# 2. 模拟日志并分析
sudo -u appuser sh -c 'echo "ERROR: disk full at  $ (date)" >> /opt/myapp/app.log'
grep "ERROR" /opt/myapp/app.log

# 3. 监控进程（模拟）
sudo -u appuser sleep 600 &
ps -u appuser
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**普通用户无法写入 /opt/myapp
  **解决** **： `确认 chown 和 chmod 已正确设置（700 = 仅属主可访问）`******

---

## 💡 小技巧 / 收获

* **RE 思维** **：一切操作尽量可脚本化、可复现**
* 本周最大收获：**权限隔离**是安全基石
* **下周重点：Shell 脚本自动化**

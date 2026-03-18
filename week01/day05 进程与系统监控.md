# 📖 Day 5 笔记：进程管理 & 服务控制

---

## ✅ 今日任务完成情况

- [X] 能查看、筛选、终止进程
- [X] 能启停 systemd 服务（如 ssh）

---

## 🔧 关键操作记录

```bash
# 后台运行一个模拟进程
sleep 300 &

# 查找并终止
ps aux | grep sleep
kill %1        # 终止作业1（或用 kill <PID>）

# 管理服务
sudo systemctl status ssh
sudo systemctl stop ssh
sudo systemctl start ssh
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**`systemctl restart ssh` **报错 “Unit ssh.service not found”**
  **解决** **：Ubuntu 中服务名为** `ssh`，但有些系统叫 `sshd`；用 `systemctl list-units | grep ssh` **确认**

---

## 💡 小技巧 / 收获

* `top` **按** `P` **按 CPU 排序，**`M` **按内存排序**
* `htop` **更直观（颜色+树状），推荐安装**
* `kill -9` **是最后手段，优先用** `kill`（发送 SIGTERM）

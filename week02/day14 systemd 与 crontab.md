# 📖 Day 14 笔记：系统服务与定时任务

---

## ✅ 今日任务完成情况

- [X] 创建自定义 systemd 服务
- [X] 设置 crontab 每日自动备份

---

## 🔧 关键操作记录

```bash
# 创建 systemd 服务
sudo tee /etc/systemd/system/mymonitor.service <<EOF
[Unit]
Description=Custom SRE Monitor
After=network.target

[Service]
Type=simple
ExecStart=/home/ubuntu/monitor_service.sh
Restart=on-failure
User=ubuntu

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now mymonitor.service
systemctl status mymonitor

# 设置 crontab
(crontab -l 2>/dev/null; echo "0 2 * * * /home/ubuntu/backup.sh") | crontab -
crontab -l  # 应看到 0 2 * * * ...
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：systemd 服务启动失败，提示“Permission denied”**
  **解决** **：确保脚本有执行权限（**`chmod +x`），且 User 指定正确

---

## 💡 小技巧 / 收获

* **systemd 脚本路径必须是绝对路径**
* **crontab 中 PATH 有限，建议脚本内用全路径（如** `/bin/tar`）
* **测试 cron：可用** `* * * * *` **每分钟运行一次调试**

# 📖 Day 13 笔记：实战：服务监控 & 自动备份

---

## ✅ 今日任务完成情况

- [X] 服务监控脚本（检测+重启+告警）
- [X] 自动备份脚本（带日期命名）

---

## 🔧 关键操作记录

```bash
# monitor_service.sh
#!/bin/bash
SERVICE="nginx"
LOG="/var/log/monitor.log"

if ! systemctl is-active --quiet " $ SERVICE"; then
    echo " $ (date):  $ SERVICE down! Attempting restart..." >> " $ LOG"
    sudo systemctl restart " $ SERVICE"
    if systemctl is-active --quiet " $ SERVICE"; then
        echo " $ (date):  $ SERVICE restarted successfully" >> " $ LOG"
    else
        echo " $ (date): FAILED to restart  $ SERVICE!" >> " $ LOG"
        # 模拟告警：可替换为 mail 或 webhook
    fi
fi

# backup.sh
#!/bin/bash
SRC="/etc"
DEST="/backup"
DATE= $ (date +%Y%m%d)
BACKUP_FILE=" $ DEST/backup_ $ DATE.tar.gz"

mkdir -p " $ DEST"
tar -czf " $ BACKUP_FILE" " $ SRC"
echo "Backup created:  $ BACKUP_FILE"
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：crontab 中脚本找不到命令（如 systemctl）**
  **解决** **：在脚本中使用绝对路径，或在 crontab 开头设置 PATH**

---

## 💡 小技巧 / 收获

* **备份脚本建议加** `set -e` **遇错即停**
* **生产环境备份应验证完整性（如** `tar -tzf file.tar.gz`）

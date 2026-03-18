# 📖 Day 12 笔记：实战：日志自动清理

---

## ✅ 今日任务完成情况

- [X] 编写 log_cleanup.sh，支持传入目录参数
- [X] 删除7天前的 .log 文件
- [X] 记录操作日志到 cleanup.log

---

## 🔧 关键操作记录

```bash
# log_cleanup.sh
#!/bin/bash
LOG_DIR= $ {1:-/var/log}
DAYS=7
LOG_FILE=" $ HOME/cleanup.log"

if [ ! -d " $ LOG_DIR" ]; then
    echo " $ (date): ERROR:  $ LOG_DIR not found" >> " $ LOG_FILE"
    exit 1
fi

echo " $ (date): Cleaning logs older than  $ DAYS days in  $ LOG_DIR" >> " $ LOG_FILE"
find " $ LOG_DIR" -name "*.log" -type f -mtime + $ DAYS -delete -print >> " $ LOG_FILE" 2>&1
echo " $ (date): Cleanup done." >> " $ LOG_FILE"

# 测试
chmod +x log_cleanup.sh
./log_cleanup.sh /tmp/test_logs
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**`find ... -delete` **在某些系统不可用**
  **解决** **：改用** `-exec rm {} \;`，但注意安全**

---

## 💡 小技巧 / 收获

* `find ... -mtime +7` **表示“修改时间超过7天”**
* `-delete` **比** `-exec rm {} \;` **更高效（但需 GNU find）**
* **默认参数技巧：**`${1:-/var/log}`

# 📖 Day 10 笔记：循环：for / while

---

## ✅ 今日任务完成情况

- [X] for 循环统计 /etc/*.conf 数量
- [X] while 循环每5秒检查 nginx 是否运行

---

## 🔧 关键操作记录

```bash
# 统计 .conf 文件
count=0
for conf in /etc/*.conf; do
    if [ -f " $ conf" ]; then
        ((count++))
    fi
done
echo "Found  $ count .conf files in /etc"

# 监控进程 (monitor_nginx.sh)
#!/bin/bash
while true; do
    if pgrep nginx > /dev/null; then
        echo " $ (date): nginx is running"
    else
        echo " $ (date): nginx NOT running!" >&2
    fi
    sleep 5
done
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**变量赋值时写了** `name = "test"`，报错 `command not found`**
  **解决** **：**Shell 中变量赋值**  **不能有空格** **，必须写成** `name="test"`**

---

## 💡 小技巧 / 收获

* `pgrep service_name` **比** `ps aux | grep` **更可靠**
* **用** `> /dev/null` **抑制命令输出**
* **按 Ctrl+C 退出无限循环**

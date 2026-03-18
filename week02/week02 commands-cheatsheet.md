# Week 2 - Shell 脚本与系统自动化速查表

> ✅ 所有命令均在 Ubuntu 24.04 验证
> 💡 使用原则：能复制、能执行、能解决问题

---

## 🔹 Shell 基础语法

```bash
# 变量定义（无空格！）
name="SRE"
echo "Hello, $name"

# 用户输入
read -p "Enter path: " path
echo "You entered: $path"

# 字符串拼接
log_file="app_$(date +%Y%m%d).log"
echo "Log: $log_file"
```

---

## 🔹 条件判断（test / [ ]）

```bash
# 文件/目录判断
[ -f /etc/passwd ] && echo "File exists"
[ -d /opt/app ] || echo "Directory missing"

# 字符串判断
[ -z "$var" ] && echo "Empty variable"
[ "$a" = "$b" ] && echo "Equal"

# 数值比较
count=5
[ $count -gt 3 ] && echo "Count > 3"

# 多条件
[ -f file.txt ] && [ -r file.txt ] && echo "Readable file exists"
```

---

## 🔹 循环结构

```bash
# for 循环遍历文件
for f in /var/log/*.log; do
    [ -f "$f" ] && echo "Processing $f"
done

# for 循环数字
for i in {1..5}; do
    echo "Round $i"
done

# while 循环（常用于监控）
while ! systemctl is-active --quiet nginx; do
    echo "$(date): nginx down, retrying..."
    sleep 5
done
```

---

## 🔹 函数与参数

```bash
# 定义函数
check_disk() {
    local usage=$(df / | awk 'NR==2 {print $5}' | tr -d '%')
    if [ $usage -gt 90 ]; then
        echo "⚠️ Disk usage: ${usage}%"
    fi
}

# 调用
check_disk

# 获取参数
echo "Script: $0"
echo "First arg: $1"
echo "Number of args: $#"
```

---

## 🔹 实用脚本技巧

```bash
# 安全删除（避免 rm -rf /*）
rm_safe() {
    [ -n "$1" ] && [ "$1" != "/" ] && rm -rf "$1"
}

# 日志记录
LOG="/var/log/myscript.log"
echo "$(date): Task started" >> "$LOG"

# 退出码处理
mycmd || { echo "Failed!"; exit 1; }

# 设置严格模式（推荐加到脚本开头）
set -euo pipefail
```

---

## 🔹 systemd 服务管理

```bash
# 创建服务（路径必须绝对！）
sudo tee /etc/systemd/system/myjob.service <<EOF
[Unit]
Description=My Custom Job
After=network.target

[Service]
ExecStart=/home/ubuntu/myscript.sh
Restart=on-failure
User=ubuntu

[Install]
WantedBy=multi-user.target
EOF

# 启用服务
sudo systemctl daemon-reload
sudo systemctl enable --now myjob
systemctl status myjob
journalctl -u myjob -f   # 查看日志
```

---

## 🔹 crontab 定时任务

```bash
# 编辑当前用户 cron
crontab -e

# 示例：每天凌晨2点备份
0 2 * * * /home/ubuntu/backup.sh >> /var/log/backup.log 2>&1

# 每5分钟运行一次（调试用）
*/5 * * * * /home/ubuntu/check.sh

# 列出任务
crontab -l

# ⚠️ 注意：cron 中 PATH 有限！建议脚本内用全路径：
# /usr/bin/tar, /usr/bin/find, /bin/bash 等
```

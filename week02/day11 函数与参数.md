# 📖 Day 11 笔记：函数定义与参数传递

---

## ✅ 今日任务完成情况

- [X] 编写函数检查服务状态和重启服务
- [X] 脚本能接收位置参数（$1, $2）

---

## 🔧 关键操作记录

```bash
# service_utils.sh
#!/bin/bash

check_service() {
    local svc=$1
    if systemctl is-active --quiet " $ svc"; then
        echo " $ svc is active"
        return 0
    else
        echo " $ svc is NOT active"
        return 1
    fi
}

restart_service() {
    local svc=$1
    echo "Restarting  $ svc..."
    sudo systemctl restart " $ svc"
}

# 主逻辑
if [  $ # -eq 0 ]; then
    echo "Usage: $0 <service_name>"
    exit 1
fi

SERVICE=$1
check_service " $ SERVICE" || restart_service " $ SERVICE"
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：函数内变量污染全局**
  **解决** **：用** `local` **声明局部变量**

---

## 💡 小技巧 / 收获

* **函数内用** `local` **声明变量避免污染全局**
* `systemctl is-active --quiet` **返回状态码，适合 if 判断**

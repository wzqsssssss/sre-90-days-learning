# 📖 Day 3 笔记：权限模型 & 用户/组管理

---

## ✅ 今日任务完成情况

- [X] 理解 rwx 对 user/group/other 的含义
- [X] 成功创建用户、设置权限、验证隔离

---

## 🔧 关键操作记录

```bash
# 创建用户
sudo useradd -m appuser
sudo passwd appuser  # 设密码为 app123

# 创建受限目录
sudo mkdir /opt/myapp
sudo chown appuser:appuser /opt/myapp
sudo chmod 700 /opt/myapp

# 切换用户测试
su - appuser
touch /opt/myapp/test.txt  # 应成功
exit

# 验证 root 外其他用户无法访问
sudo -u nobody touch /opt/myapp/fail.txt  # 应失败
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **： **`su - appuser` **提示 “This account is currently not available”******
  **解决** **：****默认 shell 是** `/sbin/nologin`，需指定：****

  ```bash
  sudo usermod -s /bin/bash appuser
  ```

---

## 💡 小技巧 / 收获

* `chmod 755` **=** `rwxr-xr-x`
* `chown user:group file` **可同时改属主和属组**
* **普通用户默认不能 kill 其他用户的进程（安全机制）**

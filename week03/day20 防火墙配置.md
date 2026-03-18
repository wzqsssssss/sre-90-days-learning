# 📖 Day 20 笔记：防火墙：ufw / firewalld

---

## ✅ 今日任务完成情况

- [X] Ubuntu 用 ufw 开放 SSH
- [X] CentOS 用 firewall-cmd 开放 HTTP

---

## 🔧 关键操作记录

```bash
# Ubuntu (ufw)
sudo ufw allow 22/tcp
sudo ufw enable
sudo ufw status verbose

# CentOS (firewalld)
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
firewall-cmd --list-all
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：开放端口后仍无法访问**
  **解决** **：确认服务（如 nginx）正在监听 0.0.0.0:80，而非 127.0.0.1:80**

---

## 💡 小技巧 / 收获

* **永远先允许 SSH，再启用防火墙，否则可能被锁在 VM 外！**
* `--permanent` **表示重启后仍生效**

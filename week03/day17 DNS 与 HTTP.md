# 📖 Day 17 笔记：DNS 查询 & HTTP 基础

---

## ✅ 今日任务完成情况

- [X] 用 dig 查询 A/MX 记录
- [X] 用 curl 获取网页并解释状态码
- [X] 修改 /etc/hosts 实现本地解析

---

## 🔧 关键操作记录

```bash
# DNS 查询
dig example.com A +short
dig gmail.com MX +short

# HTTP 请求
curl -I https://httpbin.org/status/200
curl -I https://httpbin.org/status/404

# 本地 hosts
echo "127.0.0.1 mysite.local" | sudo tee -a /etc/hosts
ping mysite.local  # 应解析到 127.0.0.1
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：修改 /etc/hosts 后浏览器仍打不开**
  **解决** **：清除 DNS 缓存（Linux 一般无需，但可重启 nscd 或用** `systemd-resolve --flush-caches`）

---

## 💡 小技巧 / 收获

* **常见状态码：200（OK）、404（Not Found）、500（Server Error）**
* `curl -v` **查看完整请求/响应头**

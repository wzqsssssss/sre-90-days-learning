# 📖 Day 18 笔记：网络排查实战

---

## ✅ 今日任务完成情况

- [X] ping / traceroute / ss / nc 全部成功使用

---

## 🔧 关键操作记录

```bash
ping -c 4 baidu.com
traceroute google.com          # Ubuntu
# 或
mtr google.com                 # 更强大

ss -tuln                       # 查看监听端口
nc -zv 127.0.0.1 22            # 测试 SSH 端口通不通
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：traceroute 显示 * * ***
  **解决** **：中间路由器可能禁 ICMP，属正常现象；可改用** `mtr` **或** `tcptraceroute`

---

## 💡 小技巧 / 收获

* **若 ping 不通但能上网，可能是 ICMP 被禁（正常）**
* `nc -zv` **是测试端口连通性的黄金命令**
* **安装工具：**`sudo apt install -y dnsutils traceroute netcat-openbsd mtr`

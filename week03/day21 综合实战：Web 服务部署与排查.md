# 📖 Day 21 笔记：综合练习：部署 Nginx 并排查

---

## ✅ 今日任务完成情况

- [X] 安装 nginx，修改首页
- [X] 配置静态 IP + 防火墙放行 80
- [X] 从宿主机访问成功
- [X] 故意制造故障并定位

---

## 🔧 关键操作记录

```bash
# 安装并修改首页
sudo apt install -y nginx
echo "<h1>SRE Day21 OK</h1>" | sudo tee /var/www/html/index.html

# 验证本地
curl http://localhost

# 从宿主机浏览器访问 http://192.168.56.10

# 故障模拟
sudo systemctl stop nginx          # 页面无法访问 → systemctl status
sudo ufw deny 80/tcp               # 连接超时 → ufw status
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：nginx 启动失败，提示 address already in use**
  **解决** **：**`sudo ss -tulnp | grep :80` **查看占用进程，kill 或换端口**

---

## 💡 小技巧 / 收获

* **排查顺序：1) 服务是否运行？2) 端口是否监听？3) 防火墙是否放行？4) 路由/网络是否通？**

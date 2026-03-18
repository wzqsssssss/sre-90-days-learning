# Week 3 - 网络原理与排查速查表

> ✅ 所有命令均在 Ubuntu 24.04 验证
> 💡 使用原则：能复制、能执行、能解决问题

---

## 🔹 **IP 与路由**

```bash
# 查看 IP（替代 ifconfig）
ip a
ip addr show eth0

# 查看路由表
ip route
ip route show default

# 临时设置 IP（重启失效）
sudo ip addr add 192.168.56.10/24 dev enp0s3
sudo ip route add default via 192.168.56.1
```

---

## 🔹 网络诊断工具

```bash
# 连通性测试
ping -c 4 8.8.8.8

# 路径追踪
traceroute google.com
mtr google.com          # 实时动态版（需安装）

# 查看监听端口
ss -tuln                # 推荐（比 netstat 快）
netstat -tuln           # 传统方式

# 测试端口连通性
nc -zv 127.0.0.1 22     # SSH
nc -zv example.com 443  # HTTPS

# 查看 DNS 解析
nslookup google.com
dig google.com A +short
```

---

## 🔹 HTTP 与 Web 调试

```bash
# 发送 GET 请求
curl https://httpbin.org/get

# 查看响应头
curl -I https://example.com

# POST 数据
curl -X POST -d "name=test" https://httpbin.org/post

# 下载文件
wget https://example.com/file.tar.gz
```

---

## 🔹 防火墙（ufw - Ubuntu）

```bash
# 允许端口
sudo ufw allow 22/tcp
sudo ufw allow 80,443/tcp

# 拒绝端口
sudo ufw deny 3389

# 启用/禁用
sudo ufw enable
sudo ufw disable

# 查看状态
sudo ufw status verbose
sudo ufw status numbered  # 带编号，方便删除
```

---

## 🔹 CentOS 7/8/9 常用命令

```bash
# 防火墙（firewalld）
sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --reload
firewall-cmd --list-all

# 网络配置（传统）
sudo vi /etc/sysconfig/network-scripts/ifcfg-eth0
# 设置 BOOTPROTO=static, IPADDR=..., GATEWAY=...

# 包管理
sudo dnf install -y bind-utils net-tools traceroute
```

---

## 🔹 静态 IP 配置（Netplan - Ubuntu 24.04+

```yml
# /etc/netplan/00-config.yaml
network:
  version: 2
  ethernets:
    enp0s3:
      dhcp4: no
      addresses: [192.168.56.10/24]
      routes:
        - to: default
          via: 192.168.56.1
      nameservers:
          addresses: [8.8.8.8, 114.114.114.114]
```

```bash
sudo netplan apply
ip a    # 验证
```

---

## 🔹 故障排查流程图

```bash
无法访问 Web 服务？
│
├─ 1. 本地 curl http://localhost → ❌ → 服务没启动（systemctl status）
│
├─ 2. ss -tuln | grep :80 → ❌ → 服务未监听（检查配置）
│
├─ 3. 本地 curl OK，但远程不行 → 防火墙问题（ufw/firewalld）
│
└─ 4. 防火墙 OK → 网络不通（ping → traceroute → 路由/安全组）
```

**✨**  **小技巧** **：**一键网络健康检查脚本****

```bash
#!/bin/bash
echo "=== Network Check ==="
ping -c 2 8.8.8.8 || echo "❌ No Internet"
ss -ltn | grep :80 || echo "❌ Port 80 not listening"
sudo ufw status | grep -q "80.*ALLOW" || echo "❌ Firewall blocking 80"
curl -s --max-time 3 http://localhost && echo "✅ Local web OK"
```

# 📖 Day 19 笔记：手动配置静态 IP

---

## ✅ 今日任务完成情况

- [X] Ubuntu/CentOS 成功设为静态 IP（如 192.168.56.10/24）

---

## 🔧 关键操作记录

```yaml
# /etc/netplan/01-netcfg.yaml
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
ip a
ip route show
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：配置后无法上网**
  **解决** **：检查网关是否在同一子网，DNS 是否可解析**

---

## 💡 小技巧 / 收获

* **先用** `ip a` **确认网卡名（enp0s3 / eth0）**
* **VirtualBox Host-Only 网络常用 192.168.56.0/24**

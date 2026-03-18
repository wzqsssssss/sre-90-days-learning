# 📖 Day 1 笔记：虚拟机安装 & 终端

---

## ✅ 今日任务完成情况

- [X] 安装 VMware 并创建 Ubuntu 虚拟机
- [X] 配置 NAT 网络，能 ping 通外网

---

## 🔧 关键操作记录

```bash
# 测试网络连通性
ping -c 4 bing.com

# 查看 IP 地址
ip a
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：VMware 虚拟机无法联网**
  **解决** **：设置 → 网络 → 连接方式选 “NAT”，重启虚拟机后正常**
* 虚拟机，nat ip设定范围应该与主机静态ip错开，否则会出现虚拟机内部连不上网的情况

---

## 💡 小技巧 / 收获

* **Ubuntu 快捷键：**`Ctrl+Alt+T` **打开终端**
* **首次登录建议更新系统：**

```bash
sudo apt update && sudo apt upgrade -y
```

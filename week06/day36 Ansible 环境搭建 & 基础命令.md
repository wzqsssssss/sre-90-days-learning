# 📖 Day 36 笔记：Ansible 环境搭建 & 基础命令

---

## ✅ 今日任务完成情况

- [X] 在控制机（Ubuntu）安装 Ansible
- [X] 配置 SSH 免密登录到目标主机（localhost 或另一台 VM）
- [X] `编写 INI 格式 Inventory 文件并测试连通性`
- [X] **成功运行** `ansible all -m ping`

---

## 🔧 关键操作记录

```bash
# 安装 Ansible（Ubuntu）
sudo apt update
sudo apt install ansible -y

# 生成 SSH 密钥（若无）
ssh-keygen -t rsa -b 2048

# 复制公钥到目标主机（如本机）
ssh-copy-id localhost

# 测试免密登录
ssh localhost

# 创建 inventory.ini
echo "[local]\nlocalhost ansible_connection=local" > inventory.ini

# 测试 Ansible 连通性
ansible all -i inventory.ini -m ping
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**`ansible: command not found`
  **解决** **：确认是否用** `python` **安装，或改用** `pipx install ansible`（某些 Ubuntu 版本 apt 源较旧）
* **问题** **：**`ping` **模块返回** `UNREACHABLE!`
  **解决** **：检查** `inventory.ini` **中是否指定** `ansible_connection=local`（对 localhost 必须加）

---

## 💡 小技巧 / 收获

* **Ansible 默认使用 `/etc/ansible/hosts` **作为 inventory**** **，但推荐用** `-i` **指定自定义文件**
* **ad-hoc 命令格式** **：**`ansible <group> -i <inventory> -m <module> -a "<args>"`
* **常用模块速记** **：**
* `ping`：测试连接
* `command`：执行命令（不支持 shell 特性）
* `shell`：执行 shell 命令（支持管道、重定向等）

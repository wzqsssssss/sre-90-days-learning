# Week 6 - Ansible 命令速查表

> ✅ 所有命令均在 Ubuntu 24.04 验证 + Python 3.12.3 验证
> 💡 使用原则：能复制、能执行、能解决问题

---

## 🔹 安装与环境检查

```bash
# 安装 Ansible（推荐使用 pip3 获取最新版）
sudo apt update && sudo apt install python3-pip -y
pip3 install --user ansible

# 验证安装
ansible --version

# 检查控制机是否能免密登录目标机
ssh user@target_host

# 测试 Ansible 连通性（使用 ping 模块）
ansible all -i inventory.ini -m ping
```

---

## 🔹 Inventory（主机清单）常用写法

```ini
# inventory.ini 示例（INI 格式）
[webservers]
web1 ansible_host=192.168.1.10
web2 ansible_host=192.168.1.11

[databases]
db1 ansible_host=192.168.1.20

[prod:children]
webservers
databases

# 本地回环（无需 SSH）
localhost ansible_connection=local
```

```yml
# inventory.yaml 示例（YAML 格式）
all:
  children:
    webservers:
      hosts:
        web1:
          ansible_host: 192.168.1.10
    databases:
      hosts:
        db1:
          ansible_host: 192.168.1.20
```

---

## 🔹 Ad-hoc 命令（快速执行）

```bash
# 在所有主机执行命令
ansible all -i inventory.ini -a "uptime"

# 使用 shell 模块（支持管道、重定向）
ansible webservers -i inventory.ini -m shell -a "df -h | grep /dev/sda1"

# 复制文件到远程
ansible webservers -i inventory.ini -m copy -a "src=./app.conf dest=/etc/app.conf"

# 安装软件包（自动识别系统）
ansible webservers -i inventory.ini -m package -a "name=nginx state=present"

# 重启服务
ansible webservers -i inventory.ini -m service -a "name=nginx state=restarted"
```

---

## 🔹 Playbook 常用命令

```bash
# 正常运行
ansible-playbook -i inventory.ini site.yml

# 显示详细输出（-v 到 -vvvv）
ansible-playbook -i inventory.ini site.yml -v

# Dry-run（只检查，不执行）
ansible-playbook -i inventory.ini site.yml --check

# 只运行特定 tag
ansible-playbook -i inventory.ini site.yml --tags "deploy"

# 跳过某些 tag
ansible-playbook -i inventory.ini site.yml --skip-tags "debug"

# 限制只对某台主机运行
ansible-playbook -i inventory.ini site.yml --limit web1
```

---

## 🔹 变量与 Facts

```bash
# 查看某主机的所有 facts（自动收集的系统信息）
ansible web1 -i inventory.ini -m setup

# 查看特定 fact
ansible web1 -i inventory.ini -m setup -a "filter=ansible_os_family"

# 常用 facts 示例：
# ansible_distribution → Ubuntu
# ansible_architecture → x86_64
# ansible_default_ipv4.address → 主 IP
```

---

## 🔹 Vault（敏感信息加密）

```bash
# 创建加密文件
ansible-vault create group_vars/webservers/vault.yml

# 编辑加密文件
ansible-vault edit group_vars/webservers/vault.yml

# 查看加密文件内容
ansible-vault view group_vars/webservers/vault.yml

# 运行 Playbook 时输入密码
ansible-playbook -i inventory.ini site.yml --ask-vault-pass

# 使用 vault 密码文件（仅用于自动化，注意权限！）
echo "mysecretpassword" > .vault_pass
chmod 600 .vault_pass
ansible-playbook -i inventory.ini site.yml --vault-password-file .vault_pass
```

---

## 🔹 Roles 与项目结构

```bash
# 创建新 Role
ansible-galaxy init roles/nginx

# 推荐项目结构
my_project/
├── inventory.ini
├── site.yml
├── group_vars/
│   └── webservers/
│       ├── vars.yml
│       └── vault.yml   # (encrypted)
└── roles/
    └── nginx/
        ├── tasks/
        ├── handlers/
        ├── templates/
        ├── defaults/
        └── files/
```

```yml
# site.yml 调用 Role 示例
---
- name: Deploy web stack
  hosts: webservers
  become: yes
  roles:
    - nginx
    - flask_app
```

---

## 🔹 脚本调试与排错

```yml
# 在 Playbook 中打印变量
- debug:
    var: ansible_distribution

- debug:
    msg: "Port is {{ app_port }}"
```

```bash
# 临时关闭 host key checking（测试环境可用）
export ANSIBLE_HOST_KEY_CHECKING=False

# 查看模块文档（离线）
ansible-doc copy
ansible-doc template
```

**✨**  **小技巧**

```bash
# 快速生成 SSH 免密（控制机 → 目标机）
ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
ssh-copy-id user@target_host

# 把常用选项写入 ansible.cfg（放在项目根目录）
echo "[defaults]
inventory = inventory.ini
host_key_checking = False
retry_files_enabled = False" > ansible.cfg
```

```bash
# 别名加速（加到 ~/.bashrc）
echo "alias apb='ansible-playbook -i inventory.ini'" >> ~/.bashrc
source ~/.bashrc
# 之后只需：apb site.yml
```

1. **幂等性** **：重复运行结果一致**
2. **声明式** **：描述“要什么”，不是“怎么做”**
3. **无代理** **：靠 SSH 即可管理，无需在目标机装软件**

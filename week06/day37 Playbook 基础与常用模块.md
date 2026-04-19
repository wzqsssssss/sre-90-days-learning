# 📖 Day 37 笔记：Playbook 基础与常用模块

---

## ✅ 今日任务完成情况

- [X] 编写第一个 Playbook（部署 Nginx）
- [X] `使用 package、copy、service 等模块`
- [X] `成功在目标主机显示自定义首页`
- [X] **使用** `--check` **模式进行 dry-run 测试**

---

## 🔧 关键操作记录

```yml
# site.yml
---
- name: Deploy Nginx with custom page
  hosts: local
  become: yes
  tasks:
    - name: Install nginx
      package:
        name: nginx
        state: present

    - name: Start and enable nginx
      service:
        name: nginx
        state: started
        enabled: yes

    - name: Deploy custom index.html
      copy:
        content: "<h1>Hello from Ansible! 🚀</h1>"
        dest: /var/www/html/index.html
```

```bash
# 运行 Playbook
ansible-playbook -i inventory.ini site.yml

# Dry-run 模式（不实际执行）
ansible-playbook -i inventory.ini site.yml --check
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**`Failed to start nginx.service: Unit nginx.service not found`
  **解决** **：确认系统是否已安装 nginx（Ubuntu 用** `apt`，CentOS 用 `yum/dnf`）
* **问题** **：**`copy` **模块权限不足**
  **解决** **：Playbook 中添加** `become: yes` **获取 root 权限**

---

## 💡 小技巧 / 收获

* **`become: yes` **= sudo**** **，几乎所有系统配置都需要它**
* **幂等性** **：重复运行 Playbook 不会重复安装或报错（Ansible 的核心优势）**
* **查看详细输出** **：加** `-v`、`-vv` **参数（最多** `-vvvv`）

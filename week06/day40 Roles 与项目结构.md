# 📖 Day 40 笔记：Roles 与项目结构

---

## ✅ 今日任务完成情况

- [X] **使用** `ansible-galaxy init nginx_role` **创建 Role**
- [X] 将 Day 37–38 的任务拆分到 Role 的各子目录
- [X] 编写 `site.yml` **调用 Role**
- [X] **通过修改** `defaults/main.yml` **快速切换配置**

---

## 🔧 关键操作记录

```bash
# 创建 Role
ansible-galaxy init roles/nginx_role
```

```yml
# roles/nginx_role/defaults/main.yml
nginx_port: 80

# roles/nginx_role/tasks/main.yml
- name: Install nginx
  package:
    name: nginx
    state: present
- name: Deploy config
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/sites-available/default
  notify: Reload nginx

# site.yml
---
- name: Deploy web server
  hosts: local
  become: yes
  roles:
    - nginx_role
```

```bash
# 运行
ansible-playbook -i inventory.ini site.yml
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：Role 中的 handler 未生效**
  **解决** **：确保** `handlers/main.yml` **存在，且在主 Playbook 或 Role 中被加载**
* **问题** **：模板找不到**
  **解决** **：模板必须放在** `roles/<role>/templates/` **下**

---

## 💡 小技巧 / 收获

* **Role 目录结构是 Ansible 最佳实践** **，便于复用和分享**
* **优先级** **：**`vars/` **>** `defaults/`（defaults 可被外部覆盖）
* **多个 Role 可在同一个 Playbook 中调用**

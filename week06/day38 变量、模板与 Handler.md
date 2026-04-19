# 📖 Day 38 笔记：变量、模板与 Handler

---

## ✅ 今日任务完成情况

- [X] 在 Playbook 中定义变量（**`vars`）**
- [X] `创建 Jinja2 模板（.j2）生成 Nginx 配置`
- [X] `使用 notify + handlers 实现配置变更后 reload`
- [X] 验证修改端口后服务自动重载

---

## 🔧 关键操作记录

```yml
# templates/nginx.conf.j2
server {
    listen {{ nginx_port }};
    server_name localhost;
    location / {
        root /var/www/html;
        index index.html;
    }
}
```

```yml
# site.yml（节选）
vars:
  nginx_port: 8080

tasks:
  - name: Deploy Nginx config from template
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/sites-available/default
    notify: Reload nginx

handlers:
  - name: Reload nginx
    service:
      name: nginx
      state: reloaded
```

```bash
# 修改端口后重新运行
ansible-playbook -i inventory.ini site.yml
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：Handler 没有触发**
  **解决** **：确保 task 状态为 “changed”（若配置未变，不会触发 reload）**
* **问题** **：Nginx 配置语法错误导致 reload 失败**
  **解决** **：先用** `nginx -t` **手动测试配置，或在 Playbook 中加验证 task**

---

## 💡 小技巧 / 收获

* **Handler 只在被 `notify` **且 task 状态为 changed 时执行****
* **模板路径默认在 `templates/` **目录下（相对于 Playbook）****
* **变量优先级** **：命令行 > playbook vars > group_vars > defaults（Role 中）**

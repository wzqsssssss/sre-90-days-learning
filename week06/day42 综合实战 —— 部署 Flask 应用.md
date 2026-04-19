# 📖 Day 42 笔记：综合实战 —— 部署 Flask 应用

---

## ✅ 今日任务完成情况

- [X] **创建** `flask_app` **Role**
- [X] **安装 Python、pip、systemd 服务**
- [X] 用 template 生成 systemd unit 和 app.py
- [X] 配置 Nginx 反向代理
- [X] 敏感信息（如 SECRET_KEY）用 vault 加密
- [X] 全流程一键部署成功

---

## 🔧 关键操作记录

```yml
# roles/flask_app/defaults/main.yml
app_user: flaskuser
app_port: 5000
secret_key: "change-in-vault"
```

```ini
# group_vars/local/vault.yml（加密）
secret_key: "super-secret-key-123!"
```

```yml
# templates/app.service.j2
[Unit]
Description=Flask App
After=network.target

[Service]
User={{ app_user }}
WorkingDirectory=/opt/flask_app
ExecStart=/usr/bin/python3 app.py
Environment=FLASK_APP=app.py
Environment=SECRET_KEY={{ secret_key }}

[Install]
WantedBy=multi-user.target
```

```bash
# 最终部署
ansible-playbook -i inventory.ini site.yml --ask-vault-pass
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：systemd 服务启动失败，日志无输出**
  **解决** **：用** `journalctl -u flask_app` **查看日志；确保** `/opt/flask_app/app.py` **有可执行权限**
* **问题** **：Nginx 502 Bad Gateway**
  **解决** **：确认 Flask 应用监听** `0.0.0.0:5000`（而非 `127.0.0.1`）

---

## 💡 小技巧 / 收获

* **完整项目结构建议** **：**
  ```文本
  ansible-flask/
  ├── inventory.ini
  ├── site.yml
  ├── group_vars/
  │   └── local/
  │       └── vault.yml (encrypted)
  └── roles/
      └── flask_app/
          ├── defaults/
          ├── tasks/
          ├── templates/
          └── handlers/
  ```

* **幂等性验证** **：连续运行两次 Playbook，第二次应全部 “ok”，无 “changed”**

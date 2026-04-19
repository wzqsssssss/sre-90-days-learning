# 📖 Day 41 笔记：安全与进阶功能

---

## ✅ 今日任务完成情况

- [X] **使用** `ansible-vault create` **加密敏感变量文件**
- [X] `在 Playbook 中引用 vault 加密变量`
- [X] 使用 `delegate_to: localhost` **发送本地通知**
- [X] **拆分 tasks 为多个文件并用** `include_tasks` **引入**

---

## 🔧 关键操作记录

```bash
# 创建加密变量文件
ansible-vault create group_vars/local/vault.yml
# 输入密码，写入内容如：
# db_password: mysecretpass123
```

```yml
# site.yml
vars_files:
  - group_vars/local/vault.yml

tasks:
  - name: Show secret (for demo)
    debug:
      msg: "DB password is {{ db_password }}"
```

```bash
# 运行时提供 vault 密码
ansible-playbook -i inventory.ini site.yml --ask-vault-pass

# 或用 vault 密码文件（不推荐明文存密码）
ansible-playbook -i inventory.ini site.yml --vault-password-file .vault_pass
```

```yml
# 委托任务示例
- name: Notify deployment complete
  shell: echo "Deployed at $(date)" >> /tmp/deploy.log
  delegate_to: localhost
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：忘记 vault 密码**
  **解决** **：无法恢复！务必妥善保管密码或使用 vault ID + 多密码文件（Ansible 2.4+）**
* **问题** **：**`delegate_to` **仍尝试 SSH 到 localhost**
  **解决** **：加上** `connection: local` **更稳妥**

---

## 💡 小技巧 / 收获

* **千万不要把明文密码提交到 Git** **！用 vault 或 CI/CD secrets**
* **`--ask-vault-pass` **比密码文件更安全（交互式输入）****
* **`include_tasks` **动态引入，**`import_tasks` **静态解析****

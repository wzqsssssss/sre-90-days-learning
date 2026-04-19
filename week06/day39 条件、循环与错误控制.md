# 📖 Day 39 笔记：条件、循环与错误控制

---

## ✅ 今日任务完成情况

- [X] `使用 when 根据操作系统选择包管理器`
- [X] **用** `loop` **批量创建用户**
- [X] **尝试** `ignore_errors` **和** `block/rescue`
- [X] 验证不同系统下 Playbook 行为正确

---

## 🔧 关键操作记录

```yml
- name: Install package based on OS
  package:
    name: "{{ 'httpd' if ansible_os_family == 'RedHat' else 'nginx' }}"
    state: present
  when: ansible_os_family in ['Debian', 'RedHat']

- name: Create multiple users
  user:
    name: "{{ item }}"
    state: present
  loop:
    - dev1
    - dev2
    - tester

- name: Risky task (may fail)
  command: /bin/false
  ignore_errors: yes

- name: Safe block with rescue
  block:
    - name: Try something dangerous
      command: ls /nonexistent
  rescue:
    - name: Handle failure
      debug:
        msg: "Task failed, but we caught it!"
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**`ansible_os_family` **未定义**
  **解决** **：先运行** `setup` **模块收集 facts：**`ansible <host> -m setup`
* **问题** **：**`loop` **中变量名冲突**
  **解决** **：避免在 loop 内使用** `item` **以外的嵌套结构，或改用** `loop_control`

---

## 💡 小技巧 / 收获

* **Facts 是 Ansible 自动收集的主机信息** **（如 IP、OS、内核等），可在 Playbook 中直接用**
* **`ansible_distribution` **vs** `ansible_os_family`** **：**
* `Ubuntu` **→** `Debian`
* `CentOS` **→** `RedHat`
* **`rescue` **类似 try-catch，适合做清理或通知****

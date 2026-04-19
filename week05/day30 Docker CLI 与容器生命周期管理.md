# 📖 Day 30 笔记：Docker CLI 与容器生命周期管理

---

## ✅ 今日任务完成情况

- [X] **编写** `hello.py` **脚本并在容器中运行**
- [X] `使用 -v 挂载本地目录`
- [X] 掌 `握 logs、exec、inspect 等调试命令`
- [X] 创建并验证命名卷（volume）持久化

---

## 🔧 关键操作记录

```bash
# 后台运行带挂载的脚本
docker run -d --name my-script -v $(pwd):/app python:3.12-slim python /app/hello.py

# 查看日志
docker logs my-script

# 进入容器
docker exec -it my-script bash

# 查看容器元数据（IP、挂载点等）
docker inspect my-script

# 创建并使用 volume
docker volume create mydata
docker run -v mydata:/data alpine touch /data/test.txt
docker run -v mydata:/data alpine ls /data
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**Windows PowerShell 中** `$(pwd)` **报错****
  **解决** **：** `改用 ${PWD} 或绝对路径，例如：`

  ```
  docker run -v ${PWD}:/app ...
  ```
* **问题** **：容器内看不到挂载文件**
  **解决** **：确认宿主机路径存在，且容器内目标目录为空（非覆盖已有目录）**

---

## 💡 小技巧 / 收获

* **`-it` **= interactive + TTY**** **：用于交互式会话（如 bash）**
* **`-d` **= detached**** **：后台运行**
* **SRE 调试三件套** **：**`logs` **→** `exec` **→** `inspect`

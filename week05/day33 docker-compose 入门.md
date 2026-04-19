# 📖 Day 33 笔记：docker-compose 入门

---

## ✅ 今日任务完成情况

- [X] **编写** `docker-compose.yml`
- [X] **使用** `docker compose up -d` **启动服务**
- [X] **验证服务可访问，日志可查看**

---

## 🔧 关键操作记录

```yml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    restart: unless-stopped
```

```python
# 启动 & 查看日志
docker compose up -d
docker compose logs -f web

# 停止
docker compose down
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：** **`docker-compose` **命令未找到****
  **解决** **：**Docker Desktop 已内置** `docker compose`（注意无短横线），使用新语法**

---

## 💡 小技巧 / 收获

* **`restart` **策略**** **：**
* `no`：默认，不重启
* `on-failure`：仅失败时重启
* `unless-stopped`：始终重启，除非手动停止（推荐生产使用）

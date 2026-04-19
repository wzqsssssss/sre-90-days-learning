# 📖 Day 34 笔记：多服务编排 or 定时任务

---

## ✅ 今日任务完成情况

- [X] Web + Redis 多服务通信成功
- [X] `监控脚本可通过 cron 或容器定期执行`

---

## 🔧 关键操作记录

```yml
# docker-compose.yml 片段
services:
  web:
    build: .
    environment:
      - REDIS_HOST=redis
    depends_on:
      - redis
  redis:
    image: redis:7-alpine
```

```python
# app.py 中连接 Redis
import redis
r = redis.Redis(host='redis', port=6379)
r.incr('hits')
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** ：**容器间无法通过服务名解析**
  **解决** **：**确保在同一** `docker-compose.yml` **中定义，Docker 会自动创建内部 DNS。****

---

## 💡 小技巧 / 收获

* **服务名 = DNS 名** **：在 Compose 网络中，**`redis` **会自动解析为 Redis 容器 IP。**
* **`depends_on` **不等待服务就绪**** **：它只控制启动顺序，不保证服务已 ready（需应用自己重试连接）。**

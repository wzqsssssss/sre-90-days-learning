# 📖 Day 32 笔记：Dockerfile 安全与优化

---

## ✅ 今日任务完成情况

- [X] `在 Dockerfile 中添加非 root 用户`
- [X] 对比优化前后镜像大小
- [X] 尝试多阶段构建

---

## 🔧 关键操作记录

```bash
# 添加非 root 用户
RUN addgroup --system app && adduser --system --ingroup app app
USER app
```

```python
# 查看镜像大小
docker images

# 验证容器用户
docker run --rm my-app id
# 应输出 uid=... app gid=... app
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：** `非 root 用户无权限写日志目录`
  **解决** **：** `在 Dockerfile 中提前创建目录并赋权：`

  ```bash
  RUN mkdir -p /app/logs && chown -R app:app /app/logs
  ```

---

## 💡 小技巧 / 收获

* **安全基线** **：生产容器禁止以 root 运行！**
* **镜像体积目标** **：简单 Python 应用 ≤ 150MB（slim 镜像 + 清理缓存）**

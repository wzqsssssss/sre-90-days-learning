# 📖 Day 31 笔记：编写 Dockerfile 容器化 Python 应用

---

## ✅ 今日任务完成情况

- [X] **创建 Flask Web 应用（或使用现有监控脚本）**
- [X] `编写 .dockerignore`
- [X] `编写符合最佳实践的 Dockerfile`
- [X] 成功构建镜像并访问服务

---

## 🔧 关键操作记录

```bash
# Dockerfile 示例
FROM python:3.12-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]
```

```bash
# 构建 & 运行
docker build -t my-app .
docker run -d --name web -p 8000:8000 my-app

# 验证
curl http://localhost:8000
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**Flask 默认只监听** `127.0.0.1`，容器外无法访问**
  **解决** **：**`启动时绑定 host='0.0.0.0'：`

  ```python
  app.run(host='0.0.0.0', port=8000)
  ```

* **问题** **：Python 日志不实时输出**
  **解决** **：设置** `PYTHONUNBUFFERED=1`（已在 Dockerfile 中处理）

---

## 💡 小技巧 / 收获

* **层缓存优化** **：先** `COPY requirements.txt` **再** `RUN pip install`，避免代码变更导致重装依赖。
* **`.dockerignore` **必须有**** **：防止** `__pycache__`、`.git` **等无用文件进镜像。**

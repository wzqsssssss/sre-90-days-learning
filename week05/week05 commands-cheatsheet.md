# Week 5 - Docker 命令速查表

> ✅ 所有命令均在 Ubuntu 24.04 验证 + Python 3.12.3 验证
> 💡 使用原则：能复制、能执行、能解决问题

---

## 🔹 镜像（Image）管理

```bash
docker images                     # 列出本地镜像
docker pull python:3.11-slim      # 拉取镜像
docker build -t my-app .          # 从当前目录构建镜像（需 Dockerfile）
docker rmi <image-id>             # 删除镜像
docker rmi $(docker images -q)    # 删除所有未使用的镜像（慎用！）
docker save -o my-app.tar my-app  # 导出镜像为 tar
docker load -i my-app.tar         # 从 tar 加载镜像
```

---

## 🔹 容器（Container）生命周期

```bash
docker run -d --name web -p 8000:8000 my-app        # 后台运行容器
docker run -it --rm alpine sh                       # 临时交互式容器（退出即删）
docker ps                           # 查看运行中的容器
docker ps -a                        # 查看所有容器（含已停止）
docker stop web                     # 停止容器
docker start web                    # 启动已停止容器
docker restart web                  # 重启容器
docker rm web                       # 删除已停止容器
docker rm -f web                    # 强制删除（即使正在运行）
docker rm $(docker ps -aq)          # 删除所有容器（慎用！）
```

---

## 🔹 调试与日志

```bash
docker logs web                     # 查看容器日志
docker logs -f web                  # 实时跟踪日志（按 Ctrl+C 退出）
docker exec -it web bash            # 进入运行中的容器
docker inspect web                  # 查看容器详细信息（IP、挂载、网络等）
docker top web                      # 查看容器内进程
docker stats                        # 实时监控所有容器资源使用（CPU/内存）
```

---

## 🔹 数据持久化（卷 & 绑定挂载）

```bash
# 绑定挂载（Bind Mount）— 推荐用于开发
docker run -v $(pwd):/app my-app

# 命名卷（Named Volume）— 推荐用于生产数据
docker volume create app-data
docker run -v app-data:/data my-app

# 查看卷
docker volume ls
docker volume inspect app-data

# 备份卷数据（通过临时容器）
docker run --rm -v app-data:/data -v $(pwd):/backup alpine \
  tar czf /backup/app-data.tar.gz -C /data .
```

---

## 🔹 网络与通信

```bash
docker network ls                   # 列出网络
docker network create mynet         # 创建自定义 bridge 网络
docker run --network mynet --name db redis
docker run --network mynet --name web my-app

# 容器间可通过服务名通信（如 web → db）
```

**默认情况下，**`docker compose` **会自动创建专属网络，服务名即 DNS 名。**

---

## 🔹 docker-compose 常用命令

```bash
docker compose up -d                # 后台启动所有服务
docker compose down                 # 停止并删除容器、网络（不删卷）
docker compose down -v              # 同时删除命名卷（⚠️ 数据丢失！）
docker compose logs -f web          # 跟踪指定服务日志
docker compose ps                   # 查看服务状态
docker compose build                # 仅构建镜像（不启动）
docker compose restart web          # 重启单个服务

```

****新版是** `docker compose`（无短横线），不是 `docker-compose`**

---

## 🔹 Dockerfile 编写最佳实践（示例）

```bash
FROM python:3.12-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt  # 利用层缓存
COPY . .
RUN addgroup --system app && adduser --system --ingroup app app
USER app
EXPOSE 8000
CMD ["python", "app.py"]

# ❌ 避免
# COPY . . before pip install → 破坏缓存
# RUN pip install without --no-cache-dir → 镜像变大
# 以 root 运行 → 安全风险

```

---

## 🔹 安全与优化技巧

```bash
# 扫描镜像漏洞（Docker Scout，需登录 Docker Hub）
docker scout my-app

# 查看镜像大小
docker images

# 减小体积技巧：
#   - 用 slim/alpine 基础镜像
#   - 合并 RUN 命令
#   - 清理 apt 缓存（若用 Debian）：
#     RUN apt-get update && apt-get install -y ... && rm -rf /var/lib/apt/lists/*
```

---

## 🔹 快捷别名

```bash
# 添加到 ~/.bashrc
echo "alias dps='docker ps'" >> ~/.bashrc
echo "alias dlogs='docker logs -f'" >> ~/.bashrc
echo "alias dc='docker compose'" >> ~/.bashrc
source ~/.bashrc

# 使用示例
dps
dlogs web
dc up -d
```

**✨**  **小技巧**

* **日志打 stdout** **：方便被采集（Fluentd / Loki）**
* **配置走环境变量** **：避免硬编码（**`ENV` **或** `environment:` **in compose）**
* **非 root 运行** **：安全基线**
* **镜像不可变** **：同一镜像在 dev/staging/prod 行为一致**
* **compose 用于本地/测试，K8s 用于生产** **（但原理相通）**

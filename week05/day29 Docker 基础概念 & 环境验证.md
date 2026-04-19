# 📖 Day 29 笔记：Docker 基础概念 & 环境验证

---

## ✅ 今日任务完成情况

- [X] 安装 Docker Engine
- [X] **验证** `docker --version` **和** `docker compose version`
- [X] `成功运行 hello-world 容器`
- [X] **拉取** `python:3.12-slim` **并进入交互式 shell**

---

## 🔧 关键操作记录

```bash
# 验证安装
docker --version
docker compose version

# 运行 Hello World
docker run hello-world

# 进入 Python 容器
docker run -it --rm python:3.11-slim bash

# 查看本地镜像与容器
docker images
docker ps -a
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **： **Linux 下运行** `docker` **命令提示 “permission denied”****
  **解决** **：**将用户加入 docker 组 →****

  ```bash
  sudo usermod -aG docker $USER
  ```

  **重启终端或执行** `newgrp docker`
* **问题** **：拉取镜像速度极慢**
* **解决** ：**配置国内镜像加速器（如阿里云），修改** `/etc/docker/daemon.json`：
* ```json
  {
    "registry-mirrors": ["https://<your-mirror>.mirror.aliyuncs.com"]
  }
  ```

**重启 Docker：**`sudo systemctl restart docker`

---

## 💡 小技巧 / 收获

* **镜像 ≠ 容器** **：镜像是只读模板，容器是它的运行实例。**
* **`--rm` **参数**** **：容器退出后自动删除，适合临时测试。**
* **Docker 架构** **：Client ↔ Daemon ↔ Registry**

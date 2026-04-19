# 📖 Day 44 笔记：本地集群搭建（Minikube）

---

## ✅ 今日任务完成情况

- [X] 安装 Minikube
- [X] `启动本地集群`
- [X] `验证 kubectl get nodes 显示 Ready`

---

## 🔧 关键操作记录

```bash
# 安装 Minikube（Linux 示例）
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# 启动集群（使用 containerd 作为运行时）
minikube start --driver=docker

# 检查节点状态
kubectl get nodes

# 查看集群上下文
kubectl config current-context
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**`minikube start` **卡在 "Pulling base image..."**
  **解决** **：添加国内镜像加速（如阿里云）或使用** `--image-mirror-country=cn` **参数：**
* ```bash
  minikube start --image-mirror-country=cn --driver=docker
  ```

---

## 💡 小技巧 / 收获

* **Minikube 内置 Docker 环境** **：可用** `minikube docker-env` **切换上下文，在本地构建镜像直接供集群使用。**
* **推荐驱动** **：**`--driver=docker` **最轻量，兼容性好。**

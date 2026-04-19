# 📖 Day 43 笔记：K8s 核心概念初探

---

## ✅ 今日任务完成情况

- [X] 阅读 Kubernetes 官方文档 “What is Kubernetes?” 和 “Kubernetes Components”
- [X] 理解 Pod 是最小调度单位
- [X] `能口头解释 Pod 与容器的区别`

---

## 🔧 关键操作记录

```bash
# 无实际命令，但可查看官方架构图
# https://kubernetes.io/docs/concepts/overview/components/
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：一开始以为“一个 Pod = 一个容器”，混淆了调度单位。**
  **解决** **：通过官方文档明确：Pod 是逻辑主机，可包含多个紧密耦合的容器（如主应用 + 日志 sidecar）。**

---

## 💡 小技巧 / 收获

* **Pod ≠ Container** **：Pod 是 K8s 调度的最小单元，容器是运行时的最小单元。**
* **为什么需要 Pod** **？因为有时多个容器需要共享网络、存储、IPC（例如 Web Server + Log Shipper）。**

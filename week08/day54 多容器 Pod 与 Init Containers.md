# 📖 Day 54 笔记：多容器 Pod 与 Init Containers

---

## ✅ 今日任务完成情况

- [X] **创建含 sidecar 容器的 Pod**
- [X] 实践 Init Container（模拟等待依赖）

---

## 🔧 关键操作记录

```yml
# pod-multi-container.yaml
spec:
  initContainers:
  - name: wait-for-db
    image: busybox:1.28
    command: ['sh', '-c', 'echo "Waiting for DB..."; sleep 10; echo "DB ready!"']
  containers:
  - name: main-app
    image: nginx
  - name: log-shipper
    image: busybox:1.28
    command: ['tail', '-f', '/dev/null']  # 模拟 sidecar
```

```bash
kubectl apply -f pod-multi-container.yaml
kubectl logs <pod> -c main-app
kubectl logs <pod> -c log-shipper
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：Init Container 失败导致主容器不启动**
  **解决** **：这是预期行为！Init Container 必须成功，主容器才会启动。**

---

## 💡 小技巧 / 收获

* **Init Container 用于“前置条件检查”** **（如等待数据库、加载证书）。**
* **Sidecar 容器用于辅助功能** **（日志收集、监控代理），与主容器共享网络/存储。**

# 📖 Day 47 笔记：Deployment 入门

---

## ✅ 今日任务完成情况

- [X] **编写 Deployment YAML**
- [X] 部署 3 副本 nginx
- [X] **验证自动重建能力**

---

## 🔧 关键操作记录

```yml
# deployment-nginx.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.25
```

```bash
kubectl apply -f deployment-nginx.yaml
kubectl get deployments
kubectl get replicasets
kubectl delete pod <任意一个Pod>  # 观察自动重建
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：删除 Pod 后新 Pod 一直 Pending**
  **解决** **：检查节点资源是否不足，或镜像拉取失败（**`kubectl describe pod` **查 Events）。**

---

## 💡 小技巧 / 收获

* **Deployment 控制 ReplicaSet，ReplicaSet 控制 Pod** **。**
* **滚动更新基础** **：修改** `image` **字段即可触发更新。**

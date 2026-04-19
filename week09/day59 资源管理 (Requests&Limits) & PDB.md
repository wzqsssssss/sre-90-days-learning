# 📖 Day 59 笔记：资源管理 (Requests/Limits) & PDB

---

## ✅ 今日任务完成情况

- [X] **为应用容器设置合理的 requests/limits**
- [X] 理解 QoS 等级
- [X] `为关键应用创建 PDB`

---

## 🔧 关键操作记录

```yml
# deployment-with-resources.yaml
spec:
  containers:
  - name: web-app
    image: nginx
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m" # 0.25 core
      limits:
        memory: "128Mi"
        cpu: "500m" # 0.5 core
```

```yml
# pdb-redis.yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: redis-pdb
spec:
  minAvailable: 1 # 至少保证1个Pod可用
  selector:
    matchLabels:
      app: redis
```

```bash
kubectl apply -f pdb-redis.yaml
kubectl get pdb
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：设置了内存 limits 后，应用频繁 OOMKilled。**
  **解决** **：**`limits` **设置过低。应通过监控（如** `kubectl top pod`）观察实际使用量，再合理设置。

---

## 💡 小技巧 / 收获

* **Requests 决定调度** **：K8s 只会将 Pod 调度到剩余资源 >= requests 的节点上。**
* **Limits 决定上限** **：CPU 超限会被 throttling（节流），内存超限会被 OOMKilled（杀死）。**
* **PDB 是保障高可用的“防驱逐盾牌”** **，在执行** `kubectl drain` **时会强制遵守。**

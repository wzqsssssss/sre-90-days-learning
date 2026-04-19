# 📖 Day 58 笔记：PersistentVolume 与 Redis 持久化

---

## ✅ 今日任务完成情况

- [X] 在 Worker 节点创建本地存储目录
- [X] `创建 PV 和 PVC`
- [X] 部署 StatefulSet 的 Redis 并挂载 PVC
- [X] `验证数据持久化`

---

## 🔧 关键操作记录

```yml
# pv-redis.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: redis-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: local-storage
  local:
    path: /mnt/redis-data
  nodeAffinity:
    required:
      nodeSelectorTerms:
        - matchExpressions:
            - key: kubernetes.io/hostname
              operator: In
              values:
                - worker-node-hostname # 替换为你的 Worker 节点名
```

```yml
# pvc-redis.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: redis-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: local-storage
```

```yml
# statefulset-redis.yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: redis
spec:
  serviceName: "redis"
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
        - name: redis
          image: redis:7.0
          volumeMounts:
            - name: redis-data
              mountPath: /data
      volumes:
        - name: redis-data
          persistentVolumeClaim:
            claimName: redis-pvc
```

```bash
# 在 Worker 节点上
sudo mkdir -p /mnt/redis-data
sudo chmod 777 /mnt/redis-data # 仅用于测试

# 应用资源
kubectl apply -f pv-redis.yaml -f pvc-redis.yaml -f statefulset-redis.yaml

# 测试持久化
kubectl exec -it redis-0 -- redis-cli
> SET testkey "hello"
> exit
kubectl delete pod redis-0
# 等待新 Pod 启动
kubectl exec -it redis-0 -- redis-cli
> GET testkey # 应该返回 "hello"
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：PV 一直处于** `Pending` **状态。**
  **解决** **：检查** `nodeAffinity` **中的节点名是否与** `kubectl get nodes` **输出完全一致。**

---

## 💡 小技巧 / 收获

* **StatefulSet 是管理有状态应用（如数据库）的标准方式** **，保证 Pod 名称、网络标识和存储的稳定性。**
* **Local PV 性能好但不具备高可用性** **，生产环境通常使用云盘或分布式存储（如 Ceph）。**

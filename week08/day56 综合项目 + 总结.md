# 📖 Day 56 笔记：综合项目 + 总结

---

## ✅ 今日任务完成情况

- [X] **部署 Flask + Redis 应用**
- [X] ****编写完整 YAML 清单****
- [X] 输出总结文档

---

## 🔧 关键操作记录

```bash
# 项目结构示例
.
├── flask-app/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
├── redis/
│   ├── statefulset.yaml
│   ├── service.yaml
│   └── pvc.yaml
└── kustomization.yaml (可选)
```

```bash
kubectl apply -k .  # 或分别 apply
kubectl port-forward svc/flask-svc 5000:80
# 访问 http://localhost:5000
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：Flask 应用无法连接 Redis**
  **解决** **：确认使用的是 Redis Service 名（**`redis-svc`）作为 hostname，而非 Pod IP。

---

## 💡 小技巧 / 收获

* **服务发现靠 Service 名** **：在集群内，**`<service-name>.<namespace>.svc.cluster.local` **是标准 DNS。**
* **本周最大收获** **：K8s 不只是“跑容器”，而是通过声明式 API + 控制器模式实现自愈、扩缩、隔离等能力。**

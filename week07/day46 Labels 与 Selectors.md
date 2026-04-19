# 📖 Day 46 笔记：Labels 与 Selectors

---

## ✅ 今日任务完成情况

- [X] `为 Pod 添加 labels`
- [X] **使用 label selector 查询**
- [X] `理解 Service 如何通过 selector 关联 Pod `

---

## 🔧 关键操作记录

```yml
# pod-with-label.yaml
metadata:
  name: web-pod
  labels:
    app: web
    env: dev
```

```bash
# 查看带标签的 Pod
kubectl get pods -l app=web
kubectl get pods -l env=dev,app=web

# 查看所有标签
kubectl get pods --show-labels
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：Service 无法找到后端 Pod**
  **解决** **：检查 Service 的** `spec.selector` **是否与 Pod 的** `labels` **完全匹配。**

---

## 💡 小技巧 / 收获

* **标签是 K8s 的“ glue”** **：Deployment、Service、ReplicaSet 都靠它关联资源。**
* **不要硬编码 IP** **：永远通过 Service + Label 访问应用。**

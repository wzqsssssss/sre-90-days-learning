# 📖 Day 69 笔记：健康探针深度实践

---

## ✅ 今日任务完成情况

- [X] 为应用同时配置 livenessProbe 和 readinessProbe
- [X] **模拟** `liveness` **失败，观察 Pod 重启**
- [X] **模拟** `readiness` **失败，观察流量切换

---

## 🔧 关键操作记录

```yml
# deployment-with-probes.yaml
spec:
  containers:
    - name: app
      image: my-app
      livenessProbe:
        exec:
          command: ["/bin/sh", "-c", "test -f /tmp/live"]
        initialDelaySeconds: 10
        periodSeconds: 5
      readinessProbe:
        exec:
          command: ["/bin/sh", "-c", "test -f /tmp/ready"]
        initialDelaySeconds: 5
        periodSeconds: 5
```

```bash
# 部署后
kubectl exec -it <pod> -- touch /tmp/live /tmp/ready

# 模拟 liveness 失败
kubectl exec -it <pod> -- rm /tmp/live
# 观察 Pod 重启: kubectl get pods -w

# 模拟 readiness 失败
kubectl exec -it <pod> -- rm /tmp/ready
# 观察 Endpoints: kubectl get endpoints my-app-svc
# 此时该 Pod IP 应从 Endpoints 列表中消失
```

---

## ⚠️ 遇到的问题 & 解法

* **问题**：`readinessProbe` **失败后，Pod 仍在接收流量。**

  **解决** **：确认客户端是通过** **Service** **访问的，而不是直接访问 Pod IP。**

---

## 💡 小技巧 / 收获

* **`livenessProbe` **是“生命线”，失败就重启**** **。**
* **`readinessProbe` **是“就绪开关”，失败就切流**** **。**
* **两者结合，是实现零宕机滚动更新和自愈的关键** **。**

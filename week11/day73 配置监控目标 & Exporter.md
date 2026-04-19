# 📖 Day 73 笔记：配置监控目标 & Exporter

---

## ✅ 今日任务完成情况

- [X] `部署一个 Nginx 应用并暴露 /metrics（模拟） `
- [X] 创建 Service 和 ServiceMonitor
- [X] `在 Prometheus Targets 页面看到新目标`

---

## 🔧 关键操作记录

```yml
# nginx-demo.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-demo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx-demo
  template:
    metadata:
      labels:
        app: nginx-demo
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-demo
  labels:
    app: nginx-demo
spec:
  ports:
  - port: 80
    targetPort: 80
  selector:
    app: nginx-demo
```

```yml
# servicemonitor-nginx.yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: nginx-demo
  namespace: default
spec:
  selector:
    matchLabels:
      app: nginx-demo
  endpoints:
  - port: http
    interval: 30s
#注：真实应用需用 prometheus/client 库暴露指标
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：ServiceMonitor 创建后，Prometheus Targets 里看不到？**
  **解决** **：检查** `selector.matchLabels` **是否与 Service 的 labels 完全匹配；确认 ServiceMonitor 与 Prometheus 在同一命名空间或已配置** `serviceMonitorNamespaceSelector`。

---

## 💡 小技巧 / 收获

* **ServiceMonitor vs PodMonitor** **：**
* `ServiceMonitor`：基于 Service 的 Endpoints 发现目标（推荐，更稳定）
* `PodMonitor`：直接监控 Pod（适合无 Service 的场景）

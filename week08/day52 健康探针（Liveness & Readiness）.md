# 📖 Day 52 笔记：健康探针（Liveness & Readiness）

---

## ✅ 今日任务完成情况

- [X] **为应用添加 livenessProbe 和 readinessProbe**
- [X] `模拟故障并观察 K8s 行为`

---

## 🔧 关键操作记录

```yml
# deployment-with-probes.yaml
spec:
  containers:
  - name: app
    image: nginx
    livenessProbe:
      httpGet:
        path: /healthz
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 10
    readinessProbe:
      httpGet:
        path: /ready
        port: 80
      initialDelaySeconds: 2
      periodSeconds: 5
# 注：为测试，可临时在 nginx 中添加 /healthz 和 /ready 路由（或用自定义镜像）。
```

```bash
# 模拟 liveness 失败：进入容器删除 /healthz 文件或返回 500
kubectl exec -it <pod> -- rm /usr/share/nginx/html/healthz
# 观察 Pod 重启
kubectl get pods -w
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：探针一直失败，Pod 不断重启**
  **解决** **：检查** `initialDelaySeconds` **是否太短，应用还没启动完就被探测。**

---

## 💡 小技巧 / 收获

* **livenessProbe → 决定是否重启 Pod**
* **readinessProbe → 决定是否加入 Service 后端（流量接入）**
* **合理设置 initialDelaySeconds 非常重要！**

# 📖 Day 72 笔记：在 Kubernetes 中部署 Prometheus

---

## ✅ 今日任务完成情况

- [X] 使用 Helm 安装** `kube-prometheus-stack`**
- [X] **验证 Prometheus、Alertmanager、Grafana Pod 状态**
- [X] `访问 Prometheus Web UI`

---

## 🔧 关键操作记录

```bash
# 添加 Helm repo
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# 安装（指定命名空间）
kubectl create ns monitoring
helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack -n monitoring

# 端口转发访问
kubectl port-forward svc/kube-prometheus-stack-prometheus 9090:9090 -n monitoring
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：Helm 安装后 Grafana 无法登录？**
  **解决** **：默认账号** `admin`，密码可通过以下命令获取：

  ```bash
  kubectl get secret kube-prometheus-stack-grafana -n monitoring -o jsonpath='{.data.admin-password}' | base64 -d
  ```

---

## 💡 小技巧 / 收获

* `kube-prometheus-stack` **默认包含：**

  * **Prometheus Server**
  * **Alertmanager**
  * **Grafana**
  * **Node Exporter**
  * **Kube State Metrics**
  * **大量预置的 ServiceMonitor**

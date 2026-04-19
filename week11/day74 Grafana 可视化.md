# 📖 Day 74 笔记：Grafana 可视化

---

## ✅ 今日任务完成情况

- [X] **导入官方 Dashboard（ID: 1860 for Node Exporter）**
- [X] **创建自定义 Dashboard 展示 CPU/内存**
- [X] **配置变量（如** `namespace`）实现动态过滤

---

## 🔧 关键操作记录

```bash
# 端口转发 Grafana
kubectl port-forward svc/kube-prometheus-stack-grafana 3000:80 -n monitoring
```

**在 Grafana UI 中：**

1. **Dashboards → Import**
2. **输入 ID** `1860`（Node Exporter Full）
3. **选择 Prometheus 数据源**

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：导入 Dashboard 后图表无数据？**
  **解决** **：检查数据源是否选择正确（应为** `Prometheus`）；确认指标名称是否匹配（如旧版用 `node_cpu`，新版用 `node_cpu_seconds_total`）。

---

## 💡 小技巧 / 收获

* **常用 Dashboard ID** **：**
* `315`：Kubernetes Cluster
* `6417`：Kubernetes Pods
* `11074`：Kubernetes Deployments

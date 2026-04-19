# 📖 Day 71 笔记：Prometheus 基础概念 & 架构理解

---

## ✅ 今日任务完成情况

- [X] 理解 Prometheus 的核心组件（Server, Exporter, Alertmanager）
- [X] `掌握 Pull 模型 vs Push 模型的区别`
- [X] `学习 PromQL 基础语法（rate(), sum(), by()）`

---

## 🔧 关键操作记录

```bash
# 在本地用 Docker 快速启动 Prometheus
docker run -d --name=prometheus -p 9090:9090 prom/prometheus

# 访问 Web UI: http://localhost:9090
# 尝试查询: up, prometheus_build_info
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：不理解为什么 Prometheus 用 Pull 而不是 Push？**
  **解决** **：Pull 模型更适合动态环境（如 K8s），因为 Server 主动发现目标，无需客户端配置推送地址；且网络策略更简单（只需 Server 能访问 Target）。**

---

## 💡 小技巧 / 收获

* **Prometheus 数据模型** **：**`metric_name{label1="value1", label2="value2"} value timestamp`
* **常用 PromQL** **：**

  ```promql
  # CPU 使用率（排除 idle）
  100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

  # 内存使用率
  (node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100
  ```

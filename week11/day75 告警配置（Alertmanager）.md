# 📖 Day 75 笔记：告警配置（Alertmanager）

---

## ✅ 今日任务完成情况

- [X] **编写 PrometheusRule：CPU > 80% 持续 2 分钟告警**
- [X] `在 Alertmanager UI 查看告警状态`
- [X] 验证告警从** `pending` **到** `firing`**

---

## 🔧 关键操作记录

```yml
# cpu-alert.yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: high-cpu-alert
  namespace: monitoring
spec:
  groups:
  - name: node-alerts
    rules:
    - alert: HighCpuUsage
      expr: 100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
      for: 2m
      labels:
        severity: warning
      annotations:
        summary: "High CPU usage on {{ $labels.instance }}"
        description: "CPU usage is above 80% (current value: {{ $value }}%)"
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：告警规则创建后不生效？**
  **解决** **：检查 PrometheusRule 的 namespace 是否被 Prometheus 监听（默认只监听** `monitoring`）；在 Prometheus UI 的 **Alerts** **页面查看规则是否加载。**

---

## 💡 小技巧 / 收获

* **测试告警** **：可在表达式中临时降低阈值（如** `> 10`）快速触发。
* **静默（Silence）** **：在 Alertmanager 中可临时屏蔽特定告警。**

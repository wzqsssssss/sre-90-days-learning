# 📖 Day 77 笔记：整合项目 - 监控自定义应用

---

## ✅ 今日任务完成情况

- [X] 部署 Python Flask 应用，集成** `prometheus_client`**
- [X] ******配置 ServiceMonitor 抓取应用指标******
- [X] **在 Grafana 创建 Dashboard 展示请求 QPS、延迟**

---

## 🔧 关键操作记录

```python
# app.py (Flask + prometheus_client)
from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
REQUEST_COUNT = Counter('flask_requests_total', 'Total requests')

@app.route('/metrics')
def metrics():
    return generate_latest()

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    return "Hello Prometheus!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

```yml
# flask-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: flask-app
  labels:
    app: flask-app
spec:
  ports:
  - port: 5000
    name: http
  selector:
    app: flask-app
---
# flask-servicemonitor.yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: flask-app
spec:
  selector:
    matchLabels:
      app: flask-app
  endpoints:
  - port: http
    path: /metrics
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**`/metrics` **返回 404？**
  **解决** **：确认 Flask 路由路径正确；检查 Service 的** `port.name` **是否与 ServiceMonitor 的** `endpoints.port` **一致。**

---

## 💡 小技巧 / 收获

* **自定义指标类型** **：**
* `Counter`：单调递增（如请求数）
* `Gauge`：可增可减（如内存使用量）
* `Histogram`：分布统计（如请求延迟）

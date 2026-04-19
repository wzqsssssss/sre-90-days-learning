# 📖 Day 76 笔记：深入 PromQL & 故障排查

---

## ✅ 今日任务完成情况

- [X] 编写复杂查询：各命名空间 Pod 内存 Top 5
- [X] **模拟 Target Down（删除 Pod），观察行为**
- [X] 使用** `up` **指标检测服务可用性**

---

## 🔧 关键操作记录

```promql
# 各命名空间内存使用 Top 5
topk(5, sum by (namespace) (container_memory_usage_bytes{container!="",container!="POD"}))

# 检测 Down 的 Target
up == 0

# 计算 API Server 请求 QPS
sum(rate(apiserver_request_total[5m]))
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：查询返回** `no data`？
  **解决** **：检查时间范围（右上角）；确认指标是否存在（在** **Graph** **标签页输入指标名）；检查标签过滤是否过严。**

---

## 💡 小技巧 / 收获

* **调试技巧** **：**
* **先查原始指标（如** `container_memory_usage_bytes`）
* **逐步添加聚合（**`sum by (pod)`）
* **用** `count()` **验证数据量**

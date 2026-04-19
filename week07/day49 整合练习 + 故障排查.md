# 📖 Day 49 笔记：整合练习 + 故障排查

---

## ✅ 今日任务完成情况

- [X] **从零部署完整应用（Deployment + Service）**
- [X] **模拟故障并观察行为**
- [X] 完成本周总结笔记

---

## 🔧 关键操作记录

```bash
# 清理重来
kubectl delete -f .

# 重新部署
kubectl apply -f deployment.yaml -f service.yaml

# 查看所有资源
kubectl get all -o wide
```


---

## ⚠️ 遇到的问题 & 解法

* **问题** **：Service 有 Endpoints，但无法访问**
  **解决** **：检查容器是否监听** `0.0.0.0`（而非 `127.0.0.1`），nginx 默认 OK。

---

## 💡 小技巧 / 收获

* **`kubectl get all` **是快速概览的好命令****
* **排错三板斧** **：**

  1. `kubectl describe <resource>`
  2. `kubectl logs <pod>`
  3. **检查 Labels/Selectors 是否匹配**

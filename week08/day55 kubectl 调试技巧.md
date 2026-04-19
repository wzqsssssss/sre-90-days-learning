# 📖 Day 55 笔记：kubectl 调试技巧

---

## ✅ 今日任务完成情况

- [X] **使用 describe 查看 Events**
- [X] `使用 logs 查看日志`
- [X] **使用 exec 进入容器**

---

## 🔧 关键操作记录

```bash
# 查看 Pod 详细信息（含 Events）
kubectl describe pod <pod-name>

# 实时查看日志
kubectl logs -f <pod-name>

# 进入容器
kubectl exec -it <pod-name> -- sh

# 查看特定容器日志（多容器 Pod）
kubectl logs <pod-name> -c <container-name>

# 查看上一个崩溃的容器日志
kubectl logs <pod-name> --previous
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：Pod 卡在** `ContainerCreating`
  **解决** **：**`describe` **显示 “Failed to pull image”，检查镜像名称或网络。**

---

## 💡 小技巧 / 收获

* **Events 是排错第一入口** **！90% 的问题原因都在这里。**
* **`--previous` **参数对 CrashLoopBackOff 排错极有用**** **。**

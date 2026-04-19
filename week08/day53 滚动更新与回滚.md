# 📖 Day 53 笔记：滚动更新与回滚

---

## ✅ 今日任务完成情况

- [X] `修改 Deployment 镜像版本`
- [X] **观察滚动更新过程**
- [X] `成功执行回滚`

---

## 🔧 关键操作记录

```bash
# 查看历史版本
kubectl rollout history deployment/nginx-deploy

# 更新镜像（触发滚动更新）
kubectl set image deployment/nginx-deploy nginx=nginx:1.26

# 监控更新状态
kubectl rollout status deployment/nginx-deploy

# 回滚到上一版本
kubectl rollout undo deployment/nginx-deploy

# 回滚到指定版本
kubectl rollout undo deployment/nginx-deploy --to-revision=2
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：更新后服务中断**
  **解决** **：确保** `readinessProbe` **正确配置，且** `maxUnavailable`/`maxSurge` **设置合理（默认 25%）。**

---

## 💡 小技巧 / 收获

* **Deployment 默认策略是 RollingUpdate** **。**
* **`kubectl rollout pause/resume` **可暂停/恢复更新，用于金丝雀发布调试**** **。**

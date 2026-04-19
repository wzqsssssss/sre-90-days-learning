# 📖 Day 45 笔记：kubectl 与 YAML 基础

---

## ✅ 今日任务完成情况

- [X] **掌握常用 kubectl 命令**
- [X] `用 YAML 创建 nginx Pod`
- [X] `对比命令式 vs 声明式管理`

---

## 🔧 关键操作记录

```yml
# pod-nginx.yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
  - name: nginx
    image: nginx:1.25
```

```bash
# 应用 YAML
kubectl apply -f pod-nginx.yaml

# 查看 Pod
kubectl get pods
kubectl describe pod nginx-pod
kubectl logs nginx-pod

# 删除 Pod
kubectl delete -f pod-nginx.yaml
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**`kubectl apply` **报错 “error validating data”**
  **解决** **：YAML 缩进错误。使用** `yamllint` **或 VS Code YAML 插件检查格式。**

---

## 💡 小技巧 / 收获

* **声明式 > 命令式** **：生产环境应使用 YAML 文件管理资源，便于版本控制。**
* **快速生成模板** **：**`kubectl create deploy nginx --image=nginx --dry-run=client -o yaml > deploy.yaml`

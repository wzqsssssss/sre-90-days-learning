# 📖 Day 60 笔记：多租户隔离 (Namespace + RBAC)

---

## ✅ 今日任务完成情况

- [X] `创建 dev-team 和 prod-team 命名空间`
- [X] 为 `dev-team` **创建 ServiceAccount 和 RoleBinding****
- [X] `验证权限隔离`

---

## 🔧 关键操作记录

```yml
# role-dev.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: dev-team
  name: dev-role
rules:
  - apiGroups: ["", "apps", "batch"] # "" 表示核心 API 组
    resources: ["pods", "deployments", "jobs"]
    verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```

```yml
# rolebinding-dev.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: dev-binding
  namespace: dev-team
subjects:
  - kind: ServiceAccount
    name: dev-sa
    namespace: dev-team
roleRef:
  kind: Role
  name: dev-role
  apiGroup: rbac.authorization.k8s.io
```

```bash
# 创建资源
kubectl create ns dev-team
kubectl create ns prod-team
kubectl create sa dev-sa -n dev-team
kubectl apply -f role-dev.yaml -f rolebinding-dev.yaml

# 获取 dev-sa 的 token 并配置新的 kubeconfig (过程略)
# 使用新 kubeconfig
kubectl get pods -n dev-team # 成功
kubectl get pods -n prod-team # 失败，提示权限不足
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：RoleBinding 创建后权限不生效。**
  **解决** **：确认** `subjects` **中的** `namespace` **字段正确，且使用的 kubeconfig 确实关联了该 ServiceAccount。**

---

## 💡 小技巧 / 收获

* **Namespace 是逻辑隔离的第一道墙** **。**
* **RBAC 是权限控制的基石** **，遵循最小权限原则。**
* **ServiceAccount 是给 Pod 用的身份** **，User 是给人用的身份。**

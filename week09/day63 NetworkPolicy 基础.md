# 📖 Day 63 笔记：NetworkPolicy 基础

---

## ✅ 今日任务完成情况

- [X] **理解 NetworkPolicy 作用**
- [X] ****创建策略限制 Pod 间通信****
- [X] 验证策略生效

---

## 🔧 关键操作记录

```yml
# networkpolicy-deny-all.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
  namespace: default
spec:
  podSelector: {} # 选中所有 Pod
  policyTypes:
    - Ingress
    - Egress
```

```yml
# networkpolicy-allow-frontend-to-backend.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080
```

```bash
# 测试
kubectl run debug --image=busybox:1.28 -it --rm -- sh
/ # wget -qO- http://backend-svc:8080 # 应该失败
# 在一个标签为 app=frontend 的 Pod 中执行同样命令，应该成功
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：应用了 NetworkPolicy 后所有流量都被拒绝。**
  **解决** **：Calico 等 CNI 插件默认允许所有流量。只有当 Pod 被至少一个 NetworkPolicy 选中时，才会进入“拒绝所有未明确允许”的模式。**

---

## 💡 小技巧 / 收获

* **NetworkPolicy 实现了微隔离（Micro-segmentation）** **，是零信任安全模型的关键。**
* **策略是“白名单”机制** **：只允许明确声明的流量，其余全部拒绝。**

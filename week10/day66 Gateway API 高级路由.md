# 📖 Day 66 笔记：Gateway API 高级路由

---

## ✅ 今日任务完成情况

- [X] `配置基于路径和主机名的路由`
- [X] 实践金丝雀发布（权重路由）
- [X] `验证流量按预期分配`

---

## 🔧 关键操作记录

```yml
# httproute-canary.yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: canary-route
spec:
  parentRefs:
    - name: my-gateway
  hostnames:
    - "canary.example.com"
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api/v1
      backendRefs:
        - name: stable-svc
          port: 80
          weight: 90
        - name: canary-svc
          port: 80
          weight: 10
```

```bash
# 部署两个版本的服务
kubectl apply -f stable-deploy.yaml -f canary-deploy.yaml

# 使用脚本或工具循环请求，观察日志
for i in {1..100}; do
  curl -s -H "Host: canary.example.com" http://<GATEWAY_IP>/api/v1 | grep version
done
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：权重路由不生效，所有流量都去了一个后端。**
  **解决** **：确认两个** `backendRefs` **的** `weight` **字段总和为 100，并且服务名称和端口正确。**

---

## 💡 小技巧 / 收获

* **高级路由能力（如权重、Header 匹配）是 Ingress 很难标准化实现的，而 Gateway API 原生支持** **。**
* **金丝雀发布从此变得非常简单和标准化** **。**

# 📖 Day 65 笔记：跨 Namespace 引用与 ReferenceGrant

---

## ✅ 今日任务完成情况

- [X] 将应用部署在 `app-ns` **命名空间**
- [X] **将** `Gateway` **部署在** `gateway-ns` **命名空间**
- [X] `创建 ReferenceGrant 实现跨 ns 路由`
- [X] 验证路由成功

---

## 🔧 关键操作记录

```yml
# referencegrant.yaml
apiVersion: gateway.networking.k8s.io/v1beta1
kind: ReferenceGrant
metadata:
  name: allow-gateway-to-app
  namespace: app-ns # Grant 必须在被引用资源（Service）所在的命名空间
spec:
  from:
    - group: gateway.networking.k8s.io
      kind: HTTPRoute
      namespace: gateway-ns # 允许哪个命名空间的 HTTPRoute 引用我
  to:
    - group: "" # core group
      kind: Service
      name: my-app-svc # 可以省略 name，表示允许所有 Service
```

```bash
kubectl create ns app-ns
kubectl create ns gateway-ns
# ... 部署应用到 app-ns, Gateway 到 gateway-ns

kubectl apply -f referencegrant.yaml
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：创建了** `ReferenceGrant` **但路由依然失败。**
  **解决** **：检查** `ReferenceGrant` **的** `namespace` **字段是否在**  **被引用方** **（即 Service 所在的** `app-ns`）。

---

## 💡 小技巧 / 收获

* **`ReferenceGrant` **是 Gateway API 实现多租户安全隔离的关键**** **。**
* **没有 `ReferenceGrant`，跨命名空间的引用会被拒绝** **，这是默认的安全行为。**

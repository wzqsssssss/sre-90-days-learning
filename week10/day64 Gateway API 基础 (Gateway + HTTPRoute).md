# 📖 Day 64 笔记：Gateway API 基础 (Gateway + HTTPRoute)

---

## ✅ 今日任务完成情况

- [X] 安装 Gateway API CRD
- [X] `部署 Nginx Gateway Fabric 控制器`
- [X] **创建** `GatewayClass` **->** `Gateway` **->** `HTTPRoute`
- [X] `成功通过 NodePort 访问应用`

---

## 🔧 关键操作记录

```bash
# 1. 安装 Gateway API CRD
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.3.0/standard-install.yaml

# 2. 安装 Nginx Gateway Fabric
# 下载部署文件
wget https://raw.githubusercontent.com/nginx/nginx-gateway-fabric/v2.0.0/deploy/crds.yaml
wget https://raw.githubusercontent.com/nginx/nginx-gateway-fabric/v2.0.0/deploy/nginx-gateway-fabric.yaml

# 应用
kubectl apply -f crds.yaml
kubectl apply -f nginx-gateway-fabric.yaml

# 3. 创建资源
# gatewayclass.yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: nginx-gc
spec:
  controllerName: gateway.nginx.org/nginx-gateway-controller

# gateway.yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: my-gateway
  namespace: default
spec:
  gatewayClassName: nginx-gc
  listeners:
    - name: http
      port: 80
      protocol: HTTP

# httproute.yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: app-route
  namespace: default
spec:
  parentRefs:
    - name: my-gateway
  hostnames:
    - "myapp.local"
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /
      backendRefs:
        - name: my-app-svc
          port: 80
```

```bash
kubectl apply -f gatewayclass.yaml -f gateway.yaml -f httproute.yaml

# 获取 Gateway 的 IP/端口
kubectl get gateway my-gateway -o jsonpath='{.status.addresses[0].value}:{.spec.listeners[0].port}'

# 测试访问
curl -H "Host: myapp.local" http://<GATEWAY_IP>:<PORT>
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**`Gateway` **的** `status.addresses` **为空。**
  **解决** **：确认 Nginx Gateway Fabric Pod 是否正常运行 (**`kubectl get pods -n nginx-gateway`)。若使用 NodePort，地址会是节点 IP。

---

## 💡 小技巧 / 收获

* **角色分离** **：**`GatewayClass` **(集群管理员) vs** `Gateway` **(平台团队) vs** `HTTPRoute` **(应用开发者)。**
* **Gateway API 是声明式的、面向角色的，比 Ingress 更清晰、更强大** **。**

# Week 10 - Kubernetes 现代流量与自动化命令速查表

> ✅ 所有命令均在 kubectl v1.28+ 集群验证
> 💡 使用原则：能复制、能执行、能解决问题

---

## 🔹 Gateway API (Ingress 升级版)

```bash
# 安装 Gateway API CRD 和 Nginx Gateway Fabric 控制器
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.3.0/standard-install.yaml
kubectl apply -f https://raw.githubusercontent.com/nginx/nginx-gateway-fabric/v2.0.0/deploy/nginx-gateway-fabric.yaml

# 查看核心资源
kubectl get gatewayclass
kubectl get gateway
kubectl get httproute

# 创建跨命名空间路由（关键：ReferenceGrant）
# 在 app-ns 命名空间创建 ReferenceGrant
kubectl create -n app-ns -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1beta1
kind: ReferenceGrant
metadata:
  name: allow-gw-to-app
spec:
  from:
    - group: gateway.networking.k8s.io
      kind: HTTPRoute
      namespace: gateway-ns
  to:
    - group: ""
      kind: Service
EOF

# 测试访问
GATEWAY_IP=$(kubectl get gateway my-gw -o jsonpath='{.status.addresses[0].value}')
curl -H "Host: myapp.local" http://$GATEWAY_IP
```

---

## 🔹 自动扩缩容 (HPA)

```ini
# 前提：部署 Metrics Server
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# 验证指标可用
kubectl top nodes
kubectl top pods

# 创建 HPA
kubectl autoscale deployment my-app --cpu-percent=50 --min=2 --max=10

# 或使用 YAML (推荐)
kubectl create -f - <<EOF
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 50
EOF

# 监控 HPA 状态
kubectl get hpa
kubectl describe hpa my-app-hpa
```

---

## 🔹 一次性与定时任务 (Job / CronJob)

```bash
# Job: 运行一次性任务
kubectl create job pi --image=perl -- perl -Mbignum=bpi -wle 'print bpi(2000)'

# CronJob: 运行定时任务 (每分钟一次，用于测试)
kubectl create cronjob hello --image=busybox --schedule="*/1 * * * *" -- echo "Hello from Kubernetes"

# 查看状态
kubectl get jobs
kubectl get cronjobs
kubectl get pods --watch # 观察 Job/CronJob 创建的 Pod

# 查看任务日志
kubectl logs job/pi
kubectl logs cronjob/hello # 需要指定具体的 Pod 名称
```

---

## 🔹 应用健康探针 (Liveness, Readiness, Startup)

```yml
# 在 Pod/Deployment 的容器定义中添加
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 5
readinessProbe:
  exec:
    command: ["/bin/sh", "-c", "test -f /tmp/app.ready"]
  initialDelaySeconds: 5
  periodSeconds: 3
startupProbe:
  tcpSocket:
    port: 8080
  failureThreshold: 30
  periodSeconds: 10
```

```bash
# 关键排错命令
# 查看探针失败事件
kubectl describe pod <pod-name> | grep -A10 -B5 "Liveness\|Readiness"
# 模拟探针失败
kubectl exec <pod-name> -- rm /tmp/app.ready
# 查看 Endpoints 变化 (Readiness 失败会移除 IP)
kubectl get endpoints <service-name>
```

---

## 🔹 自定义控制器入门 (Operator SDK)

```bash
# 初始化项目
operator-sdk init --domain=my.domain --repo=my-operator

# 创建 API (CRD + Controller)
operator-sdk create api --group=apps --version=v1alpha1 --kind=MyApp --resource --controller

# 构建并推送镜像
make docker-build docker-push IMG=my-registry/my-operator:v0.0.1

# 部署 Operator 到集群
make deploy IMG=my-registry/my-operator:v0.0.1

# 创建自定义资源 (CR)
kubectl apply -f config/samples/apps_v1alpha1_myapp.yaml
```

---

**✨**  **小技巧**

```bash
# 1. 快速查看所有网关相关资源
kubectl get gtw,httproute,refgrant -A

# 2. 解释 Gateway API 资源字段
kubectl explain gateway.spec.listeners
kubectl explain httproute.spec.rules.backendRefs

# 3. 为 Job/CronJob 设置历史记录限制 (避免资源堆积)
kubectl patch cronjob hello -p '{"spec":{"successfulJobsHistoryLimit":3,"failedJobsHistoryLimit":1}}'
```

# Week 8 - Kubernetes 配置与服务命令速查表

> ✅ 所有命令均在 Minikube + kubectl v1.30+ 验证
> 💡 使用原则：能复制、能执行、能解决问题

---

## 🔹 Service 类型与访问

```bash
# 查看服务
kubectl get svc
kubectl describe svc <service-name>

# 创建不同类型的 Service
kubectl expose deploy/my-app --port=80 --type=ClusterIP   # 默认类型（集群内访问）
kubectl expose deploy/my-app --port=80 --type=NodePort    # 节点端口（外部测试）
kubectl expose deploy/my-app --port=80 --type=LoadBalancer # 云厂商负载均衡（Minikube 用 tunnel）

# Minikube 访问 LoadBalancer/NodePort
minikube service <service-name>        # 自动打开浏览器
minikube ip                            # 获取节点 IP，手动拼接 URL

# 测试服务连通性（从 Pod 内部）
kubectl run debug --image=busybox:1.28 -it --rm -- sh
/ # wget -qO- http://<service-name>:<port>
```

---

## 🔹 ConfigMap（非敏感配置

```bash
# 创建 ConfigMap
kubectl create configmap app-config --from-literal=log_level=info
kubectl create configmap app-config --from-file=./app.conf
kubectl create configmap app-config --from-env-file=./.env

# 查看与使用
kubectl get configmap app-config -o yaml
kubectl describe configmap app-config

# 在 Pod 中注入（两种方式）
# 1. 作为环境变量
env:
  - name: LOG_LEVEL
    valueFrom:
      configMapKeyRef:
        name: app-config
        key: log_level

# 2. 作为卷挂载（推荐用于配置文件）
volumeMounts:
  - name: config-volume
    mountPath: /etc/config
volumes:
  - name: config-volume
    configMap:
      name: app-config
```

---

## 🔹 Secret（敏感信息）

```bash
# 创建 Secret (Opaque 类型)
echo -n 'my-password' | base64  # 先编码
kubectl create secret generic db-secret --from-literal=password='my-password'
# 或从文件创建
kubectl create secret generic tls-secret --from-file=tls.crt=./cert.pem --from-file=tls.key=./key.pem

# 查看（值是 base64 编码的）
kubectl get secret db-secret -o yaml

# 在 Pod 中注入（方式同 ConfigMap）
# 1. 作为环境变量（不推荐用于高敏信息）
env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: db-secret
        key: password

# 2. 作为卷挂载（推荐！）
volumeMounts:
  - name: secret-volume
    mountPath: /etc/secret
volumes:
  - name: secret-volume
    secret:
      secretName: db-secret
```

---

## 🔹 健康探针（Liveness & Readiness）

```yml
# 在 Deployment/Pod 的容器定义中添加
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 5   # 启动后多久开始探测
  periodSeconds: 10        # 探测间隔
readinessProbe:
  exec:
    command: ["/bin/sh", "-c", "test -f /tmp/ready"]
  initialDelaySeconds: 2
  periodSeconds: 5
```

```bash
# 关键排错命令
# 查看探针失败事件
kubectl describe pod <pod-name> | grep -A5 -B5 "Liveness\|Readiness"
# 查看应用日志，确认 /healthz 端点是否正常
kubectl logs <pod-name>
```

---

## 🔹 滚动更新与回滚

```bash
# 触发更新（修改镜像）
kubectl set image deployment/my-app my-app=nginx:1.26

# 监控更新过程
kubectl rollout status deployment/my-app

# 查看历史版本
kubectl rollout history deployment/my-app

# 回滚
kubectl rollout undo deployment/my-app                # 回滚到上一版
kubectl rollout undo deployment/my-app --to-revision=2 # 回滚到指定版本

# 暂停/恢复更新（用于金丝雀发布）
kubectl rollout pause deployment/my-app
kubectl rollout resume deployment/my-app
```

---

**✨**  **小技巧**

```bash
# 1. 快速创建 Secret/ConfigMap 的 YAML 模板
kubectl create secret generic my-secret --from-literal=key=value --dry-run=client -o yaml > secret.yaml
kubectl create configmap my-config --from-file=config.txt --dry-run=client -o yaml > configmap.yaml

# 2. 解码 Secret 的值
kubectl get secret db-secret -o jsonpath='{.data.password}' | base64 -d

# 3. 查看所有命名空间下的 ConfigMap 和 Secret
kubectl get cm,secret -A
```

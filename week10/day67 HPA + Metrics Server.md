# 📖 Day 67 笔记：HPA + Metrics Server

---

## ✅ 今日任务完成情况

- [X] **在集群中部署 Metrics Server**
- [X] **验证** `kubectl top nodes/pods` **工作正常**
- [X] 为应用配置 HPA 并测试自动扩缩容

---

## 🔧 关键操作记录

```bash
# 1. 安装 Metrics Server (注意替换镜像源)
wget https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
# 编辑 components.yaml，在 args 中添加:
# - --kubelet-insecure-tls
# - --kubelet-preferred-address-types=InternalIP
kubectl apply -f components.yaml

# 2. 验证
kubectl top nodes
kubectl top pods

# 3. 配置 HPA
kubectl autoscale deployment my-app --cpu-percent=50 --min=1 --max=5

# 或使用 YAML
# hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app
  minReplicas: 1
  maxReplicas: 5
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 50
```

```bash
# 4. 压测
kubectl run -it --rm load-test --image=busybox:1.28 --restart=Never -- sh
/ # while true; do wget -qO- http://my-app-svc; done
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**`kubectl top` **报错 “Metrics API not available”。**
  **解决** **：Metrics Server Pod 没有正常运行。检查其日志，通常需要添加** `--kubelet-insecure-tls` **参数。**

---

## 💡 小技巧 / 收获

* **HPA 是实现弹性伸缩的核心** **，让应用能根据真实负载动态调整资源。**
* **Metrics Server 是 HPA 的数据来源** **，必须先部署它。**

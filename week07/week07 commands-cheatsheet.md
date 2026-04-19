# Week 7 - Kubernetes (kubectl) 命令速查表

> ✅ 所有命令均在 Minikube + kubectl v1.30+ 验证
> 💡 使用原则：能复制、能执行、能解决问题

---

## 🔹 集群与节点信息

```bash
kubectl cluster-info          # 查看集群基本信息
kubectl get nodes             # 列出所有节点
kubectl get nodes -o wide     # 显示额外信息（如 OS、内核）
kubectl describe node <node>  # 查看节点详细状态（含资源使用、事件）
kubectl top nodes             # 查看节点 CPU/内存使用（需 Metrics Server）
```

---

## 🔹 Pod 管理（最小调度单元）

```bash
kubectl get pods                          # 列出当前命名空间的 Pod
kubectl get pods -A                       # 列出所有命名空间的 Pod
kubectl get pods -o wide                  # 显示 IP、节点等
kubectl describe pod <pod-name>           # 查看 Pod 详情（关键排错命令！）
kubectl logs <pod-name>                   # 查看 Pod 日志
kubectl logs -f <pod-name>                # 实时跟踪日志（按 Ctrl+C 退出）
kubectl logs <pod-name> -c <container>    # 多容器 Pod 查看指定容器日志
kubectl exec -it <pod-name> -- sh         # 进入 Pod 容器（交互式 shell）
kubectl delete pod <pod-name>             # 删除 Pod（Deployment 会自动重建）
```

---

## 🔹 资源部署与管理

```bash
# 通用操作
kubectl get all                           # 快速查看所有核心资源
kubectl apply -f file.yaml                # 声明式创建/更新资源
kubectl delete -f file.yaml               # 删除资源
kubectl explain pod.spec.containers       # 查看 API 字段说明（超实用！）

# Deployment
kubectl get deployments
kubectl scale deploy/nginx --replicas=5   # 手动扩缩容
kubectl rollout status deploy/nginx        # 查看滚动更新状态
kubectl rollout history deploy/nginx       # 查看发布历史
kubectl rollout undo deploy/nginx          # 回滚到上一版本

# Service
kubectl get svc
kubectl expose deploy/nginx --port=80 --type=NodePort  # 快速暴露服务
```

---

## 🔹 调试与排错三板斧

```bash
# 1️⃣ 看事件（Events 是黄金入口！）
kubectl describe pod <problem-pod>

# 2️⃣ 看日志
kubectl logs <problem-pod>
kubectl logs <problem-pod> --previous   # 查看上一个崩溃容器的日志

# 3️⃣ 进容器
kubectl exec -it <problem-pod> -- sh
# 在容器内测试：
#   curl localhost:8080      # 测试应用是否监听
#   nslookup kubernetes      # 测试 DNS 是否正常
#   cat /etc/resolv.conf     # 查看 DNS 配置
```

---

## 🔹 配置与上下文

```bash
kubectl config view                     # 查看当前 kubeconfig
kubectl config current-context          # 查看当前上下文
kubectl config use-context minikube     # 切换上下文
kubectl config get-contexts             # 列出所有上下文

# Minikube 专用
minikube start --driver=docker          # 启动集群
minikube stop                           # 停止集群
minikube delete                         # 彻底删除集群
minikube ip                             # 获取集群 IP（用于 NodePort 访问）
minikube dashboard                      # 打开 Web UI# 查看某主机的所有 facts（自动收集的系统信息）
ansible web1 -i inventory.ini -m setup

# 查看特定 fact
ansible web1 -i inventory.ini -m setup -a "filter=ansible_os_family"

# 常用 facts 示例：
# ansible_distribution → Ubuntu
# ansible_architecture → x86_64
# ansible_default_ipv4.address → 主 IP
```

---

## 🔹 实用技巧 & 别名

```bash
# 1. 设置别名（永久生效）
echo "alias k=kubectl" >> ~/.bashrc
echo "complete -F __start_kubectl k" >> ~/.bashrc  # 启用 k 的 tab 补全
source ~/.bashrc

# 2. 常用缩写（kubectl 原生支持）
k get po        # = kubectl get pods
k get deploy    # = kubectl get deployments
k get svc       # = kubectl get services
k get no        # = kubectl get nodes

# 3. 强制删除（Pod 卡在 Terminating 时）
kubectl delete pod <pod-name> --grace-period=0 --force
```

---

**✨**  **小技巧**

```bash
# 把常用命令组合存为脚本
# 创建 debug.sh
cat > ~/debug.sh << 'EOF'
#!/bin/bash
POD=$1
echo "=== Describe ==="
kubectl describe pod $POD
echo -e "\n=== Logs ==="
kubectl logs $POD
echo -e "\n=== Events ==="
kubectl get events --field-selector involvedObject.name=$POD
EOF
chmod +x ~/debug.sh
# 使用: ~/debug.sh my-pod-name
```

# Week 9 - Kubernetes 生产核心命令速查表

> ✅ 所有命令均在 kubeadm v1.28+ 集群验证
> 💡 使用原则：能复制、能执行、能解决问题

---

## 🔹 kubeadm 集群搭建与管理

```bash
# 初始化 Master 节点（关键：指定 CIDR）
sudo kubeadm init --pod-network-cidr=192.168.0.0/16 --image-repository=registry.aliyuncs.com/google_containers

# 配置 kubectl（Master 节点）
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Worker 节点加入集群（命令由 kubeadm init 输出提供）
sudo kubeadm join <master-ip>:6443 --token <token> --discovery-token-ca-cert-hash sha256:<hash>

# 重置节点（出错时清理环境）
sudo kubeadm reset
sudo rm -rf ~/.kube/
```

---

## 🔹 **持久化存储 (PV/PVC)**

```ibash
# 查看存储状态
kubectl get pv
kubectl get pvc

# 创建 PV/PVC 后，检查绑定状态
kubectl describe pv <pv-name>
kubectl describe pvc <pvc-name>

# 在 Pod 中使用 PVC
volumeMounts:
  - name: data-volume
    mountPath: /var/lib/mysql
volumes:
  - name: data-volume
    persistentVolumeClaim:
      claimName: mysql-pvc

# 动态创建 PVC（使用 StorageClass）
kubectl create pvc mysql-pvc --size=10Gi --storage-class=standard
```

---

## 🔹 资源管理 (Requests/Limits) & PDB

```bash
# 查看 Pod 资源分配和使用
kubectl describe pod <pod-name> | grep -A5 -B5 "Limits\|Requests"
kubectl top pods

# 创建 PodDisruptionBudget (PDB)
kubectl create pdb my-pdb --selector=app=my-app --min-available=1
# 或通过 YAML
echo '
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: my-pdb
spec:
  minAvailable: 1
  selector:
    matchLabels:
      app: my-app
' | kubectl apply -f -
```

---

## 🔹 Helm 包管理器

```bash
# 安装 Helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# 核心操作
helm search repo nginx          # 搜索 Chart
helm repo add bitnami https://charts.bitnami.com/bitnami # 添加仓库
helm install my-release bitnami/nginx # 安装
helm list                       # 列出已安装的 Release
helm upgrade my-release bitnami/nginx --set service.type=NodePort # 升级
helm rollback my-release 1      # 回滚到版本1
helm uninstall my-release       # 卸载

# 调试
helm template my-release ./my-chart > rendered.yaml # 本地渲染模板
helm get values my-release      # 查看当前生效的 values
```

---

## 🔹 多租户与 RBAC

```bash
# 命名空间管理
kubectl create ns dev-team
kubectl config set-context --current --namespace=dev-team # 切换默认 ns

# 创建 ServiceAccount 和角色绑定
kubectl create sa dev-sa -n dev-team
kubectl create role dev-role --verb=get,list,create --resource=pods,deployments -n dev-team
kubectl create rolebinding dev-binding --role=dev-role --serviceaccount=dev-team:dev-sa -n dev-team

# 获取 SA 的 Token（用于配置新 kubeconfig）
kubectl create token dev-sa -n dev-team --duration=24h
```

---

**✨**  **小技巧**

```bash
# 1. 快速查看所有命名空间下的 PVC 状态
kubectl get pvc -A

# 2. 强制删除卡住的 PV/PVC
kubectl patch pvc <pvc-name> -p '{"metadata":{"finalizers":null}}'
kubectl patch pv <pv-name> -p '{"metadata":{"finalizers":null}}'

# 3. 为 kubectl 设置别名（永久生效）
echo 'alias k=kubectl' >> ~/.bashrc
echo 'alias kg="kubectl get"' >> ~/.bashrc
echo 'alias kd="kubectl describe"' >> ~/.bashrc
source ~/.bashrc
# 使用: kg po, kd svc/my-svc
```

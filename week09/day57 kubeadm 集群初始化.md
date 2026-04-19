# 📖 Day 57 笔记：kubeadm 集群初始化

---

## ✅ 今日任务完成情况

- [X] 在 Master 节点完成 kubeadm 前置配置
- [X] **使用** `kubeadm init` **初始化集**群****
- [X] 在 Worker 节点成功加入集群
- [X] `所有节点状态为 Ready`

---

## 🔧 关键操作记录

```bash
# 在所有节点上（Master & Worker）
# 1. 禁用 swap
sudo swapoff -a
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab

# 2. 加载内核模块
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF
sudo modprobe overlay
sudo modprobe br_netfilter

# 3. 安装 containerd 和 kubeadm/kubelet/kubectl
# ... (此处省略具体安装步骤)

# 在 Master 节点
# 4. 初始化集群 (关键: 指定 pod-network-cidr)
sudo kubeadm init --pod-network-cidr=192.168.0.0/16

# 5. 配置 kubectl
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# 在 Worker 节点
# 6. 运行 kubeadm join 命令 (由 init 输出提供)
sudo kubeadm join <master-ip>:6443 --token <token> --discovery-token-ca-cert-hash sha256:<hash>

# 验证
kubectl get nodes
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**`kubeadm init` **卡在** `[wait-control-plane]`，因为无法拉取镜像。
  **解决** **：使用国内镜像源。先** `kubeadm config images list` **查看所需镜像，然后手动** `crictl pull` **或使用** `--image-repository` **参数：**

  ```bash
  kubeadm init --image-repository registry.aliyuncs.com/google_containers --pod-network-cidr=192.168.0.0/16
  ```
* **问题** **：Worker 节点加入后状态为** `NotReady`。
  **解决** **：这是正常的，因为还没安装 CNI 网络插件。下一步就是装 Calico。**

---

## 💡 小技巧 / 收获

* **`--pod-network-cidr` **必须与后续 CNI 插件的 CIDR 一致**** **，否则 Pod 无法通信。**
* **`kubeadm reset` **是清理环境的利器**** **，出错时果断重来。**

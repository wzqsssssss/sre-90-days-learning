# 📖 Day 70 笔记：自定义 Operator 入门

---

## ✅ 今日任务完成情况

- [X] **理解 Operator 模式和工作原理**
- [X] ******使用** `operator-sdk` **创建项目******
- [X] **定义** `MyApp` **CRD 并编写简单 Reconcile 逻辑**
- [X] 部署 Operator 并验证功能

---

## 🔧 关键操作记录

```bash
# 1. 安装 operator-sdk
# (过程略)

# 2. 创建新项目
operator-sdk init --domain=my.domain --repo=my-operator

# 3. 创建 API (CRD + Controller)
operator-sdk create api --group=apps --version=v1alpha1 --kind=MyApp --resource --controller

# 4. 修改 pkg/apis/apps/v1alpha1/myapp_types.go 定义 Spec/Status
// MyAppSpec defines the desired state of MyApp
type MyAppSpec struct {
    Size int32 `json:"size"`
}

// MyAppStatus defines the observed state of MyApp
type MyAppStatus struct {
    Nodes []string `json:"nodes"`
}

# 5. 修改 controllers/myapp_controller.go 的 Reconcile 函数
// 核心逻辑: 如果不存在 Deployment，则创建一个副本数为 spec.size 的 Deployment

# 6. 构建并部署
make docker-build docker-push IMG=<your-registry>/my-operator:v0.0.1
make deploy IMG=<your-registry>/my-operator:v0.0.1

# 7. 创建自定义资源
# myapp-sample.yaml
apiVersion: apps.my.domain/v1alpha1
kind: MyApp
metadata:
  name: myapp-sample
spec:
  size: 3

kubectl apply -f myapp-sample.yaml
kubectl get deployments # 应看到一个名为 myapp-sample 的 Deployment，副本数为3
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：Operator Pod 启动失败，报错权限不足。**
  **解决** **：RBAC 权限未配置完整。**`operator-sdk` **会自动生成** `config/rbac/` **目录下的文件，确保它们被正确应用。**

---

## 💡 小技巧 / 收获

* **Operator = CRD + Controller** **。CRD 定义新资源，Controller 实现业务逻辑。**
* **Reconcile 循环是核心** **：它不断将“实际状态”向“期望状态”收敛。**
* **虽然只写了 Demo，但已掌握 Operator 开发的核心范式** **。**

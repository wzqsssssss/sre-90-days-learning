# Week 11 - Prometheus & Kubernetes 运维速查表

> ✅ 所有命令均在 kubectl v1.28+ 集群验证
> 💡 使用原则：能复制、能执行、能解决问题

---

## 🔹 Helm 与 Prometheus Stack 操作

```bash
# 添加官方 Helm 仓库
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# 安装 kube-prometheus-stack（含 Prometheus + Grafana + Alertmanager）
kubectl create ns monitoring
helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack -n monitoring

# 升级/卸载
helm upgrade kube-prometheus-stack prometheus-community/kube-prometheus-stack -n monitoring
helm uninstall kube-prometheus-stack -n monitoring

# 查看 Helm Release 状态
helm list -n monitoring
```

---

## 🔹 端口转发快速访问组件

```ini
# 访问 Prometheus UI
kubectl port-forward svc/kube-prometheus-stack-prometheus 9090:9090 -n monitoring

# 访问 Grafana（默认账号 admin）
kubectl port-forward svc/kube-prometheus-stack-grafana 3000:80 -n monitoring

# 访问 Alertmanager
kubectl port-forward svc/kube-prometheus-stack-alertmanager 9093:9093 -n monitoring
```

---

## 🔹 获取默认密码（Grafana / Prometheus）

```bash
# Grafana admin 密码
kubectl get secret kube-prometheus-stack-grafana -n monitoring \
  -o jsonpath='{.data.admin-password}' | base64 -d && echo

# Prometheus 默认无密码，但若启用 basic-auth 可查 secret
```

---

## 🔹 ServiceMonitor 调试命令

```yml
# 查看所有 ServiceMonitor
kubectl get servicemonitor --all-namespaces

# 查看 Prometheus 抓取目标（Targets）
# 先 port-forward 到 Prometheus，然后访问 http://localhost:9090/targets

# 检查 Service 是否带正确 label（ServiceMonitor selector 匹配依据）
kubectl get svc <service-name> --show-labels

# 查看 Endpoints 是否生成（关键！）
kubectl get endpoints <service-name>
```

**常见失败原因** **：Service 的** `labels` **与 ServiceMonitor 的** `selector.matchLabels` **不一致**

---

## 🔹 常用 PromQL 查询

```promql
# 节点 CPU 使用率（排除 idle）
100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# 节点内存使用率
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100

# Pod 内存使用 Top 10
topk(10, sum by (pod, namespace) (container_memory_usage_bytes{container!="",container!="POD"}))

# K8s Deployment 副本状态（期望 vs 实际）
kube_deployment_spec_replicas != kube_deployment_status_replicas_available

# API Server QPS
sum(rate(apiserver_request_total[5m]))

# 检测 Down 的 Target
up == 0
```

---

## 🔹 告警规则管理

```bash
# 查看已加载的告警规则
kubectl get prometheusrule -n monitoring

# 应用自定义告警规则（YAML）
kubectl apply -f cpu-alert.yaml

# 在 Prometheus UI 验证：Alerts 标签页
# 在 Alertmanager UI 查看：http://localhost:9093
```

---

## 🔹 日志与排错命令

```bash
# 查看 Prometheus Pod 日志
kubectl logs -l app=kube-prometheus-stack-prometheus -n monitoring -c prometheus

# 查看 Operator 日志（负责同步 ServiceMonitor）
kubectl logs -l app=kube-prometheus-stack-operator -n monitoring

# 检查 CRD 是否安装（ServiceMonitor 依赖）
kubectl get crd servicemonitors.monitoring.coreos.com

# 查看 Pod 事件（排查调度/拉镜像失败）
kubectl describe pod <prometheus-pod-name> -n monitoring
```

---

## 🔹 Grafana 快速配置

```text
# 数据源（Data Source）自动配置为 Prometheus（由 Helm 完成）
# 导入 Dashboard：
#   → Dashboards → Import → 输入 ID（如 1860）
#   → 选择 Prometheus 数据源

# 常用 Dashboard ID：
#   1860 → Node Exporter Full
#    315 → Kubernetes Cluster Monitoring
#   6417 → Kubernetes Pods
#  11074 → Kubernetes Deployments
```

---

## 🔹 自定义应用暴露指标（Python 示例）

```python
# 安装依赖
pip install prometheus_client flask

# 在 Flask 中暴露 /metrics
from prometheus_client import Counter, generate_latest
from flask import Flask

app = Flask(__name__)
REQUESTS = Counter('app_requests_total', 'Total requests')

@app.route('/')
def home():
    REQUESTS.inc()
    return "OK"

@app.route('/metrics')
def metrics():
    return generate_latest()

# 应用需监听 0.0.0.0，并在 Service 中暴露对应端口
```

---

**✨**  **小技巧**

```bash
# 快速创建测试 Pod（带 curl）
kubectl run debug --image=busybox:1.28 --rm -it --restart=Never -- sh

# 在集群内测试服务连通性
curl http://nginx-demo.default.svc:80/metrics

# 临时编辑资源（如 Service）
kubectl edit svc nginx-demo

# 查看所有命名空间的 Pod
kubectl get pods --all-namespaces

# 保存当前集群状态快照（用于对比）
kubectl get all -A > cluster-before.txt

# 遇到监控不生效？按顺序检查：
1️⃣ 应用是否暴露 /metrics？
2️⃣ Service 是否有正确 labels？
3️⃣ ServiceMonitor selector 是否匹配？
4️⃣ Endpoints 是否非空？
5️⃣ Prometheus Targets 页面是否显示 UP？
```

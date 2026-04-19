# 📖 Day 50 笔记：Service 类型与外部访问

---

## ✅ 今日任务完成情况

- [X] 理解 ClusterIP / NodePort / LoadBalancer 区别
- [X] 将 Service 改为 NodePort 类型
- [X] `从宿主机浏览器访问应用`

---

## 🔧 关键操作记录

```yml
# service-nodeport.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30080  # 可选，范围 30000-32767
```

```bash
# 获取 Minikube IP（若使用 Minikube）
minikube ip

# 访问服务（假设 nodePort=30080）
curl http://<NODE_IP>:30080
# 或在浏览器打开 http://<NODE_IP>:30080
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：浏览器无法访问** `http://localhost:30080`
  **解决** **：Minikube 运行在 Docker VM 中，需用** `minikube ip` **获取真实 IP，而非 localhost。**

---

## 💡 小技巧 / 收获

* **NodePort = ClusterIP + 主机端口映射** **。**
* **生产环境通常用 Ingress 或 Gateway API** **，NodePort 仅用于测试或简单暴露。**

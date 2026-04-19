# 📖 Day 48 笔记：Service 基础

---

## ✅ 今日任务完成情况

- [X] **创建 ClusterIP Service**
- [X] `从集群内访问服务`
- [X] **理解 Service 虚拟 IP 机制**

---

## 🔧 关键操作记录

```yml
# service-nginx.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

```bash
# 测试访问（临时启动 busybox）
kubectl run -it --rm debug --image=busybox:1.28 --restart=Never -- sh
/ # wget -qO- http://nginx-svc
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：在 busybox 中** `nslookup nginx-svc` **失败**
  **解决** **：旧版 busybox DNS 工具有 bug，改用** `1.28+` **版本或直接** `wget` **测试连通性。**

---

## 💡 小技巧 / 收获

* **Service 是稳定的网络端点** **，即使后端 Pod IP 变化，Service IP 不变。**
* **ClusterIP 只能在集群内部访问** **。**

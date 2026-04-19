# 📖 Day 51 笔记：ConfigMap 与 Secret

---

## ✅ 今日任务完成情况

- [X] 创建 ConfigMap 存储配置
- [X] `创建 Secret 存储密码`
- [X] `将它们挂载到 Pod`

---

## 🔧 关键操作记录

```yml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  log_level: "info"
  app.conf: |
    port=8080
    debug=false
```

```yml
# secret.yaml（值需 base64 编码）
echo -n 'mysecretpassword' | base64
# 输出: bXlzZWNyZXRwYXNzd29yZAo=

apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  password: bXlzZWNyZXRwYXNzd29yZAo=
```

```yml
# pod-using-config.yaml
spec:
  containers:
  - name: app
    image: nginx
    env:
      - name: LOG_LEVEL
        valueFrom:
          configMapKeyRef:
            name: app-config
            key: log_level
    volumeMounts:
      - name: config-volume
        mountPath: /etc/config
  volumes:
    - name: config-volume
      configMap:
        name: app-config
```

```bash
kubectl apply -f configmap.yaml -f secret.yaml -f pod-using-config.yaml
kubectl exec -it <pod> -- cat /etc/config/app.conf
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：Secret 的值末尾多出换行符**
  **解决** **：使用** `echo -n` **而非** `echo`，避免自动添加 `\n`。

---

## 💡 小技巧 / 收获

* **Secret 不是加密的！** **仅做 base64 编码，需配合 etcd 加密或外部 Vault 使用。**
* **ConfigMap/Secret 更新后，挂载为 volume 的文件会自动更新（约 1 分钟延迟）** **。**

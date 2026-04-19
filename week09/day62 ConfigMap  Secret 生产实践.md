# 📖 Day 62 笔记：ConfigMap / Secret 生产实践

---

## ✅ 今日任务完成情况

- [X] **将应用配置提取到 ConfigMap**
- [X] `将敏感信息存入 Secret`
- [X] **通过 Volume 和 Env 注入**

---

## 🔧 关键操作记录

```yml
# secret-db.yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  username: YWRtaW4= # echo -n 'admin' | base64
  password: MWYyZDFlMmU2N2Rm # echo -n '1f2d1e2e67df' | base64
```

```
# deployment-with-secret.yaml
spec:
  containers:
    - name: app
      image: my-app
      env:
        - name: DB_USER
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: username
      volumeMounts:
        - name: config-volume
          mountPath: /etc/app/config
  volumes:
    - name: config-volume
      configMap:
        name: app-config
```

```bash
# 验证
kubectl exec -it <pod> -- printenv | grep DB_USER
kubectl exec -it <pod> -- cat /etc/app/config/app.conf
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：应用读取 Secret 时值末尾有奇怪字符。**
  **解决** **：确保使用** `echo -n` **生成 base64，避免换行符被编码进去。**

---

## 💡 小技巧 / 收获

* **永远不要在代码或镜像中硬编码配置和密钥** **。**
* **Secret 默认未加密** **，生产环境应启用 etcd 加密或集成外部 Vault。**

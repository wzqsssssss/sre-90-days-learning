# 📖 Day 68 笔记：Job 与 CronJob

---

## ✅ 今日任务完成情况

- [X] **创建并运行一个 Job**
- [X] `创建并验证一个 CronJob`
- [X] **理解 Job 的 completions 和 parallelism**

---

## 🔧 关键操作记录

```yml
# job-migration.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: db-migration
spec:
  template:
    spec:
      containers:
        - name: migrator
          image: busybox:1.28
          command: ["sh", "-c", "echo 'Running migration...'; sleep 10; echo 'Done!'"]
      restartPolicy: OnFailure
```

```bash
# cronjob-backup.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: daily-backup
spec:
  schedule: "*/2 * * * *" # 每2分钟一次，用于测试
  jobTemplate:
    spec:
      template:
        spec:
          containers:
            - name: backup
              image: busybox:1.28
              command: ["sh", "-c", "echo 'Backup at $(date)'"]
          restartPolicy: OnFailure
```

```bash
kubectl apply -f job-migration.yaml
kubectl get jobs
kubectl logs job/db-migration

kubectl apply -f cronjob-backup.yaml
kubectl get cronjobs
# 等待几分钟后
kubectl get jobs
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：CronJob 没有按计划创建 Job。**
  **解决** **：检查** `schedule` **语法是否正确（5个字段），并确认** `startingDeadlineSeconds` **设置。**

---

## 💡 小技巧 / 收获

* **Job 用于一次性任务，CronJob 用于周期性任务** **。**
* **`restartPolicy` **对 Job 很重要，通常设为** `OnFailure` **或** `Never`** **。**

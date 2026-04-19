# 📖 Day 61 笔记：Helm 入门与应用打包

---

## ✅ 今日任务完成情况

- [X] **安装 Helm CLI**
- [X] 创建自定义 Helm Chart
- [X] 使用 Helm 部署和升级应用

---

## 🔧 关键操作记录

```yml
# 安装 Helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# 创建 Chart
helm create my-web-app
# 修改 templates/ 下的 deployment.yaml 和 service.yaml 以匹配你的应用

# 查看生成的清单
helm template my-release ./my-web-app

# 部署
helm install my-release ./my-web-app

# 升级 (修改 values.yaml 后)
helm upgrade my-release ./my-web-app

# 查看历史版本
helm history my-release

# 卸载
helm uninstall my-release
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**`helm install` **报错模板渲染失败。**
  **解决** **：YAML 模板语法错误。使用** `helm template` **先本地渲染，检查输出是否合法。**

---

## 💡 小技巧 / 收获

* **Chart 是 Helm 的打包单元** **，包含** `Chart.yaml`, `values.yaml`, `templates/`。
* **`values.yaml` **是配置中心**** **，所有可变参数都应放在这里。**
* **Helm Release 是 Chart 的一次部署实例** **。**

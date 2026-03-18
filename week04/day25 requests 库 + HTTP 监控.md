# 📖 Day 25 笔记：requests 库 + HTTP 监控

---

## ✅ 今日任务完成情况

- [X] **安装** `requests`：`pip install requests`
- [X] 编写 URL 可用性检测脚本
- [X] 添加超时和异常处理

---

## 🔧 关键操作记录

```python
import requests

def check_url(url, timeout=5):
    try:
        resp = requests.get(url, timeout=timeout)
        return resp.status_code == 200, resp.elapsed.total_seconds()
    except requests.RequestException as e:
        return False, str(e)

ok, latency = check_url("https://httpbin.org")
print(f"OK: {ok}, Latency: {latency:.2f}s")
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：未安装 requests 报** `ModuleNotFoundError`
  **解决** **：先运行** `python -m pip install requests`

---

## 💡 小技巧 / 收获

* `requests.get().elapsed` **可测响应时间**
* **生产环境建议加 User-Agent 模拟浏览器**

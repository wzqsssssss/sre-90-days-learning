# 📖 Day 26 笔记：整合系统监控脚本

---

## ✅ 今日任务完成情况

- [X] 整合磁盘、内存检查逻辑
- [X] 超过阈值（如磁盘>80%）打印告警
- [X] **脚本命名为** `system_monitor.py` **并测试通过**

---

## 🔧 关键操作记录

```python
import shutil

def check_disk_usage(threshold=80):
    usage = shutil.disk_usage("/")
    total = usage.total
    free = usage.free
    used_pct = (total - free) / total * 100
    if used_pct > threshold:
        print(f"⚠️ 磁盘使用率过高: {used_pct:.1f}%")
        return False
    return True
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**`shutil.disk_usage()` **返回字节，数字太大不好读**
  **解决** **：除以** `1024**3` **转 GB，或直接算百分比**

---

## 💡 小技巧 / 收获

* `shutil.disk_usage("/")` **是跨平台获取磁盘信息的好方法**

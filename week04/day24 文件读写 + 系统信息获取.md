# 📖 Day 24 笔记：文件读写 + 系统信息获取

---

## ✅ 今日任务完成情况

- [X] **用** `with open()` **读写文件**
- [X] **通过** `subprocess` **执行** `df -h` **和** `free -h`
- [X] **输出结果写入** `sysinfo.log`

---

## 🔧 关键操作记录

```bash
# Shell 命令参考（Python 中调用）
df -h          # 磁盘使用
free -h        # 内存使用
```

```python
import subprocess

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

disk_info = run_cmd("df -h")
with open("sysinfo.log", "w") as f:
    f.write(disk_info + "\n")
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：**`subprocess` **中文乱码**
  **解决** **：加** `text=True` **或指定** `encoding='utf-8'`

---

## 💡 小技巧 / 收获

* **永远用** `with open()`，自动关闭文件
* `os.popen()` **也可执行命令，但** `subprocess` **更安全灵活**

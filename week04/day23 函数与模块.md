# 📖 Day 23 笔记：函数与模块

---

## ✅ 今日任务完成情况

- [X] 定义3个自定义函数（带参数和返回值）
- [X] **使用** `import os`, `import time`
- [X] **完成** `day2_functions.py`

---

## 🔧 关键操作记录

```python
import os
import time

def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def join_path(*parts):
    return os.path.join(*parts)

def avg(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：函数内部修改全局变量报错**
  **解决** **：如需修改，需在函数内声明** `global var_name`

---

## 💡 小技巧 / 收获

* **函数文档用三引号写 docstring，可用** `help(func)` **查看**
* `*args` **和** `**kwargs` **可接收任意参数**

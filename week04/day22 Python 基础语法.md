# 📖 Day 22 笔记：Python 基础语法

---

## ✅ 今日任务完成情况

- [X] 学习变量、数据类型（int, str, bool, list, dict）
- [X] 掌握 if/else、for/while 循环
- [X] **编写5个小练习程序并保存为** `day1_basics.py`

---

## 🔧 关键操作记录

```python
# 判断奇偶
num = 7
print("偶数" if num % 2 == 0 else "奇数")

# 遍历字典
info = {"cpu": "4核", "mem": "8GB"}
for k, v in info.items():
    print(f"{k}: {v}")

# 列表推导式
squares = [x**2 for x in range(5)]
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **： `list.append()` **返回** `None`，误以为能链式调用**
  **解决** **：**理解** `append()` **是原地修改，不返回新列表****

---

## 💡 小技巧 / 收获

* Python 使用缩进代替大括号，****4空格是标准**
* **用** `type(x)` **快速查看变量类型**
* **字符串格式化推荐 f-string：**`f"值: {value}"`

# 📖 Day 9 笔记：条件控制：if / test / [ ]

---

## ✅ 今日任务完成情况

- [X] 编写脚本判断目录是否存在，不存在则创建

---

## 🔧 关键操作记录

```bash
# 条件判断示例
#!/bin/bash
target_dir="/opt/myapp"

if [ -d " $ target_dir" ]; then
    echo "Directory exists. Listing contents:"
    ls -l " $ target_dir"
else
    echo "Directory not found. Creating..."
    mkdir -p " $ target_dir"
    echo "Created  $ target_dir"
fi
```

---


## ⚠️ 遇到的问题 & 解法

* **问题** **：**变量赋值时写了** `name = "test"`，报错 `command not found`**
  **解决** **：**Shell 中变量赋值**  **不能有空格** **，必须写成** `name="test"`**

---

## 💡 小技巧 / 收获

* `[ -d path ]`：目录存在？
* `[ -f file ]`：普通文件存在？
* `[ -z "$var" ]`：变量为空？
* **注意引号：**`[ -d "$dir" ]` **防止路径含空格出错**

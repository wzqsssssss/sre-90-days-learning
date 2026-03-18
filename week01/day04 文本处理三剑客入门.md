# 📖 Day 4 笔记：grep / sed / awk 实战

---

## ✅ 今日任务完成情况

- [X] 能用 grep/sed/awk 分析 /etc/passwd 和模拟日志
- [X] 完成 3 个文本提取任务

---

## 🔧 关键操作记录

```bash
# 提取所有用户名（/etc/passwd 第1列）
awk -F: '{print $1}' /etc/passwd

# 找出 UID >= 1000 的普通用户
awk -F: '$3 >= 1000 {print $1, $3}' /etc/passwd

# 模拟日志并过滤
echo -e "INFO: started\nERROR: disk full\nWARN: high load\nERROR: timeout" > ~/app.log
grep -i "error" ~/app.log          # 找错误
sed 's/ERROR/CRITICAL/g' ~/app.log # 临时替换
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **：`sed -i` **修改后文件变空****
  **解决** **：**原命令写错成** `sed -i '/pattern/d'` **误删了所有行；应先用无** `-i` **版本预览****

---

## 💡 小技巧 / 收获

* `grep -E` **支持扩展正则（如** `grep -E 'error|fail'`）
* `awk` **默认以空格或 tab 分隔，用** `-F:` **指定冒号分隔**
* **日志分析黄金组合：**`tail -f log | grep ERROR`

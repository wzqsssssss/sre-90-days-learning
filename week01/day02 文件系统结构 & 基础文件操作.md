# 📖 Day 2 笔记：文件系统 & 基础命令

---

## ✅ 今日任务完成情况

- [X] 理解 /, /home, /etc, /var, /usr 等核心目录作用
- [X] 熟练使用 12+ 基础文件命令完成操作任务

---

## 🔧 关键操作记录

```bash
# 创建练习目录
mkdir -p ~/lab/{docs,logs,scripts}

# 创建并复制文件
touch ~/lab/docs/readme.txt
cp ~/lab/docs/readme.txt ~/lab/docs/README.bak

# 查看文件内容
echo "Hello SRE" > ~/lab/docs/readme.txt
cat ~/lab/docs/readme.txt

# 移动与删除
mv ~/lab/docs/README.bak ~/lab/
rm ~/lab/README.bak
```

---

## ⚠️ 遇到的问题 & 解法

* **问题** **： `rm -rf /*` **误输入****
  **解决** **：**立刻按** `Ctrl+C` **中断；以后加别名防护：****

  ```bash
  echo "alias rm='rm -i'" >> ~/.bashrc
  ```

---

## 💡 小技巧 / 收获

* `/etc`：配置文件集中地
* `/var/log`：日志默认位置
* `tree` **命令可直观显示目录结构（需** `apt install tree`）

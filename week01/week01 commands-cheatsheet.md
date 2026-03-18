# Week 1 - Linux 命令速查表

> ✅ 所有命令均在 Ubuntu 24.04 验证
> 💡 使用原则：能复制、能执行、能解决问题

---

## 🔹 文件与目录操作

```bash
ls -l                 # 详细列表
ls -a                 # 显示隐藏文件
pwd                   # 当前路径
cd /path              # 切换目录
mkdir -p a/b/c        # 递归创建目录
touch file.txt        # 创建空文件
cp src dest           # 复制
mv old new            # 移动/重命名
rm -f file            # 强制删除文件
rm -rf dir            # 强制删除目录（慎用！）
cat file              # 查看全文
less file             # 分页查看（按 q 退出）
head -n 10 file       # 查看前10行
tail -f /var/log/syslog  # 实时跟踪日志
```

---

## 🔹 权限与用户管理

```bash
chmod 755 file        # rwxr-xr-x
chmod u+x script.sh   # 给属主加执行权限
chown user:group file # 修改属主和属组
useradd -m testuser   # 创建用户并建家目录
passwd testuser       # 设置密码
su - testuser         # 切换用户
id                    # 查看当前用户 UID/GID
groups                # 查看所属组
sudo systemctl restart ssh  # 以 root 权限重启服务
```

---

## 🔹 文本处理三剑客

```bash
# grep：搜索
grep "error" /var/log/syslog
grep -i "Error" file          # 忽略大小写
grep -v "debug" file          # 反向匹配（不含 debug 的行）
grep -r "TODO" /etc/          # 递归搜索目录

# sed：流编辑（常用替换）
sed 's/foo/bar/g' file        # 输出替换结果（不改原文件）
sed -i 's/foo/bar/g' file     # 直接修改文件（⚠️ 小心！）

# awk：列处理
awk -F: '{print $1}' /etc/passwd    # 打印 passwd 第1列（用户名）
awk '$3 > 1000 {print $1}' /etc/passwd  # UID>1000 的用户
```

---

## 🔹 进程与系统监控

```bash
ps aux | grep nginx          # 查找 nginx 进程
top                          # 实时资源监控（按 q 退出）
htop                         # 更友好的 top（需 apt install htop）
kill -9 <PID>                # 强制终止进程
systemctl status ssh         # 查看服务状态
systemctl start/stop/restart ssh
```

---

## 🔹 网络与包管理

```bash
ip a                         # 查看 IP 地址（替代 ifconfig）
ping -c 4 google.com         # 测试连通性
apt update                   # 更新软件包列表（Ubuntu）
apt install vim curl net-tools -y
# CentOS: dnf install vim curl -y

man ls                       # 查看命令手册
command --help               # 快速帮助
```

---

## 🔹 环境与脚本

```bash
echo  $ PATH                   # 查看环境变量
export PATH= $ PATH:/my/script # 临时添加路径
vim ~/.bashrc                # 永久添加 PATH（末尾加 export 行）
source ~/.bashrc             # 重载配置
```

**✨**  **小技巧** **：把常用命令存为别名**

```bash
1echo"alias ll='ls -lh'">> ~/.bashrc
2source ~/.bashrc
```

#/bin/bash

#检查用户，版本，磁盘

# 定义变量
USER_NAME=$(whoami)
OS_VERSION=$(awk -F= '/^PRETTY_NAME/ {print $2}' /etc/os-release|tr -d '"')
DISK_USAGE=$(df / |awk 'NR==2 {print $5}')

# 字符串拼接
MESSAGE="您好,${USER_NAME}用户.当前系统版本是：${OS_VERSION}。根分区磁盘使用率为：${DISK_USAGE}。"

# 输出信息
echo "$MESSAGE"

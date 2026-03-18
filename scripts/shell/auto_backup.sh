#!/bin/bash

#自动备份目录为带日期的tar.gz

usage(){
    echo "用法：$0 <源目录>[目标备份目录]"
    echo "示例：$0 /var/www /backup"
    exit 1
}

SOURCE_DIR="${1:-}"
BACKUP_ROOT="${2:-/backup}"

if [[ -z "$SOURCE_DIR" ]];then
    echo "未指定源目录"
    usage
fi

if [[ ! -d "$SOURCE_DIR" ]];then
    echo "源目录'$SOURCE_DIR'不存在！"
    exit 1
fi

SOURCE_DIR="$(cd "$SOURCE_DIR" && pwd)"
if [[ -z "$SOURCE_DIR" ]];then
    echo "无法解析源目录"
    exit 1
fi

#如果备份目录不存在则创建
sudo mkdir -p "$BACKUP_ROOT" 2>/dev/null ||{
    echo "无法创建或访问备份目录'$BACKUP_ROOT'"
    exit 1
}

#生成带日期的文件名
DATE=$(date +%Y%m%d)
BASENAME=$(basename "$SOURCE_DIR")
BACKUP_FILE="$BACKUP_ROOT/backup_$(BASENAME)_${DATE}.tar.gz"

echo "开始备份：$SOURCE_DIR -> $BACKUP_FILE"

#执行备份
if tar -cvf "$BACKUP_FILE" -C "$(dirname "$SOURCE_DIR")" "$BASENAME" 2>/dev/null;then
    SIZE=$(du -sh "BACKUP_FILE"|cut -f1)
    echo "备份成功！大小：$SIZE"
    echo "备份文件：$BACKUP_FILE"
else
    echo "备份失败！请检查权限或磁盘空间"
    exit 1
fi


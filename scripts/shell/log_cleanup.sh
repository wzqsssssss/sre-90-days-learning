#/bin/bash

#日志清理：删除过期的.log文件

#获取脚本执行的绝对路径
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

#操作日志备份
LOG_FILE="$SCRIPT_DIR/clean.log"

#$*将输出传递个每一个参数
log(){
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $*" >> "$LOG_FILE"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $*"
}

#如果没提供参数，默认为当前目录
TARGET_DIR="${1:-.}"

#检查目录是否存在
if [[ ! -d "$TARGET_DIR" ]];then
    log "错误的目标路径 '$TARGET_DIR'不存在！"
    exit 1
fi

#将路径转换为绝对路径
TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"
if [[ -z "$TARGET_DIR" ]];then
    echo "错误的路径"
    exit 1
fi

#查找并删除7天前的.log文件
log "开始清理目标路径：$TARGET_DIR"

#使用 find 安全查找 .log 文件（只匹配以 .log 结尾的普通文件）
#-mtime +7 表示“修改时间在7*24小时之前”
#注意：+7 = 大于7天，即8天及以上
#< <比起管道符号，不会创建子进程，导致写入空数据，比起$()不会额外触发分词，不会额外解析*和?
mapfile -t old_logs < <(find "$TARGET_DIR" -type f -name "*.log" -mtime +7 2>/dev/null)

if [[ ${#old_logs[@]} -eq 0 ]]; then
    log "未发现过期的.log 文件，无需清理。"
else
    log "发现 ${#old_logs[@]} 个过期日志文件，开始删除..."
    
    delete=0
    for file in "${old_logs[@]}";do
        if rm -f "$file" 2>/dev/null;then
            log "已删除：$file"
	    ((delete++))
	else
	    log "无法删除文件：'$file'"
	fi
    done
    log "清理完成：共清理$delete个文件"
fi

log "本次清理完成"
echo ”操作日志已添加到：$LOG_FILE“

#!/bin/bash

#web服务监控

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

LOG_FILE="$SCRIPT_DIR/service_monitor.log"

log(){
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $*"|tee -a "$LOG_FILE"
}

ALERT(){
    #模拟告警
    #echo "[ALERT] $(date):$*" >&2
    echo "$*"|mail -s "Service Down ALERT" 595794339@qq.com
}

# 默认检查nginx和httpd
SERVICES=()
if [[ $# -gt 0 ]];then
    SERVICES=($@)
else
    SERVICES=("nginx" "httpd")
fi

for svc in "${SERVICES[@]}";do
    log "检查服务：$svc"
   
    if systemctl is-active --quiet "$svc" 2>/dev/null;then
        log "服务“$svc”正在运行"
    else
        log "服务'$svc'未运行！正在尝试重启..."
	ALERT "服务'$svc'已停止，正在自动重启！"

	if sudo systemctl restart "$svc" 2>/dev/null;then
	    if systemctl is-active --quiet "$svc";then
	        log "服务‘$svc’重启成功"
		ALERT "服务'$svc'已经恢复启动！"
	    else
		log "服务'$svc'重启失败"
		ALERT "服务'$svc'重启失败，请人工介入！"
	    fi
	else
            log "无法执行systemctl restart"
	    ALERT "服务'$svc'重启命令执行失败！请检查服务名或权限"
        fi
    fi
done

log "本轮监控结束"

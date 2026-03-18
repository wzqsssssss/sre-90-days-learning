#/bin/bash

#检查服务状态，传入restart参数会重启

check_service(){
    local service_name="$1"
    if systemctl is-active --quiet "$service_name";then
        echo "服务'$service_name'正在运行"
	return 0
    else 
	echo "服务'$service_name'未运行或不存在"
	return 1
    fi
}

#重启服务
restart_service(){
    local service_name="$1"
    echo "正在尝试重启服务'$service_name'"    
    if  sudo systemctl restart "$service_name";then
        echo "服务'$service_name'重启成功"
	return 0
    else
	echo "服务'$service_name'重启失败？请检查服务名或权限是否正确"
	return 1
    fi
}

#主程序
if [ $# -lt 1 ];then
    echo "用法: $0 <服务名> [选项]"
    echo "示例: $0 nginx"
    echo "$0 nginx restart"
    exit 1
fi

SERVICE="$1"

ACTION="${2:-}"

check_service "$SERVICE"

if [[ "$ACTION" == "restart" ]]; then
    restart_service "$SERVICE"
fi

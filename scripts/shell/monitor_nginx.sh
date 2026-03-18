#!/bin/bash

#检查nginx是否正常运行

PROCESS_NAME="nginx"

echo "该服务是：$PROCESS_NAME (press Ctrl+C to stop)"

while true;do
    if pgrep -x "$PROCESS_NAME" > /dev/null;then
        echo "$(date):$PROCESS_NAME is running."
    else
        echo "$(date):$PROCESS_NAME is NOT running!"
	# sudo systemctl start nginx
    fi
    sleep 5
done

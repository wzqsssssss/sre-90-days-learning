#!/bin/bash

#统计/etc下有多少.log文件

count=0
for file in /etc/*.conf;do
    if [ -f "$file" ];then
       echo "找到文件: $file"
       ((count++))
    fi
done
echo "============================="
echo "/etc下的.conf文件有:$count个"


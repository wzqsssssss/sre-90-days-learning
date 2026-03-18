#/bin/bash

#如果目录不存在则创建

#读取用户输入
echo '请输入目录名：'
read DIR

if [[ -d "$DIR" ]];then
	echo "目录 '$DIR' 已存在，列出内容："
	ls "$DIR"
else
	mkdir -p "$DIR"
        echo '该目录之前不存在，现在已经创建！'	
fi

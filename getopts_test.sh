#!/bin/bash

# 初始化默认值
threshold=80                                        # 默认阈值为80
mount_point="/"                                     # 默认检查根目录

while getopts "t:m:h" opt; do    # 定义参数：t(阈值)、m(挂载点)、h(帮助)，后面的冒号表示该参数需要传值
	case $opt in
		t) threshold=$OPTARG ;;
		m) mount_point=$OPTARG ;;
		h) echo "用法: $0 [-t 阈值] [-m 挂载点]"     # 如果传了 -h，打印帮助信息
           	   echo "示例: $0 -t 90 -m /var"
           	   exit 0 ;;
		\?) echo "未知参数，请使用 -h 查看用法"      # 如果传了未定义的参数，提示错误
                    exit 1 ;;
	esac
done

echo "解析完成！即将检查挂载点：$mount_point，报警阈值：$threshold"
df -h "$mount_point" | tail -n 1                    # 执行实际检查命令

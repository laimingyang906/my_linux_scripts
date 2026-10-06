#!/bin/bash
USAGE=$(df -h / | tail -n 1 | awk '{print $5}' |sed 's/%//')

if [ $USAGE -gt 10 ]; then
	echo " 警告：磁盘快满了！当前使用率：$USAGE%" >> /var/log/disk_alert.log
fi

echo "当前磁盘使用率为:$USAGE%"

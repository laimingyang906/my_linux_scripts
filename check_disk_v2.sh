#!/bin/bash
set -euo pipefail

log() {
    local level="$1" #第一个参数是日志级别
    local level msg="$2" #第二个参数是日志内容
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] [$level] $msg"
}

check_disk(){
    local mount_point="$1" #接收挂载点参数
    local threshold="$2" #接收阈值参数
    local usage=$(df -h "$mount_point" | tail -n 1| awk '{print$5}' | sed 's/%//')

    if [ "$usage" -gt "$threshold" ]; then
        log "WARN" "挂载点$mount_point磁盘使用率：$usage%(超过阈值$threshold%)"
    else
        log "INFO" "挂载点 $mount_point 磁盘使用率：$usage% (正常)"
    fi
}


log "INFO" "服务器磁盘巡检启动"

# 定义要检查的挂载点数组
mount_points=("/" "/var" "/boot")

# 遍历所有挂载点并检查
for mp in "${mount_points[@]}"; do
    check_disk "$mp" 80                           # 调用函数，传入挂载点和80的阈值
done

log "INFO" "巡检结束"

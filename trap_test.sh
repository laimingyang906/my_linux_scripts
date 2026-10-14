#!/bin/bash

cleanup() {
    echo ""                                          # 打印空行，让输出好看一点
    echo "[$(date +'%H:%M:%S')] 捕获到中断信号，正在清理现场..."  # 提示用户正在清理
    rm -f /tmp/script_test.lock                      # 删除脚本产生的临时锁文件
    echo "[$(date +'%H:%M:%S')] 清理完成，脚本安全退出。"         # 提示清理完毕
    exit 0                                           # 以正常状态码退出脚本
}
trap cleanup SIGINT SIGTERM ERR

echo "脚本开始执行，创建临时锁文件..."
touch /tmp/script_test.lock                         # 模拟脚本运行时创建临时文件
echo "临时文件已创建：/tmp/script_test.lock"
echo "脚本正在执行重要任务（按 Ctrl+C 试着中断我）..."
sleep 30                                            # 模拟一个需要长时间执行的任务（睡眠30秒）
echo "任务执行完毕，正常退出。"

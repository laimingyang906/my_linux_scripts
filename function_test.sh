#!/bin/bash

log_info(){
    local message="$1"   # local声明局部变量，只在函数内部有效；$1代表传入函数的第一个参数
    echo "[$(date +'%Y-%m-%d %H:%M:%S')]" INFO:$message
}
add_num(){
    local num1=$1
    local num2=$2
    echo $((num1+num2))
}

log_info "脚本开始执行"
result=$(add_num 10 20)
log_info "10+20的计算结果是：$result"
log_info "脚本执行结束"

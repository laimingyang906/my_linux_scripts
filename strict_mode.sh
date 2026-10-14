#!/bin/bash
set -e  # 遇到任何命令返回非0状态（即执行失败）时，立即退出脚本，防止错误累积
set -u  #遇到未定义的变量时报错并退出，防止 rm -rf $DIR 中 $DIR 为空导致误删根目录
set -o pipefail # 管道命令中任何一个环节失败，整个管道就视为失败，防止错误被管道屏蔽

echo "第一步：正常执行"
ls /nonexistent
echo "第二步：这行永远不会被执行"

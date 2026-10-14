1/lsof谁在占用端口、谁在占用文件
(1)lsof -i :80
（2)sudo lsof /var/log/nginx/access.log
(3)sudo lsof +L1列出所有被删除但是仍然在被进程使用的文件
2、strace追踪进程的底层系统调用
(1)strace -f -t ls /var/www/html追踪ls命令的执行全过程
(2)strace -e trace=network curl -I http://www.baidu.com 追踪curl到底卡在哪一步
3/vmstat看整体健康度（CPU/内存/IO等）
vmstat 1 5 
r是等待运行的进程数、si/so是交换分区读写、wa是IO等待百分比...

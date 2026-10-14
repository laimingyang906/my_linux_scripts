网络排错黄金四步法：
1.检查网络物理链路是否通畅 ping -n 4 8.8.8.8 /结合ping和路由追踪mtr 8.8.8.8   2.网络通域名打不开一般是域名解析有问题 nslookup www.baidu.com 更强大也更详细 dig www.baidu.com  3.如果网络没有问题，查端口或者服务是否正常监听 （1）查远程端口连接性 nc -vz 网址 80（或者443）（2）sudo ss -tunlp...  4.如果底层网络、DNS、端口都没有问题，就是软件或者应用层的问题了 curl -v http://...或者查看程序内部的报错日志docker logs ...

以下补充：
1、检查端口通不通
nc -vz 39.106.44.177 80
不通是服务器挂了吗
sudo ss -tunlp | grep :80
如果服务没挂，那就可能是防火墙拦截了
sudo utf allow 90/tcp
2、是不是DNS的问题？
curl -v http://www.baidu.com
如果无法解析域名
看DNS是什么状态
dig www.baidu.com
如果超时或者报错就说明域名解析挂了，恢复并测试
/etc/resolv.conf nameserver那一行恢复然后测试curl -I http://www.baidu.com

3/端口不通，服务挂了
curl -v http://localhost从本机测试绕过防火墙
如果不行 再检查 sudo ss -tunlp | grep :80
什么都不输出就说明nginx没在跑
启动sudo systemctl start nginx再检查 curl -I hhttp://localhost

4/如果服务器连不上外网或者外边连不上服务器可以用
mtr -r -c 5 www.baidu.com看看数据包在哪个节点卡住了

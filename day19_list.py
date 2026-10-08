servers = ["192.168.1.1", "10.0.0.1", "8.8.8.8"]
print("服务器列表：", servers)
print("第一台服务器是:", servers[0])

for ip in servers:
	print(f"正在检查服务器：{ip}")

servers.append("39.106.44.177")
print("添加后，列表变成了：", servers)

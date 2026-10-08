server_info = {
	"ip": "39.106.44.177",
	"name": "my_cloud_server",
	"disk_usage":85,
	"status": "running"
}

print("服务器信息：", server_info)

print(f"服务器IP:{server_info['ip']}")


print(f"磁盘使用率:{server_info['disk_usage']}%")

server_info["disk_usage"] = 92
print(f"修改后的磁盘使用率: {server_info['disk_usage']}%")

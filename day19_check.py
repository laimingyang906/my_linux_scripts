servers = [
	{"ip": "192.168.1.1", "disk": 45, "status": "ok"},
	{"ip": "10.0.0.1", "disk": 85, "status": "ok"}, 
	{"ip": "8.8.8.8", "disk": 95, "status": "critical"},
	{"ip": "10.0.9.22", "disk": 70, "status": "ok"} 
]

for srv in servers:
	ip = srv["ip"]
	disk = srv["disk"]

	if disk >90:
		print(f"【严重警告】服务器{ip}磁盘使用率高达{disk}%!")
	elif disk > 80:
		print(f"【警告】服务器{ip}磁盘使用率较高：{disk}%!")
	else:
		print(f"【正常】服务器{ip}状态健康，磁盘使用率：{disk}%!")

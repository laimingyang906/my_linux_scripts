import requests

url = "http://39.106.44.177"

try:
	response = requests.get(url, timeout=5)
	status = response.status_code
	if status == 200:
		print(f"【正常】网站{url}运行健康，状态码：{status}")
	else:
	 	print(f"【警告】网站{url}运行异常，状态码：{status}")

except resquests.exceptions.RequestException as e:
	 print(f"【严重故障】无法访问{url}，错误原因：{e}")

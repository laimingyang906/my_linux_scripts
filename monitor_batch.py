import requests

urls = [
	"http://39.106.44.177",       # 你的服务器
    "https://www.baidu.com",       # 百度
    "https://github.com",          # GitHub
    "https://www.taobao.com",      # 淘宝
    "http://1.1.1.1",
	"https://httpbin.org/status/404",
	"https://httpbin.org/status/500"
]
print("开始批量巡检网站...\n")
 
for url in urls:
	try:
		response = requests.get(url,timeout=5)
		status = response.status_code
		if status ==200:
			print(f"[ok]{url} - 状态码：{status}")
		elif status == 404:
			print(f"[网页不存在或链接错误]{url} - 状态码：{status}")
		elif status == 500:
   			print(f"[服务器内部错误，请立即检查后端代码]{url} - 状态码：{status}")
		else:
			print(f"[WARN] {url} - 异常状态码：{status}")
	except requests.exceptions.RequestException as e:
		print(f"[FAIL] {url} -连接失败!")

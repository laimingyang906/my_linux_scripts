import logging
import requests
from datetime import datetime
# 配置日志（输出到文件 monitor.log，同时输出到屏幕）
logging.basicConfig(
    level=logging.INFO,  # 记录 INFO 及以上级别的日志
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("monitor.log", encoding='utf-8'),  # 写入日志文件
        logging.StreamHandler()                               # 打印到终端
    ]
)

def send_alert(url, error_msg):
	alert_text = f"【严重警告】网站{url}在{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}连接失败！原因：{error_msg}"
	logging.error(alert_text)
	with open("alert.log","a",encoding='utf-8') as f:
		f.write(alert_text + "\n")
	print("\003[91m"+ alert_text + "\033[0m")

logging.info("=== 网站监控系统启动 ===")

urls = [
    "http://39.106.44.177",
    "https://www.baidu.com",
    "http://1.1.1.1"  # 必挂的测试网址
]

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            logging.info(f"[OK] {url} - 状态码：{response.status_code}")
        else:
            logging.warning(f"[WARN] {url} - 异常状态码：{response.status_code}")
    except requests.exceptions.RequestException as e:
        # 连接失败，属于严重错误
        send_alert(url,str(e))
logging.info("=== 监控结束 ===")

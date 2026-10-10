import configparser
import logging
import requests
from datetime import datetime

# 1. 读取配置函数
def load_config(config_path="config.ini"):
    config = configparser.ConfigParser()
    config.read(config_path, encoding='utf-8')
    timeout = config.getint('setting', 'timeout')
    urls = [url for key, url in config.items('urls')]
    return timeout, urls

# 2. 发送告警函数
def send_alert(url, error_msg):
    alert_text = f"【严重告警】网站 {url} 在 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 连接失败！原因：{error_msg}"
    logging.error(alert_text)
    with open("alert.log", "a", encoding='utf-8') as f:
        f.write(alert_text + "\n")
    print(f"\033[91m{alert_text}\033[0m")

# 3. 核心检查逻辑
def check_urls(timeout, urls):
    logging.info("=== 网站监控系统启动 ===")
    for url in urls:
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                logging.info(f"[OK] {url} - 状态码：{response.status_code}")
            else:
                logging.warning(f"[WARN] {url} - 异常状态码：{response.status_code}")
        except requests.exceptions.RequestException as e:
            send_alert(url, str(e))
    logging.info("=== 监控结束 ===")

# 4. 主程序入口（只在直接运行此文件时执行）
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler("monitor.log", encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    
    # 读取配置并开始检查
    timeout, urls = load_config()
    check_urls(timeout, urls)

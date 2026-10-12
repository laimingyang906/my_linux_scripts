#!/usr/bin/env python3
# 声明这是一个 Python3 脚本，方便系统直接识别

import shutil
# 导入 shutil 库，用于获取服务器磁盘的容量信息（标准库，无需额外安装）

import requests
# 导入 requests 库，用于向网站发送 HTTP 请求，检查其是否存活

import logging
# 导入 logging 库，用于生成专业的日志记录（替代 print）

from datetime import datetime
# 从 datetime 模块导入 datetime 类，用于获取当前的时间戳

logging.basicConfig(
    # 调用 logging 的基础配置函数
    level=logging.INFO,
    # 设置日志级别为 INFO，意味着 INFO 及以上级别（WARNING、ERROR）的日志都会被记录
    format='%(asctime)s - %(levelname)s - %(message)s',
    # 设置日志格式：包含时间(asctime)、日志级别(levelname)和日志内容(message)
    datefmt='%Y-%m-%d %H:%M:%S',
    # 设置时间显示格式为：年-月-日 时:分:秒
    handlers=[
        # 设置日志的输出渠道
        logging.FileHandler("patrol.log", encoding='utf-8'),
        # 渠道1：写入到当前目录下的 patrol.log 文件中，编码为 utf-8 以支持中文
        logging.StreamHandler()
        # 渠道2：同时输出到终端屏幕上
    ]
)

def check_disk(threshold=80):
    # 定义一个检查磁盘的函数，默认阈值设为 80（即 80%）
    total, used, free = shutil.disk_usage("/")
    # 使用 shutil.disk_usage 查询根目录（/）的磁盘情况，并解包为：总大小、已用大小、剩余大小
    percent = (used / total) * 100
    # 计算使用率百分比：（已用 / 总大小）乘以 100
    if percent > threshold:
        # 如果使用率超过了阈值（比如 80%）
        return f"【警告】磁盘空间告急！当前使用率：{percent:.2f}%"
        # 返回带有警告信息的字符串，:.2f 表示保留两位小数
    else:
        # 如果没超过阈值
        return f"【正常】磁盘使用率：{percent:.2f}%"
        # 返回正常状态的字符串

def check_website(url):
    # 定义一个检查网站是否存活的函数，传入参数为网址 url
    try:
        # 开启异常捕获，防止网络报错直接导致脚本崩溃
        response = requests.get(url, timeout=5)
        # 向目标网址发起 GET 请求，最长等待 5 秒
        if response.status_code == 200:
            # 如果返回的状态码是 200 (代表正常访问)
            return f"【正常】网站 {url} 状态码 200"
            # 返回正常提示
        else:
            # 如果返回了非 200 的状态码（如 404, 500）
            return f"【警告】网站 {url} 返回异常状态码：{response.status_code}"
            # 返回警告信息
    except Exception as e:
        # 如果连接超时、DNS 解析失败等抛出异常
        return f"【严重】网站 {url} 无法连接！错误：{e}"
        # 返回严重故障信息

if __name__ == "__main__":
    # 判断当前文件是否被直接运行（如果是被 import，则不执行下面的代码）
    logging.info("======== 服务器巡检机器人启动 ========")
    # 记录一条启动日志
    
    # 1. 执行磁盘检查
    disk_result = check_disk()
    # 调用 check_disk 函数，把返回的结果存在 disk_result 变量里
    logging.info(disk_result)
    # 把磁盘检查结果写进日志
    
    # 2. 执行网站检查
    web_result = check_website("http://39.106.44.177")
    # 调用 check_website 函数，检查我们自己的服务器，结果存在 web_result 变量里
    logging.info(web_result)
    # 把网站检查结果写进日志
    
    logging.info("======== 巡检结束 ========")
    # 记录一条结束日志

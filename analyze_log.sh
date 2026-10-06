#!/bin/bash
LOG_FILE="/var/log/nginx/access.log"

echo "====网站日志分析报告===="
echo "报告生成时间:$(date)"
echo ""

echo "1.访问量最高的前5个IP:"
awk '{print $1}' $LOG_FILE | sort |uniq -c | sort -rn | head -n 5
echo ""

echo "2.被访问最多的前5个页面:"
awk '{print $7}' $LOG_FILE | sort | uniq -c | sort -rn | head -n 5
echo ""

echo "3.总访问次数:"
wc -l< $LOG_FILE
echo "=================="

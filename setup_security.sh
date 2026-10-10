#!/bin/bash
# Day 22: 服务器安全加固备忘录
# 本脚本仅用于记录安全加固流程，请勿直接在生产环境盲目执行

echo "=== 1. 配置 UFW 防火墙 ==="
# sudo ufw allow ssh    # 先放行 SSH 保命
# sudo ufw allow 80/tcp # 放行 HTTP
# sudo ufw allow 443/tcp # 放行 HTTPS
# sudo ufw enable       # 开启防火墙

echo "=== 2. 安装并配置 Fail2ban ==="
# sudo apt install fail2ban -y
# sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
# sudo nano /etc/fail2ban/jail.local
# (在 jail.local 的 [sshd] 节里配置 maxretry = 3, bantime = 3600)
# sudo systemctl restart fail2ban
# sudo fail2ban-client status sshd

echo "=== 3. 修改 SSH 配置禁用密码登录 ==="
# sudo nano /etc/ssh/sshd_config
# (修改 PasswordAuthentication no, PubkeyAuthentication yes)
# sudo systemctl restart ssh

echo "安全加固备忘录记录完成！"

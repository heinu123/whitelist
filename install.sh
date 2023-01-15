#! /bin/bash

#环境配置
update(){
    sudo apt update
    sudo apt install python3-pip -y
    sudo apt install git
    sudo pip3 install requests
    sudo pip3 install netaddr
    clear
}

#获取主程序
down(){
    git clone https://github.com/heinu123/whitelist.git /usr/whitelist
    clear
}

#Main
echo "Hello World"
sleep 1

update
down

cd /usr/whitelist

echo "请输入节点端口(多个端口请用 , 分隔)"
read port

echo "请输入web认证端口"
read web_port

echo "请输入认证路径(例如/aries)"
read path

echo "请输入认证用户名"
read username

echo "请输入认证密码"
read password

echo "获取信息完成,已经写入脚本"

cat <<text >./config.py
port = [ ${port} ]
web_port = ${web_port}
URL_PATH = "${path}"
USERNAME = '${username}'
PASSWORD = '${password}'
text

echo "配置环境完成,挂起后台执行"
nohup python3 -u web.py > iplog.out 2>&1 &
clear 

echo "认证信息:"
echo "`curl -s ifconfig.me/ip`:${web_port}${path}"
echo "用户名:${username}"
echo "密码:${password}"

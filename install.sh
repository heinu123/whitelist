#!/bin/bash

red='\033[0;31m'
green='\033[0;32m'


function ERR() {
    echo -e "${red}[ERR] $* ${plain}"
}

function INFO() {
    echo -e "${green}[INFO] $* ${plain}"
}

[[ $EUID -ne 0 ]] && ERR "错误:  必须使用root用户运行此脚本!\n" && exit 1

if [[ -f /etc/redhat-release ]]; then
    release="centos"
elif cat /etc/issue | grep -Eqi "debian"; then
    release="debian"
elif cat /etc/issue | grep -Eqi "ubuntu"; then
    release="ubuntu"
elif cat /etc/issue | grep -Eqi "centos|red hat|redhat"; then
    release="centos"
elif cat /proc/version | grep -Eqi "debian"; then
    release="debian"
elif cat /proc/version | grep -Eqi "ubuntu"; then
    release="ubuntu"
elif cat /proc/version | grep -Eqi "centos|red hat|redhat"; then
    release="centos"
else
    ERR "未检测到系统版本，请联系脚本作者！\n" && exit 1
fi

os_version=""

# os version
if [[ -f /etc/os-release ]]; then
    os_version=$(awk -F'[= ."]' '/VERSION_ID/{print $3}' /etc/os-release)
fi
if [[ -z "$os_version" && -f /etc/lsb-release ]]; then
    os_version=$(awk -F'[= ."]+' '/DISTRIB_RELEASE/{print $2}' /etc/lsb-release)
fi

if [[ x"${release}" == x"centos" ]]; then
    if [[ ${os_version} -le 6 ]]; then
        ERR "请使用 CentOS 7 或更高版本的系统！\n" && exit 1
    fi
elif [[ x"${release}" == x"ubuntu" ]]; then
    if [[ ${os_version} -lt 16 ]]; then
        ERR "请使用 Ubuntu 16 或更高版本的系统！\n" && exit 1
    fi
elif [[ x"${release}" == x"debian" ]]; then
    if [[ ${os_version} -lt 8 ]]; then
        ERR "请使用 Debian 8 或更高版本的系统！\n" && exit 1
    fi
fi

INFO "正在安装所需环境..."
if [[ release == "centos" ]]; then
    sudo yum install git python3-pip wget curl screen -y
else
    sudo apt install git python3-pip wget curl screen -y
fi


sudo pip install -r requirements.txt
git clone https://github.com/heinu123/whitelist.git /usr/whitelist
cd /usr/whitelist
INFO "配置环境完成 如果报错请更新源"
INFO "正在安装..."
mv /usr/whitelist/whitelist.service /etc/systemd/system/whitelist.service
sudo systemctl daemon-reload
sudo systemctl enable python-project.service
INFO "第一次启动需要输入配置\n配置输入完成后使用ctrl+a+d退出screen\n之后可以使用 systemctl start whitelist.service启动"
screen -S whitelist -d -m /usr/bin/python3 /usr/whitelist/main.py



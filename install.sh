#!/bin/bash

RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
PLAIN="\033[0m"

red(){
    echo -e "\033[31m\033[01m$1\033[0m"
}

green(){
    echo -e "\033[32m\033[01m$1\033[0m"
}

yellow(){
    echo -e "\033[33m\033[01m$1\033[0m"
}

REGEX=("debian" "ubuntu" "centos|red hat|kernel|oracle linux|alma|rocky" "'amazon linux'" "alpine")
RELEASE=("Debian" "Ubuntu" "CentOS" "CentOS" "Alpine")
PACKAGE_UPDATE=("apt -y update" "apt -y update" "yum -y update" "yum -y update" "apk update -f")
PACKAGE_INSTALL=("apt -y install" "apt -y install" "yum -y install" "yum -y install" "apk add -f")
CMD=("$(grep -i pretty_name /etc/os-release 2>/dev/null | cut -d \" -f2)" "$(hostnamectl 2>/dev/null | grep -i system | cut -d : -f2)" "$(lsb_release -sd 2>/dev/null)" "$(grep -i description /etc/lsb-release 2>/dev/null | cut -d \" -f2)" "$(grep . /etc/redhat-release 2>/dev/null)" "$(grep . /etc/issue 2>/dev/null | cut -d \\ -f1 | sed '/^[ ]*$/d')")

for i in "${CMD[@]}"; do
    SYS="$i" && [[ -n $SYS ]] && break
done

for ((int=0; int<${#REGEX[@]}; int++)); do
    [[ $(echo "$SYS" | tr '[:upper:]' '[:lower:]') =~ ${REGEX[int]} ]] && SYSTEM="${RELEASE[int]}" && [[ -n $SYSTEM ]] && break
done

update(){
    echo "Checking Update ..."
    if [[ ! $SYSTEM == "CentOS" ]]; then
        ${PACKAGE_UPDATE[int]}
    fi
    ${PACKAGE_INSTALL[int]} update
    echo "Install dependencies ..."
    ${PACKAGE_INSTALL[int]} git python3-pip wget curl sudo iptables -y
}

install(){
    update
    git clone https://github.com/heinu123/whitelist.git /usr/whitelist
    cd /usr/whitelist
    pip3 install -r requirements.txt
    ln -sf ${0} /usr/bin/whitelist
    chmod +x /usr/bin/whitelist
    clear
    echo -e "执行初始化配置，请在设置完后${RED}手动使用Ctrl+C打断Python执行${PLAIN}"
    python3 main.py
    yellow "正在设置systemctl后台守护"
    cp -f whitelist.service /etc/systemd/system/whitelist.service
    systemctl start whitelist.service
    systemctl enable whitelist.service
    echo -e "配置完成，如果要修改配置文件请到${GREEN} /usr/whitelist/config.json ${PLAIN}修改配置 ${YELLOW}(自动配置开发ing)${PLAIN}"
    echo -e "可使用${GREEN} systemctl status whitelist ${PLAIN}查看程序运行日志"
}

uninstall(){
    read -p "确定要卸载代理白名单认证系统吗？[y/n]:" confirm
    if [[ $confirm =~ Y|y ]]; then
        systemctl stop whitelist
        systemctl disable whitelist
        iptables -F
        rm -f /etc/systemd/system/whitelist.service
        rm -rf /usr/whitelist
        green "代理白名单认证系统已彻底卸载成功！"
    fi
}

start(){
    systemctl start whitelist.service
    systemctl enable whitelist.service
    green "代理白名单认证系统已启动成功！"
}

stop(){
    systemctl stop whitelist
    systemctl disable whitelist
    green "代理白名单认证系统已关闭成功！"
}

restart(){
    systemctl stop whitelist
    systemctl disable whitelist
    systemctl start whitelist.service
    systemctl enable whitelist.service
    green "代理白名单认证系统已重启成功！"
}

updates() {
    git clone https://github.com/heinu123/whitelist.git /usr/whitelist/temp
    for file in /usr/whitelist/temp/*
    do
        mv -f ${file} /usr/whitelist/
    done
    rm -rf /usr/whitelist/temp
    pip3 install -r requirements.txt
    clear
    green "更新完成，已重新启动"
    green "如果报错请删除配置文件: /usr/whitelist/config.json"
    restart
}

menu(){
    echo "#############################################################"
    echo -e "#                ${RED}代理白名单认证系统  一键脚本${PLAIN}               #"
    echo -e "# ${GREEN}作者${PLAIN}: heinu123                                            #"
    echo -e "# ${GREEN}GitHub 项目${PLAIN}: https://github.com/heinu123/whitelist        #"
    echo -e "# 安装后可用使用∶ ${GREEN} whitelist ${PLAIN}命令再次进入带这个页面         #"
    echo "#############################################################"
    echo ""
    echo -e " ${GREEN}1.${PLAIN} 安装 代理白名单认证系统"
    echo -e " ${GREEN}2.${PLAIN} 更新 代理白名单认证系统"
    echo -e " ${GREEN}3.${PLAIN} ${RED}卸载 代理白名单认证系统${PLAIN}"
    echo " -------------"
    echo -e " ${GREEN}4.${PLAIN} 启动 代理白名单认证系统"
    echo -e " ${GREEN}5.${PLAIN} 关闭 代理白名单认证系统"
    echo -e " ${GREEN}6.${PLAIN} 重启 代理白名单认证系统"
    echo " -------------"
    echo -e " ${GREEN}0.${PLAIN} 退出脚本"
    echo ""
    read -rp "请输入选项 [0-6]: " menuInput
    case $menuInput in
        1 ) install ;;
        2 ) updates ;;
        3 ) uninstall ;;
        4 ) start ;;
        5 ) stop ;;
        6 ) restart ;;
        * ) exit 1 ;;
    esac
}

menu

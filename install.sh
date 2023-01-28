#!/bin/bash

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
    echo "Checking Update .."
    sleep 2
    if [[ ! $SYSTEM == "CentOS" ]]; then
        ${PACKAGE_UPDATE[int]}
    fi
    ${PACKAGE_INSTALL[int]} git python3-pip wget curl sudo
}

gits(){
    git clone https://github.com/heinu123/whitelist.git /usr/whitelist
    cd /usr/whitelist
    sudo pip3 install -r requirements.txt
}


#Main
update
gits
cd /usr/whitelist
clear
echo "执行初始化配置，请在设置完后手动使用Ctrl+C打断Python执行"
python3 main.py
echo "正在设置后台挂起"
nohup python3 -u main.py > log.out 2>&1 &
echo "配置完成，如果要修改配置文件请到/usr/whitelist/config.json手动配置(自动配置开发ing)"
echo "日志文件在：/usr/whitelist/log.out"
cat config.json
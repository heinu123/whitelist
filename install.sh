#! /bin/bash
update(){
    echo "Checking Update .."
    sleep 1
    sudo apt update
    sudo apt upgrade
    sudo apt install git python3-pip wget curl -y
}

gits(){
    git clone https://github.com/heinu123/whitelist.git /usr/whitelist
    cd /usr/whitelist
    sudo pip install -r requirements.txt
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
echo "日志文件位置/usr/whitelist/log.out"
cat config.json 

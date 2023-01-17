# 节点加白

## 效果
可以降低被恶意使用/BOT扫描的概率，同时降低被墙概率.

## 原理

使用Python自动监视网络连接，并使用iptables作为防火墙控制放行端口

## 一键脚本(beta)

使用root权限 (sudo -i) 执行

```
 bash <(curl -Ls https://raw.githubusercontent.com/heinu123/whitelist/master/install.sh)
```

## 手动安装
```
apt install git python3-pip wget curl screen -y
git clone https://github.com/heinu123/whitelist.git /usr/whitelist && cd /usr/whitelist
mv /usr/whitelist/whitelist.service /etc/systemd/system/whitelist.service
sudo systemctl daemon-reload
screen -S whitelist -d -m /usr/bin/python3 /usr/whitelist/main.py
```
使用ctrl+a+d退出screen终端

完成配置后可以使用systemctl启动(beta)
```
systemctl start whitelist.service
```

## 简介

默认安装在 `/usr/whitelist`


## 如何关闭

如果要关闭监听

### Step1

关闭python监听进程

请使用

```shell
ps -ef|grep python
```

查看进程号

杀掉进程python3

```shell
kill -9 进程号
```

### Step2

清空iptables

```
iptables -F
```


## 参考项目

UFWFORNODE: https://github.com/AriesEDGE/ufwfornode

## 开发&感谢

排名不分先后



[黑弩](https://github.com/heinu123)

[Aries](https://github.com/AriesEDGE)

[UniOreoX](https://github.com/unioreox)



觉得项目不错不妨给我点个小小的Star (ฅ'ω'ฅ).

感谢大家！


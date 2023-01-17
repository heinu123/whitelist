# 节点加白

## 效果
可以降低被恶意使用/BOT扫描的概率，同时降低被墙概率.

## 原理

使用Python自动监视网络连接，并使用iptables作为防火墙控制放行端口

## 食用方法

使用root权限 (sudo -i) 执行

```
 bash <(curl -Ls https://raw.githubusercontent.com/heinu123/whitelist/master/install.sh)
```



## 简介

默认安装在 `/usr/whitelist`


### 其他补充

屏蔽常见的测速网站
```
iptables -A OUTPUT -m string --string "fast.com" --algo bm -j DROP
iptables -A OUTPUT -m string --string "speedtest.net" --algo bm -j DROP
iptables -A OUTPUT -m string --string "speedtest.com" --algo bm -j DROP
iptables -A OUTPUT -m string --string "speedtest.cn" --algo bm -j DROP
iptables -A OUTPUT -m string --string "test.ustc.edu.cn" --algo bm -j DROP
iptables -A OUTPUT -m string --string "10000.gd.cn" --algo bm -j DROP
iptables -A OUTPUT -m string --string "db.laomoe.com" --algo bm -j DROP
iptables -A OUTPUT -m string --string "jiyou.cloud" --algo bm -j DROP
iptables -A OUTPUT -m string --string "ovo.speedtestcustom.com" --algo bm -j DROP
iptables -A OUTPUT -m string --string "speed.cloudflare.com" --algo bm -j DROP
```

### 日志查看

nohup 可以直接查看日志（Python）



```shell
cat /usr/whitelist/iplog.out
```



## 如何关闭

Python后台监听采用nohup



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

清除iptables进程

```
iptables -F
```


## 参考项目

UFWFORNODE: https://github.com/AriesEDGE/ufwfornode

IPTABLES: https://linux.die.net/man/8/iptables

## 开发&感谢

排名不分先后



黑弩[https://github.com/heinu123]

Aries[https://github.com/AriesEDGE]

UniOreoX[https://github.com/unioreox]



觉得项目不错不妨给我点个小小的Star (ฅ'ω'ฅ).

感谢大家！


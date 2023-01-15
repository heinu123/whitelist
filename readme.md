# 节点加白

## 效果
可以降低被恶意使用/BOT扫描的概率，同时降低被墙概率.

## 原理

使用Python自动监视网络连接，并使用iptables作为防火墙控制放行端口

## 食用方法

使用root权限 (sudo -i) 执行

```
 bash <(curl -Ls https://ghproxy.com/github.com/heinu123/whitelist/blob/main/install.sh)
```



## 简介

默认安装在 `/usr/whitelist`



### 文件介绍

`web.py` 是 主要监听 的 py文件

`autowhite.py` 是 IPTABLES 配置文件

`config.py` 是 配置文件 ，可以手动修改认证端口，账号密码等

`logs.py` 是 日志目录 ，记录认证IP，结束后会生成一个 `ip.csv` 的文件，可以批量查询IP.

### 其他补充

屏蔽测速网站
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



## 补充&预告



后期会修改前端认证页面(高情商:简约 低情商:简陋)

以后会放一个redis版本，更为方便

Aries会补充快捷命令，支持快捷命令修改端口，账号密码等.



## 参考项目

UFWFORNODE: https://github.com/AriesEDGE/ufwfornode

IPTABLES: https://linux.die.net/man/8/iptables

## 开发&感谢

排名不分先后



Telegram

黑弩 

@heinu1 https://t.me/heinu1

Aries 

@aries_init https://t.me/aries_init

UniOreoX

@UniOreoX https://t.me/unioreox



觉得项目不错不妨给我点个小小的Star (ฅ'ω'ฅ).

感谢大家！


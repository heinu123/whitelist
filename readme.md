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

清除iptables进程

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


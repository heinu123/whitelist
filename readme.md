# 节点白名单认证

## 兼容性
兼容:shadowsocks vmess socks http mtproxy vless trojan

## 效果
可以降低被主动探测/BOT扫描的概率 同时降低被墙概率

支持同时监听多个端口 支持ipv4/ipv6网络

支持屏蔽bt下载 常用测速网站 挖矿等

支持绑定url(自动跳转) 可以用来实现自动跳转到节点所属频道

支持谷歌recaptcha人机验证

## 一键脚本(beta)

使用root权限 (sudo -i) 执行

```
 bash <(curl -Ls https://raw.githubusercontent.com/heinu123/whitelist/master/install.sh)
```

## 手动安装

Step1.初始化
```
apt install git python3-pip wget curl -y
git clone https://github.com/heinu123/whitelist.git /usr/whitelist && cd /usr/whitelist
python3 main.py
```
此步完成后使用 Ctrl+C 打断

Step2.后台运行(nohup版)
```
nohup python3 -u main.py > log.out 2>&1 &
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

## Debug
1.预计会增加systemctl版本一键安装
2.预计会增加自动化修改端口

## 其他项目(重构版)

[golang重构](https://github.com/unioreox/SimpleFirewall)

## 开发&感谢

排名不分先后



[黑弩](https://github.com/heinu123)  →[telegram频道](https://t.me/heinuhome)

[Aries](https://github.com/AriesEDGE)  →[telegram频道](https://t.me/aries_init)

[UniOreoX](https://github.com/unioreox)  →[telegram频道](https://t.me/unichannelx)



觉得项目不错不妨给我点个小小的Star (ฅ'ω'ฅ).

感谢大家！

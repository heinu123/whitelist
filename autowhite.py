import config
import logs
import os
from netaddr.ip import IPAddress
 
def if_ip4or6(cfgstr):
    ipFlg = False
    if '/' in cfgstr:
        text = cfgstr[:cfgstr.rfind('/')]
    else:
        text = cfgstr
    try:
        addr = IPAddress(text)
        ipFlg = True
    except:
        ipFlg = False
 
    if ipFlg == True:
        return addr.version
    else:
        return False

def init():
    os.system("sudo rm -rf ./ip.csv")
    os.system("iptables -F")
    for sub_port in config.port:
        os.system("iptables -I INPUT -p TCP --dport "+ str(sub_port) +" -j DROP")
        os.system("iptables -I INPUT -p UDP --dport "+ str(sub_port) +" -j DROP")

def add(ip):
    if os.path.isfile("./ip.csv"):
        r = open("./ip.csv", mode='r')
        iplist = r.read()
        r.close()
    else:
        iplist = ""
    
    if ip in iplist:
        print(ip+"已经添加过白名单")
        return ip+"已经添加过白名单"
    else:
        for sub_port in config.port:
            if if_ip4or6(ip) == 4:
                os.system("iptables -I INPUT -s "+ip+" -p TCP --dport "+ str(sub_port) +" -j ACCEPT")
                os.system("iptables -I INPUT -s "+ip+" -p UDP --dport "+ str(sub_port) +" -j ACCEPT")
            else:
                os.system("ip6tables -I INPUT -s "+ip+" -p TCP --dport "+ str(sub_port) +" -j ACCEPT")
                os.system("ip6tables -I INPUT -s "+ip+" -p UDP --dport "+ str(sub_port) +" -j ACCEPT")
        print(ip+"已添加到白名单")
        logs.add(ip)
        return ip+"已添加到白名单"
import gol
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


def anti_abuse():
    os.system('iptables -A OUTPUT -m string --string "fast.com" --algo bm -j DROP')
    os.system(
        'iptables -A OUTPUT -m string --string "speedtest.net" --algo bm -j DROP')
    os.system(
        'iptables -A OUTPUT -m string --string "speedtest.com" --algo bm -j DROP')
    os.system(
        'iptables -A OUTPUT -m string --string "speedtest.cn" --algo bm -j DROP')
    os.system(
        'iptables -A OUTPUT -m string --string "test.ustc.edu.cn" --algo bm -j DROP')
    os.system(
        'iptables -A OUTPUT -m string --string "10000.gd.cn" --algo bm -j DROP')
    os.system(
        'iptables -A OUTPUT -m string --string "db.laomoe.com" --algo bm -j DROP')
    os.system(
        'iptables -A OUTPUT -m string --string "jiyou.cloud" --algo bm -j DROP')
    os.system(
        'iptables -A OUTPUT -m string --string "ovo.speedtestcustom.com" --algo bm -j DROP')
    os.system(
        'iptables -A OUTPUT -m string --string "speed.cloudflare.com" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "speedtest" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "speedtest" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string ".speed" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "speed." --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string ".speed." --algo bm -j DROP')


def anti_bt():
    os.system('iptables -A OUTPUT -m string --string "torrent" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string ".torrent" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "peer_id=" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "announce" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "info_hash" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "get_peers" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "find_node" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "BitTorrent" --algo bm -j DROP')
    os.system(
        'iptables -A OUTPUT -m string --string "announce_peer" --algo bm -j DROP')
    os.system(
        'iptables -A OUTPUT -m string --string "BitTorrent protocol" --algo bm -j DROP')
    os.system(
        'iptables -A OUTPUT -m string --string "announce.php?passkey=" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "magnet:" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "xunlei" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "sandai" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "Thunder" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "XLLiveUD" --algo bm -j DROP')
    os.system(
        'iptables -A OUTPUT -m string --string "ethermine.com" --algo bm -j DROP')
    os.system(
        'iptables -A OUTPUT -m string --string "antpool.one" --algo bm -j DROP')
    os.system(
        'iptables -A OUTPUT -m string --string "antpool.com" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "pool.bar" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "get_peers" --algo bm -j DROP')
    os.system(
        'iptables -A OUTPUT -m string --string "announce_peer" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "find_node" --algo bm -j DROP')
    os.system('iptables -A OUTPUT -m string --string "seed_hash" --algo bm -j DROP')


def init():
    os.system("sudo rm -rf ./ip.csv")
    os.system("iptables -F")
    for sub_port in gol.get_value('port'):
        os.system("iptables -I INPUT -p TCP --dport " +
                  str(sub_port) + " -j DROP")
        os.system("iptables -I INPUT -p UDP --dport " +
                  str(sub_port) + " -j DROP")


def add(ip):
    if os.path.isfile("./ip.csv"):
        r = open("./ip.csv", mode='r')
        iplist = r.read()
        r.close()
    else:
        iplist = ""

    if ip in iplist:
        print(ip+"已经添加过白名单")
        return "已经添加过白名单"
    else:
        for sub_port in gol.get_value('port'):
            if if_ip4or6(ip) == 4:
                os.system("iptables -I INPUT -s "+ip +
                          " -p TCP --dport " + str(sub_port) + " -j ACCEPT")
                os.system("iptables -I INPUT -s "+ip +
                          " -p UDP --dport " + str(sub_port) + " -j ACCEPT")
            else:
                os.system("ip6tables -I INPUT -s "+ip +
                          " -p TCP --dport " + str(sub_port) + " -j ACCEPT")
                os.system("ip6tables -I INPUT -s "+ip +
                          " -p UDP --dport " + str(sub_port) + " -j ACCEPT")
        print(ip+"已添加到白名单")
        logs.add(ip)
        return "已添加到白名单"

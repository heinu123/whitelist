import os

def adoptadd(ip):
    if os.path.isfile("./adoptip.csv"):
        r = open("./adoptip.csv", mode='r')
        iplist = r.read()
        r.close()
    else:
        iplist = ""

    if ip in iplist:
        return False
    else:
        r = open("./adoptip.csv", mode='a')
        r.write(ip+"\n")
        r.close()

def failedadd(ip):
    if os.path.isfile("./failedip.csv"):
        r = open("./failedip.csv", mode='r')
        iplist = r.read()
        r.close()
    else:
        iplist = ""

    if ip in iplist:
        return False
    else:
        r = open("./failedip.csv", mode='a')
        r.write(ip+"\n")
        r.close()
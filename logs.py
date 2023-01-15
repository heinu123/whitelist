
def add(ip):
    r = open("./ip.csv", mode='a')
    r.write(ip+"\n")
    r.close()
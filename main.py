import gol
import os
import json
import time
import config
import autowhite
import requests
import socket
import http.server
import socketserver
import base64

global port, web_port, url_path, username, password, AUTH_KEY

def main():
    gol._init()
    if os.path.exists("config.json"):
        with open('config.json', 'r') as f:
            configs = json.load(f)
        port = configs['port']
        web_port = configs['web_port']
        url_path = configs['url_path']
        username = configs['username']
        password = configs['password']
        gol.set_value('port',port)
        gol.set_value('url_path',url_path)
    else:
        config.retconfig()
        port = gol.get_value('port')
        web_port = gol.get_value('web_port')
        url_path = gol.set_value('url_path')
        username = gol.get_value('username')
        password = gol.get_value('password')
    gol.set_value('AUTH_KEY',base64.b64encode('{}:{}'.format(username, password).encode()).decode())
    autowhite.init()
    address = ("", web_port)
    print("自动白名单服务器监听开启")
    for sub_port in port:
        print("节点监听端口:"+ sub_port)
    print("公网白名单网页认证链接:http://"+ requests.get('http://ifconfig.me/ip', timeout=1).text.strip() +":"+str(web_port)+url_path)
    print("内网白名单网页认证链接:http://"+ socket.gethostbyname(socket.gethostname()) +":"+str(web_port)+url_path)
    print("白名单网页认证账号:"+username)
    print("白名单网页认证密码:"+password)
    with ThreadingHTTPServer(address, BasicAuthHandler) as httpd:
        httpd.serve_forever()
 



class BasicAuthHandler(http.server.SimpleHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="FileServer"')
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
    

    def do_GET(self):
        if self.path == gol.get_value('url_path'):
            if self.headers.get("Authorization") == None:
                self.do_AUTHHEAD()
            elif self.headers.get("Authorization") == "Basic " + gol.get_value('AUTH_KEY'):
                self.do_HEAD()
                html = open("index.html","r",encoding='utf-8')
                html_body = html.read()
                self.wfile.write(b""+html_body.replace("{add}", autowhite.add(self.client_address[0])).replace("{ip}", self.client_address[0]).encode("utf-8"))
                
            else:
                self.do_AUTHHEAD()
        else:
            if os.path.exists(self.path):
                with open(self.path,"r") as getfile:
                    self.send_response(200)
                    self.send_header("Content-type", "text/"+ os.path.splitext(self.path)[-1][1:] +"; charset=utf-8")
                    self.wfile.write(b""+getfile.encode("utf-8"))
            else:
                self.send_response(404)
                self.end_headers()

class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass




if __name__ == '__main__':
    main()
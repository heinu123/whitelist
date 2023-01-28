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
import requests

global port, web_port, url_path, username, password, AUTH_KEY,auto,url

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
        anti_bt = configs['anti_bt']
        anti_abuse = configs['anti_abuse']
        auto = configs['auto']
        url = configs['url']
        gol.set_value('port',port)
        gol.set_value('url_path',url_path)
        gol.set_value('auto',auto)
    else:
        config.retconfig()
        port = gol.get_value('port')
        web_port = gol.get_value('web_port')
        url_path = gol.set_value('url_path')
        username = gol.get_value('username')
        password = gol.get_value('password')
        anti_bt = gol.get_value('anti_bt')
        anti_abuse = gol.get_value('anti_abuse')
        auto = gol.get_value('auto')
        url = gol.get_value('url')
    gol.set_value('AUTH_KEY',base64.b64encode('{}:{}'.format(username, password).encode()).decode())
    autowhite.init()
    if anti_abuse == "true":
        autowhite.anti_abuse()
        print("已屏蔽测速滥用")
    if anti_bt == "true":
        autowhite.anti_bt()
        print("已屏蔽bt下载")
    if auto == "false":
         gol.set_value('auto',"")
    else:
        autos = '<script type="text/javascript">	\n    var t=3;\n    setInterval("refer()",1000);\n    function refer(){\n    if(t==0){\n    location="{url}";\n    }\n    document.getElementById("show").innerHTML="将在"+t+"秒后跳转到节点所属频道...";\n    t--;\n    }\n    </script>'.replace("{url}", url)
        gol.set_value('auto',str(autos))
    web_port = int(web_port)
    address = ("", web_port)
    print("自动白名单服务器监听开启")
    for sub_port in port:
        print("节点监听端口:"+ sub_port)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    print("公网白名单网页认证链接:http://"+ requests.get('http://ifconfig.me/ip', timeout=1 , headers = headers).text.strip() +":"+str(web_port)+url_path)
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
    
    def do_POST(self):
        self.do_HEAD()
        html = open("./html/index.html","r",encoding='utf-8')
        html_body = html.read()
        self.wfile.write(b""+html_body.replace("{add}", autowhite.add(self.client_address[0])).replace("{ip}", self.client_address[0]).replace("{auto}", gol.get_value('auto')).encode("utf-8"))
                

    def do_GET(self):
        if self.path == gol.get_value('url_path'):
            if self.headers.get("Authorization") == None:
                self.do_AUTHHEAD()
            elif self.headers.get("Authorization") == "Basic " + gol.get_value('AUTH_KEY'):
                self.do_HEAD()
                html = open("./html/recaptcha.html","r",encoding='utf-8')
                html_body = html.read()
                self.wfile.write(b""+html_body.encode("utf-8"))
                
            else:
                self.do_AUTHHEAD()
        else:
            if os.path.isfile(os.path.exists("."+self.path)):
                with open("."+self.path,"r") as getfile:
                    if os.path.splitext(self.path)[-1][1:] == "html":
                        header = "text/html"
                    elif os.path.splitext(self.path)[-1][1:] == "gif":
                        header = "image/gif"
                    elif os.path.splitext(self.path)[-1][1:] == "jpg":
                        header = "image/jpeg"
                    elif os.path.splitext(self.path)[-1][1:] == "png":
                        header = "image/png"
                    elif os.path.splitext(self.path)[-1][1:] == "mp4":
                        header = "video/mpeg4"
                    elif os.path.splitext(self.path)[-1][1:] == "ico":
                        header = "image/vnd.microsoft.icon"
                    self.send_response(200)
                    self.send_header("Content-type", header +"; charset=utf-8")
                    self.wfile.write(b""+getfile.encode("utf-8"))
            else:
                self.send_response(404)
                self.end_headers()

class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass




if __name__ == '__main__':
    main()
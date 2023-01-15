import config
import time
import autowhite
import requests
import http.server
import socketserver
import base64

AUTH_KEY = base64.b64encode('{}:{}'.format(config.USERNAME, config.PASSWORD).encode()).decode()


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
        if self.path == config.URL_PATH:
            if self.headers.get("Authorization") == None:
                self.do_AUTHHEAD()
            elif self.headers.get("Authorization") == "Basic " + AUTH_KEY:
                self.do_HEAD()
                html_body = "<h1>节点自动白名单系统</h1>"
                html_body += "<p>你的ip:" + autowhite.add(str(self.client_address[0])) +"</p>"
                html_body += "<p>当前时间:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "</p>"
                self.wfile.write(b""+html_body.encode("utf-8"))
                
            else:
                self.do_AUTHHEAD()
        else:
            self.send_response(403)
            self.end_headers()

class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True


if __name__ == '__main__':
    autowhite.init()
    port = config.web_port
    address = ("", port)
    print("自动白名单服务器监听开启")
    print("节点监听端口:"+ str(config.port))
    print("web认证链接:http://"+ requests.get('http://ifconfig.me/ip', timeout=1).text.strip() +":"+str(port)+config.URL_PATH)
    print("web认证账号:"+config.USERNAME)
    print("web认证密码:"+config.PASSWORD)
    with ThreadingHTTPServer(address, BasicAuthHandler) as httpd:
        httpd.serve_forever()
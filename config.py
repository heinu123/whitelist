import json
import gol
import sys
import click
from main import main


@click.command()
@click.option('--port', prompt='你的节点端口 默认:', required=True, default="35960",help='节点端口.',type=(str))
@click.option('--web_port', prompt='你的白名单网页认证端口 默认:', required=True, default="5563",help='白名单网页认证端口.',type=(str))
@click.option('--url_path', prompt='你的白名单网页认证路径 默认:', required=True, default="/" ,help='白名单网页认证路径.',type=(str))
@click.option('--username', prompt='你的白名单网页认证账号 默认:', required=True, default="123",help='白名单网页认证账号.',type=(str))
@click.option('--password', prompt='你的白名单网页认证密码 默认:', required=True, default="123",help='白名单网页认证密码.',type=(str))
def retconfig(port, web_port, url_path, username, password):
    port = port.split(",")
    web_port = int(web_port)
    if web_port in [80,443]:
        print("认证端口禁止设置为80 443")
        sys.exit(0)
    gol.set_value('port',port)
    gol.set_value('web_port',web_port)
    gol.set_value('url_path',url_path)
    gol.set_value('username',username)
    gol.set_value('password',password)
    data = {
    'port': port,
    'web_port': web_port,
    'url_path': url_path,
    'username': username,
    'password': password
    }
    with open('config.json', 'w') as f:
        json.dump(data, f,indent=4)
    print("你的配置已经存储到当前目录的config.json文件内")
    main()

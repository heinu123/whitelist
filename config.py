import json
import gol
import sys
import click
from main import main

@click.command()
@click.option('--port', prompt='你的节点端口(多个端口请使用,分割) ', required=True, help='节点端口', type=(str))
@click.option('--web_port', prompt='你的白名单网页认证端口 默认:', required=True, default="5563", help='白名单网页认证端口', type=(str))
@click.option('--url_path', prompt='你的白名单网页认证路径 默认:', required=True, default="/", help='白名单网页认证路径', type=(str))
@click.option('--username', prompt='你的白名单网页认证账号 默认:', required=True, default="123", help='白名单网页认证账号', type=(str))
@click.option('--password', prompt='你的白名单网页认证密码 默认:', required=True, default="123", help='白名单网页认证密码', type=(str))
@click.option('--anti_abuse', prompt='是否屏蔽常见的测速网站 默认:', default="true", help='屏蔽常见的测速网站.', type=(str))
@click.option('--anti_bt', prompt='是否屏蔽bt下载和挖矿 默认:', default="true", help='屏蔽bt下载', type=(str))
@click.option('--auto', prompt='是否开启自动跳转url链接 (防止转发不署名的sm玩意) 默认:', default="false", help='是否开启自动跳转url链接', type=(str))
@click.option('--url', prompt='(不开启自动跳转为空即可)设置认证成功后自动跳转到指定网页的链接 如: https://www.baidu.com', default="", help='设置认证成功后自动跳转到指定网页的链接 如: https://www.baidu.com', type=(str))
@click.option('--recaptcha', prompt='是否开启谷歌recaptcha人机验证', default="false", help='是否开启谷歌recaptcha人机验证', type=(str))
@click.option('--recaptcha_web_key', prompt='(不开启自动跳转为空即可)谷歌recaptcha的网站密钥(客户端)', default="false", help='谷歌recaptcha的网站密钥(客户端)', type=(str))
@click.option('--recaptcha_key', prompt='(不开启自动跳转为空即可)谷歌recaptcha的网站密钥(服务端)', default="", help='谷歌recaptcha的网站密钥(服务端)', type=(str))
def retconfig(port, web_port, url_path, username, password, anti_abuse, anti_bt, auto, url,recaptcha,recaptcha_web_key,recaptcha_key):
    port = port.split(",")
    if web_port in [80, 443]:
        print("认证端口禁止设置为80 443")
        sys.exit(0)
    if port == "":
        print("节点端口不能为空")
        sys.exit(0)
    if auto == "false":
        url = ""
    else:
        if url == "":
            print("url链接不可为空")
            sys.exit(0)
    if recaptcha == "false":
        recaptcha_web_key = ""
        recaptcha_key = ""
    else:
        if recaptcha_web_key == "":
            print("客户端密钥不可为空")
            sys.exit(0)
        if recaptcha_key == "":
            print("服务端密钥不可为空")
            sys.exit(0)
    gol.set_value('port', port)
    gol.set_value('web_port', web_port)
    gol.set_value('url_path', url_path)
    gol.set_value('username', username)
    gol.set_value('password', password)
    gol.set_value('anti_bt', anti_bt)
    gol.set_value('anti_abuse', anti_abuse)
    gol.set_value('auto', auto)
    gol.set_value('url', url)
    gol.set_value('recaptcha', recaptcha)
    gol.set_value('recaptcha_web_key', recaptcha_web_key)
    gol.set_value('recaptcha_key', recaptcha_key)
    data = {
        'port': port,
        'web_port': web_port,
        'url_path': url_path,
        'username': username,
        'password': password,
        'anti_bt': anti_bt,
        'anti_abuse': anti_abuse,
        'auto': auto,
        'url': url,
        'recaptcha': recaptcha,
        'recaptcha_web_key': recaptcha_web_key,
        'recaptcha_key': recaptcha_key
    }
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print("你的配置已经存储到当前目录的config.json文件内")
    main()

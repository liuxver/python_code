#! /usr/bin/env python3
#-*- coding:utf-8 -*-

#从wsgiref导入
from wsgiref.simple_server import make_server
#从 hello 导入application函数
from hello import application

#创建一个服务器 IP地址为空 端口为 8000   处理函数是 application
httpd=make_server('',8000,application)
print('Server Http on port 8000...')
#开始监听HTTP请求
httpd.serve_forever()






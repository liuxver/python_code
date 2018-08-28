#! /usr/bin/env python3
#-*- coding:utf-8 -*-

#application()函数就是符合WSGI标准的一个HTTP处理函数，
#它接收两个参数：
#environ：一个包含所有HTTP请求信息的dict对象；
#start_response：一个发送HTTP响应的函数。
def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	return [b'<h1>Hello,liuxv!</h1>']


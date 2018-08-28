#! /usr/bin/env python3
#-*- coding:utf-8 -*-
#

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('127.0.0.1',9997))

#接受欢迎消息
print(s.recv(1024).decode('utf-8'))

while True:
	data=input('Enter your message:')
	if data=='exit':
		break
	s.send(data.encode('utf-8'))
	print(s.recv(1024).decode('utf-8'))


s.send(b'exit')
s.close()





#! /usr/bin/env python3
#-*- coding:utf-8 -*-

import socket
import threading
import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#监听端口
s.bind(('127.0.0.1',9997))

#调用listen()方法开始监听端口，
#传入的参数指定等待连接的最大数量：
s.listen(5)
print('waiting for connection...')


#处理函数
#可以使用 + 或者 join链接字符串 
#当较少时候 + 效率高 较多时候 join效率高
#
def tcplink(socket,addr):
	s=''
	s=s+'\nAccept new connection from %s :%s...\n'%addr
	print(s)
	sock.send(b'Welcome!')
	while True:
		data=sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8')=='exit':
			break

		s=s+data.decode('utf-8')+'\n'
		sock.send(('Hello,%s!'%data.decode('utf-8')).encode('utf-8'))

	sock.close()
	print('Connection from %s:%s closed'%addr)
	s=s+'Connection from %s:%s closed'%addr
	print(s)
	with open('server.txt','w') as f:
		f.write(s)


#每个连接都必须创建新线程（或进程）来处理，否则，
#单线程在处理连接的过程中，无法接受其他客户端的连接：
while True:
	#接受一个新链接
	sock,addr=s.accept()
	#创建新进程来处理TCP链接
	t=threading.Thread(target=tcplink,args=(sock,addr))
	t.start()











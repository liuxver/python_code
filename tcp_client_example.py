#! /usr/bin/env python3
#-*- coding:utf-8 -*-

#导入socket库
import socket
import requests
#创建一个socket链接，创建Socket时，AF_INET指定使用IPv4协议，
#如果要用更先进的IPv6，
#就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议，
#这样，一个Socket对象就创建成功，但是还没有建立连接
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立连接，参数是一个tuple，包含地址和端口号。
s.connect(('www.baidu.com',80))


#a=requests.get('https://www.baidu.com')
#print(a.encoding)



#发送数据,http前面有一个空格
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')

#接收数据
buffer=[]
while True:
	d=s.recv(1024)#每次最多接受1024个字节
	if d:
		buffer.append(d)
	else:
		break

data=b''.join(buffer)

#关闭连接
s.close()

#接收到的数据包括HTTP头和网页本身
#，我们只需要把HTTP头和网页分离一下，
#把HTTP头打印出来，网页内容保存到文件

#data=data.strip("\n")

header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))

#a=html.decode('utf-8')

with open('baidu.txt','wb') as f:
	f.write(html)








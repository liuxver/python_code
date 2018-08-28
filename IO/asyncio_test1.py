#! /usr/bin/env python3
#-*- coding:utf-8 -*-

#用asyncio的异步网络连接来获取sina、sohu和163的网站首页：

#asyncio提供了完善的异步IO支持；
#异步操作需要在coroutine中通过yield from完成；
#多个coroutine可以封装成一组Task然后并发执行。

#eader, writer = yield from connect这里，线程在执行connect操作，挂起，三个网站连接都被挂起，哪个先连接上，先有返回对象，行，sina的连接有返回对象了，通过reader，writer解包进行接下来的操作，只要碰到yield from就挂起，执行tasks里的别的连接任务。
#感觉协程异步相比同步执行节省的时间是就是读取信息流，获得返回对象的时间。相比等待一个连接成功，然后进行操作，操作完继续进行另一个连接，节省的时间就在connect过程中，因为我把三个连接全部开启，谁连上获得对象我就接着执行谁。所以打印出的顺序会不一样。
#相同的获取信息的例子就是把文件读取到内存中：
#line = yield from reader.readline()这也要挂起，你读你的第一行，我继续读下一行。
#同时我觉得yield from内部应该有个消息管道，获取到的信息按顺序排列。



#用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。
#为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
#请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
#把@asyncio.coroutine替换为async；
#把yield from替换为await。




import asyncio

@asyncio.coroutine
def wget(host):
	print('wget %s ...'%host)
	connect=asyncio.open_connection(host,80)
	reader,writer=yield from connect
	header='GET / HTTP/1.0\r\nHost: %s\r\n\r\n'%host
	writer.write(header.encode('utf-8'))

	#刷新底层传输的写缓冲区。也就是把需要发送出去的数据，
	#从缓冲区发送出去。没有手工刷新，asyncio为你自动刷新了。
	#当执行到reader.readline()时，
	#asyncio知道应该把发送缓冲区的数据发送出去了。
	yield from writer.drain()

	while True:
		line=yield from reader.readline()
		if line==b'\r\n':
			break

		print('%s header > %s '%(host,line.decode('utf-8').rstrip()))

	#忽视body ，关闭socket
	writer.close()


loop=asyncio.get_event_loop()
tasks=[wget(host) for host in['www.sina.com.cn','www.sohu.com','www.163.com','www.zhuhu.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()




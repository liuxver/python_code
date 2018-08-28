#! /usr/bin/env python3
#-*- coding:utf-8 -*-

def consumer():
	r=''
	while True:
		n=yield r
		if not n:
			return
		print('[consumer] Consuming %s ...'%n)
		r='200OK'

def produce(c):
	#关于这个地方 传输一个None 参数 完全是
	#因为想要启动一个迭代器  必须要传入一个None参数
	c.send(None)
	n=0
	while n<5:
		n=n+1
		print('[producer] Producing %s ...'%n)
		r=c.send(n)
		print('[producer] Consumer return: %s'%r)

	c.close()

c=consumer()
produce(c)


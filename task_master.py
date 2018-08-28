#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import random,time,queue
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager

task_queue=queue.Queue()#发送任务的队列

result_queue=queue.Queue()#接受结果的队列

#从BaseMager继承的QueueManager：
class QueueManager(BaseManager):
	pass


def return_task_queue():
	global task_queue
	return task_queue

def return_result_queue():
	global result_queue
	return result_queue

def test():
	#把两个queue都注册到网络上 callable对象关联了queue对象
	QueueManager.register('get_task_queue',callable=return_task_queue)
	QueueManager.register('get_result_queue',callable=return_result_queue)

	#绑定端口 5000  设置验证码是 abc
	manager=QueueManager(address=('127.0.0.1',5000),authkey=b'abc')

	#启动queue
	manager.start()


	#获得通过网络访问的queue对象
	task=manager.get_task_queue()
	result=manager.get_result_queue()

	#放几个任务进去

	for i in range(10):
		n=random.randint(0,10000)
		print('Put task %d...'%n)
		task.put(n)

	#从result队列读取结果
	print('Try get results...')
	for i in range(10):
		r=result.get(timeout=10)
		print('Result: %s '%r)

	#关闭
	manager.shutdown()
	print('master exit.')

if __name__=='__main__':
	freeze_support()
	test()




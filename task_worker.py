import time,sys,queue

from multiprocessing.managers import BaseManager
#from multiprocessing.managers import BaseManager


#创建QueueManager  从 BaseManager 继承
class QueueManager(BaseManager):
	pass

#注册到网络上
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#链接到服务器
server_addr='127.0.0.1'
print('Connect to server %s ...'%server_addr)

m=QueueManager(address=(server_addr,5000),authkey=b'abc')
m.connect()

task=m.get_task_queue()
result=m.get_result_queue()

#从task获取任务 将结果存储到result中
for i in range(10):
	try:
		n=task.get(timeout=1)
		print('run task %d * %d ...'%(n,n))
		r='%d * %d = %d '%(n,n,n*n)
		time.sleep(1)
		result.put(r)

	except Queue.Empty:
		print('Task queue is empty.')

print('worker exit.')

import threading


#创建全局的 threadlocal 对象
local_school=threading.local()

def process_student():
	#获取当前线程关联的student
	std=local_school.student
	print('hello , %s (in %s)'%(std,threading.current_thread().name))

def process_thread(name):
	local_school.student=name
	process_student()

t1=threading.Thread(target=process_thread,args=('liuxv',),name=' thread-A ')
t2=threading.Thread(target=process_thread,args=('caomeng',),name=' thread-B ')

t1.start()
t2.start()
t1.join()
t2.join()


import time,threading

balance=0

lock=threading.Lock()  #创建锁变量


def change_it(n):
	global balance
	balance=balance+n
	balance=balance-n

def run_thread(n):
	for i in range(100000):
		lock.acquire()#加锁
		try:
			change_it(n)
		finally:
			lock.release()#使用 try finally 结构  一定要释放锁


#第二个参数必须是可迭代对象  别的不行  不能是 int
t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(5,))

t1.start()
t2.start()
t1.join()
t2.join()

print(balance)







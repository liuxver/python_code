from contextlib import contextmanager


'''
@contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：
class Query(object):
	def __init__(self,name):
		self.name=name

	def query(self):
		print('Query info about %s...'%self.name)

@contextmanager
def create_query(name):
	print('Begin')
	q=Query(name)
	yield q
	print('End')


with create_query('liuxv') as q:
    q.query()

'''
'''
代码的执行顺序是：

with语句首先执行yield之前的语句，因此打印出<h1>；
yield调用会执行with语句内部的所有语句，因此打印出hello和world；
最后执行yield之后的语句，打印出</h1>。
因此，@contextmanager让我们通过编写generator来简化上下文管理

@contextmanager
def tag(name):
    print('<%s>'%name)
    yield
    print('</%s>'%name)

with tag('h1'):
	print('hello')
	print('liuxv')

'''
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://item.jd.com/5487565.html')) as page:
	for line in page:
		print(line)

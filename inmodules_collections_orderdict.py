#! /usr/bin/env python3
#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
#
from collections import OrderedDict
class LastUpdatedOrderedDict(OrderedDict):
	def __init__(self,capacity):
		super(LastUpdatedOrderedDict,self).__init__()
		self._capacity=capacity

	def __setitem__(self,key,value):
		containsKey=1 if key in self else 0
		if(len(self)-containsKey>=self._capacity):
			last=self.popitem(last=False)
			print('Remove:',last)

		if containsKey:
			del self[key]
			print('set:',(key,value))

		else:
			print('add:',(key,value))

		OrderedDict.__setitem__(self,key,value)

ffod=LastUpdatedOrderedDict(3)
print(ffod)
ffod['a']=1
ffod['b']=2
ffod['c']=3
ffod['d']=4




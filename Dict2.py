#! /usr/bin/env python3

' a Dict2 class'
__author__='liuxv'


class Dict(dict):
	'''
	some test :
	d1=Dict()
	d1['x']=100
	d1.x
	100
	'''


	def __init__(self,**kw):
		super().__init__(**kw)

	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'"%key)

	def __setattr__(self,key,value):
		self[key]=value

if __name__=='__main__':
	import doctest
	doctest.testmod()



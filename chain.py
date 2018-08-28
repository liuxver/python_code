#!/usr/bin/env python3
#
'a chain '
__author__='liuxv'

class Chain(object):
	def __init__(self,path=''):
		self._path=path

	def __getattr__(self,path):
		return Chain('%s/%s'%(self._path,path))

	def __str__(self):
		return self._path

	__repr__=__str__

	def __call__(self):
		print("This is a Chain %s "%self._path)


print(Chain().liuxv.a.a)
c=Chain()
c()
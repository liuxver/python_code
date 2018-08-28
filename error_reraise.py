#! /usr/bin/env python3
#
'a error raise to outside'
__author__='liuxv'

def foo(s):
	n=int(s)
	if n==0:
		raise ValueError('invalid value: %s '%s)
	return 10/n

def bar():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError!444')

bar()
#! /usr/bin/env python3

'a error raise test'

__author__='liuxv'

class FooError(ValueError):
	pass

def foo(s):
	n=int(s)

	if n==0:
		raise FooError('invalid value: %s '%s)

	return 10/n

foo('0')
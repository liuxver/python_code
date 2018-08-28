#! /usr/bin/env python3
#
'a logging test'

__author__='liuxv'

import logging

def foo(s):
	return 10/int(s)

def bar(s):
	return foo(s)*2

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)

main()
print('END')
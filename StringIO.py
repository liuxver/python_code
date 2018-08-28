#!/usr/bin/env python3
#
' a test StringIO'

__author__='liuxv'

'''
from io import StringIO
f=StringIO()

f.write('hello')
f.write(' liuxv!')
print(f.getvalue())
'''
from io import StringIO
f=StringIO('hello \n liuxv \n l love you!\nyes ')
while True:
	s=f.readline()
	if s=='':
		break
	print(s.strip())


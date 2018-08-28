#!/usr/bin/env python3
#
'a test for file open'
__author__='liuxv'

'''with open('a.txt','r') as f:
	#print(f.readlines()[0].strip())
	#print(f.read(4))
'''

'''
with open('test.gif','rb') as f:
	print(f.read())

'''
'''with open('a.txt','r',errors='ignore') as f:
	print(f.read().strip())
'''

with open('a.txt','w',encoding='gbk') as f:
	f.write('Hello liuyimeng~')
	f.write('我真的爱你！')
	

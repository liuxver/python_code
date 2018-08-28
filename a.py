#!/usr/bin/env python3

def trangle(x):
	a=[]
	b=[]
	n=1
	if n==1&x==1:
		b.append(1)
		yield b
		return 'done'
	if x==2:
		a.append(1)
		yield a
		b.append(1)
		b.append(1)
		yield b
		return 'done'
	while n<=x:
		if n==1:
			b.append(1)
			yield b
		if n==2:
			a.append(1)
			b.append(1)
			b.append(1)
			yield b
		i=0
		while i<(n-1):
			if i==0:
				b.append(1)
			b.append(a[i-1]+a[i])
		b.append(1)
		yield b
		a=b
		n=n+1
	return 'done'




g=trangle(10)

while True:
	try:
		x=next(g)
		print('g:',x)
	except StopIteration as e:
		print("Return value:",e.value)
		break;
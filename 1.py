import numpy as np 
a=np.random.random((4,4,))
print(a)

b=np.mat(np.random.random((4,4)))
print(b)

print(b.I)
print("now the b*b.I")
print(b*b.I)

myeye=b*b.I
myeye-np.eye(4)
print(myeye)

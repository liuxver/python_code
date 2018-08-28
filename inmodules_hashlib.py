import hashlib
md5=hashlib.md5()
md5.update('l love xiaomengmeng  -- liuxv '.encode('utf-8'))
#print(md5.hexdigest())
md5.update('l love wuyue --liuxv'.encode('utf-8'))
print(md5.hexdigest())

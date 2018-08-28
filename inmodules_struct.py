import struct

print(struct.pack('>I',10240099))
print(struct.unpack('>IH',b'\x00\x00\x04\x00\x80\x80'))

with open('a.bmp','rb') as f:
	s=f.read(30)

print(s)
print(struct.unpack('<ccIIIIIIHH',s))

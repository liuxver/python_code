import hmac
message=b'l love wuyue'
key=b'liuxv'
h=hmac.new(key,message,digestmod='MD5')
print(h.hexdigest())
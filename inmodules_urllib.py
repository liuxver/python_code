#！ /usr/src/bin python3
# -*- coding: utf-8 -*-
#from urllib import request
'''
#对网页的抓取
#with request.urlopen('https://item.jd.com/5487565.html') as f:
#with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
##https://zh.wikipedia.org/wiki/%E7%BE%8E%E8%A1%93
with request.urlopen('http://www.liuxv.cn') as f:
	data=f.read()
	print('Status:',f.status,f.reason)
	for k,v in f.getheaders():
		print('%s:%s'%(k,v))

	print('Data:',data.decode('utf-8'))

'''


#模拟iphone6去请求豆瓣首页
'''
#from urllib import request
req=request.Request('http://www.liuxv.cn')
req.add_header('User-Agent','Mozilla/6.0(iPhone;CPU iPhone os 8_0 like Mac OS X ) AppleWebKit/536.26 (KHTML,like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
	print('Status:',f.status,f.reason)
	for k,v in f.getheaders():
		print('%s:%s'%(k,v))

	print('Data:',f.read().decode('utf-8'))

'''

'''
我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式
from urllib import request,parse

print('Login to weibo.cn')
email=input('Email:')
password=input('Password:')
login_data=parse.urlencode([
	('username',email),
	('password',password),
	('entry','mweibo'),
	('client_id',''),
	('savestate','1'),
	('ec',''),
	('pagerefer','https://passport.weibo.cn/siginin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
	])

req=request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin','https://passport.weibo.cn')
req.add_header('User-Agent','Mozilla/6.0(iPhone;CPU iPhone os 8_0 like Mac OS X ) AppleWebKit/536.26 (KHTML,like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

req.add_header('Referer','https://passport.weibo.cn/siginin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
with request.urlopen(req,data=login_data.encode('utf-8')) as f:
	print('Status:',f.status,f.reason)
	for k,v in f.getheaders():
		print('%s:%s'%(k,v))

	print('Data:',f.read().decode('utf-8'))
'''

from urllib import request,parse

print('Login to JD.com')
email=input('phone/email:')
password=input('Password:')
login_data=parse.urlencode([
	('username',email),
	('password',password),
	('entry','mweibo'),
	('client_id',''),
	('savestate','1'),
	('ec',''),
	('pagerefer','https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F%3Fcu%3Dtrue%26utm_source%3Dbaidu-pinzhuan%26utm_medium%3Dcpc%26utm_campaign%3Dt_288551095_baidupinzhuan%26utm_term%3D0f3d30c8dba7459bb52f2eb5eba8ac7d_0_1144e02a30df4e9aabad72e9da648916')
	])

req=request.Request('https://passport.jd.com/new/login.aspx')
req.add_header('Origin','https://www.jd.com')
req.add_header('User-Agent','Mozilla/6.0(iPhone;CPU iPhone os 8_0 like Mac OS X ) AppleWebKit/536.26 (KHTML,like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

req.add_header('Referer','https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F%3Fcu%3Dtrue%26utm_source%3Dbaidu-pinzhuan%26utm_medium%3Dcpc%26utm_campaign%3Dt_288551095_baidupinzhuan%26utm_term%3D0f3d30c8dba7459bb52f2eb5eba8ac7d_0_1144e02a30df4e9aabad72e9da648916')


with request.urlopen(req,data=login_data.encode('utf-8')) as f:
	print('Status:',f.status,f.reason)
	for k,v in f.getheaders():
		print('%s:%s'%(k,v))

	print('Data:',f.read().decode('charset=GBK'))








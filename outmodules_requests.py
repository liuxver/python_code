#! /usr/bin/env python3
#-*- coding:utf-8 -*-

import requests

#使用get访问页面
'''
r=requests.get('https://www.douban.com/')

print(r.status_code)
print(r.text)

'''

'''
searchthing=input('Enter your want:')

r=requests.get('https://search.jd.com/Search',params={'keyword':searchthing})
#获取访问的实际url
print(r.url)

#获取编码格式
print(r.encoding)

#获取所有的内容
print(r.content)

'''

'''
直接获取JSON（JavaScript 对象标记） 
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())


'''



'''
需要传入HTTP Header时，我们传入一个dict作为headers参数：

r=requests.get('https://www.douban.com',headers={'User-Agent':'Mozilla/5.0 (iPhone;CPU iphone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.text)

'''

r=requests.post('https://accounts.douban.com/login',data={'form_email':'1369058574@qq.com','form_password':'123456789liu'})

print(r.url)
print(r.headers)
print(r.cookies['ts'])









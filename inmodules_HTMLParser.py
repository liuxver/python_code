#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# 
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import sys
class MyHTMLParser(HTMLParser):
	def handle_starttag(self,tag,attrs):
		print('<%s>'%tag)

	def handle_endtag(self,tag):
		print('</%s>'%tag)

	def handle_startendtag(self,tag,attrs):
		print('<%s/>'%tag)

	def handle_data(self,data):
		print(data)

	def handle_comment(self,data):
		print('<!--',data,'-->')

	def handle_entityref(self,name):
		print('&%s;'%name)

	def handle_charref(self,name):
		print('&#%s;'%name)


parser=MyHTMLParser()
with request.urlopen('http://www.baidu.com') as f:
	data=f.read()
	html=data.decode("utf-8")
	parser.feed(html)
	#parser.feed(data.decode='utf-8')
	#fo=open("liuxv.html",mode="w",encoding="utf-8")
	#fo.write(data)
	#print(data)
	#print(data)
	#str(data,encoding="utf-8")
	#data.decode('utf-8')
	##data.decode('utf-8')
	#print(data)
	#parser.feed(data)
'''	
parser.feed(<html>#有三个单引号
	<head></head>
	<body>
	<!-- test html parser -->
		<p>some <a href=\"#\">HTML&nbsp;tutorial...<br>END</p>
	</body></html>)#有三个单引号
'''
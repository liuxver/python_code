#！ /usr/bin/env python3
#-*- coding:utf-8 -*-
#
import poplib

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr





#邮件地址 密码和服务器地址
email='1369058574@qq.com'
password='pnywzdormtoobaae'
pop3_server='pop.qq.com'

#连接到pop3服务器
server=poplib.POP3_SSL(pop3_server,995)
#打开调试信息
server.set_debuglevel(1)
#打印服务器端的欢迎信息
print(server.getwelcome().decode('utf-8'))

#身份认证
server.user(email)
server.pass_('pnywzdormtoobaae')

#stat()返回邮件数量和占用空间
print('Message:%s . \n Szie:%s '%server.stat())
#list()返回所有邮件编号
resp,mails,octets=server.list()
#查看返回的列表
print(mails)

#获取最新的一封邮件，索引号从1开始
index=len(mails)
resp,lines,octets=server.retr(index)

#lines存储量邮件的原始文本的每一行，
#可以获得整个邮件的原始文本

msg_content=b'\r\n'.join(lines).decode('utf-8')
#稍后解析出邮件：
msg=Parser().parsestr(msg_content)


#可以根据邮件索引号直接嗯从服务器端删除邮件
#应  server.dele(index)
server.quit()

def decode_str(s):
	value,charset=decode_header(s)[0]
	if charset:
		value=value.decode(charset)
	return value


def guess_charset(msg):
	charset=msg.get_charset()
	if charset is None:
		content_type=msg.get('Content-Type','').lower()
		pos=content_type.find('charset=')
		if pos>=0:
			charset=content_type[pos+8:].strip()

	return charset




#indent用于缩进显示
def print_info(msg,indent=0):
	if indent==0:
		for header in ['From','To','Subject']:
			value=msg.get(header,'')
			if value:
				if header=='Subject':
					value=decode_str(value)
				else:
					hdr.addr=parseaddr(value)
					name=decode_str(hdr)
					value=u'%s <%s>'%(name,addr)

			print('%s %s : %s'%(' '*indent,header,value))

	if (msg.is_multipart()):
		parts=msg.get_payload()
		for n,part in enumerate(parts):
			print('%spart %s '%(' '*indent,n))
			print('%s-------------------'%(' '*indent))
			print_info(part,indent+1)

	else:
		content_type=msg.get_content_type()
		if content_type=='text/plain' or content_type=='text/html':
			content=msg.get_payload(decode=True)
			charset=guess_charset(msg)
			if charset:
				content=content.decode(charset)

			print('%sText: %s'%(' '*indent,content+'...'))
		else:
			print('%sAttachment: %s'%(' '*indent,content_type))









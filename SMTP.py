#! /usr/bin/env python3
#-*- coding:utf-8 -*-
#

from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.mime.multipart import MIMEBase,MIMEMultipart
from email.utils import parseaddr,formataddr
#from email.mime.text import MIMEMultipart
import smtplib


#编写了一个函数_format_addr()来格式化一个邮件地址。
#注意不能简单地传入name <addr@example.com>，
#因为如果包含中文，需要通过Header对象进行编码。

def _format_addr(s):
	name,addr=parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))




#通过SMTP发送出去

#输入邮箱和密码
#from_addr=input('From:')
from_addr='1369058574@qq.com'
#password=input('Password:')
password='isogktdhidvfjfeg'

#输入收件人地址
#to_addr=input('To:')
to_addr='liuxver@icloud.com'
#smtp_server=input('SMTP server:')
##qq邮箱的发送端口号是 465 或者587
#qq邮箱的接受端口号是 995,使用SMTP_SSL()来配置
smtp_server='smtp.qq.com'


#构造MIMEText对象时，第一个参数就是邮件正文，
#第二个参数是MIME的subtype，传入'plain'表示纯文本，
#最终的MIME就是'text/plain'，
#最后一定要用utf-8编码保证多语言兼容性
#如果要发送html邮件 将’plain‘ 改成 html就好了
#msg=MIMEText('Hello,l love you! --liuxv','plain','utf-8')
#msg=MIMEText('<html><body><h1> l love you ,wuyue</h1><a href="http://www.liuxv.cn"> click this </a></body></html>','html','utf-8')


#发送附件
#建立邮件对象
#如果要求同时支持html和plain格式 那么 必须制定 subtype 为alternative 
#然后将两种格式都绑定到邮件对象上面
#nsg=MIMEMultipart('alternative')
#
msg=MIMEMultipart()

#发件人
msg['From']=_format_addr('你最爱的liuxver<%s>'%from_addr)
#收件人
msg['to']=_format_addr('我最爱的悦悦<%s>'%to_addr)
#主题
msg['Subject']=Header('来自远方的问候......','utf-8').encode()

#邮件正文是MIMEText:
msg.attach(MIMEText('Hello,l love you! --liuxv','plain','utf-8'))

#插入附件 图片
with open('img/a.bmp','rb') as f:
	#设置文件的MIME和文件名，还有文件类型
	mime=MIMEBase('image','bmp',filename='a.bmp')
	#加上必要的头信息
	mime.add_header('Content-Disposition','attachment',filename='a.bmp')
	mime.add_header('Content-ID','<0>')
	mime.add_header('X-Attachment-Id','0')

	#把附件的内容读进来
	mime.set_payload(f.read())
	#用base64编码
	encoders.encode_base64(mime)
	#添加到邮件对象中
	msg.attach(mime)

#要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，
#先把邮件作为附件添加进去，然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。
#如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
msg.attach(MIMEText('<html><body><h1>l love you </h1>'+
	'<p><img src="cid:0"></p>'+
	'</body></html>','html','utf-8'))



#使用gmail邮箱发送
try:
	server=smtplib.SMTP('smtp.gmail.com',587)#gmail的SMTP协议默认端口是587
	server.starttls()
	server.set_debuglevel(1)
	server.login('liuxver444@gmail.com','123456789@liuxv')
	server.sendmail('liuxver444@gmail.com',[to_addr],msg.as_string())
	print('发送成功')
except server.SMTPException:
	print('发送失败')
finally:
	server.quit()

'''
使用qq邮箱发送
try:
	server=smtplib.SMTP_SSL(smtp_server,465)#SMTP协议默认端口是25
	server.set_debuglevel(1)
	server.login(from_addr,password)
	server.sendmail(from_addr,[to_addr],msg.as_string())
	print('发送成功')
except server.SMTPException:
	print('发送失败')
finally:
	server.quit()

'''





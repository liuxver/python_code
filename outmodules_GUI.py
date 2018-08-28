#! /usr/bin/env python3
#-*- coding:utf-8 -*-
#

from tkinter import *
import tkinter.messagebox as messagebox
'''
一个显示退出按钮和一行文字的对话框
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel=Label(self,text='hello liuxv.')
		self.helloLabel.pack()
		self.quitButton=Button(self,text='Quit',command=self.quit)
		self.quitButton.pack()




app=Application()
app.master.title('hello liuxv')
app.mainloop()

'''

class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()


	def createWidgets(self):
		self.nameInput=Entry(self)
		self.nameInput.pack()
		self.alertButton=Button(self,text='hello ',command=self.hello) 
		self.alertButton.pack()

	def hello(self):
		name=self.nameInput.get() or 'world'
		messagebox.showinfo('Message','hello ,%s '%name)


app=Application()
app.master.title('hello world.')
app.mainloop()



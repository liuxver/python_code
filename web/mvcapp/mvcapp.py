#! /usr/bin/env python3
#-*- coding:utf-8 -*-

import mysql.connector
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	return render_template('home.html')

@app.route('/login',methods=['GET'])
def login():
	return render_template('login.html')



def findUser(username,password):
	connect=mysql.connector.connect(user='root',password='1234',database='mvctest')
	cursor=connect.cursor()
	cursor.execute('select * from users where name=%s and password=%s',(username,password))
	fetchall=cursor.fetchall()
	size=len(fetchall)
	connect.close()
	if size==1:
	    return True
	return False




@app.route('/login',methods=['POST'])
def loginin():
	username=request.form['username']
	password=request.form['password']
	flag=findUser(username,password)
	if flag:
		return render_template('loginin.html',username=username)
	return render_template('login.html',message='用户名或者密码错误',username=username)

if __name__=='__main__':
	app.run()





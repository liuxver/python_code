#! /usr/bin/env python3
#-*- coding:utf-8 -*-

#导入mysql驱动
import mysql.connector

#连接到数据库 创建游标
#
conn=mysql.connector.connect(user='root',password='1234',database='test')
cursor=conn.cursor()

#创建user表
cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')

#插入一行记录  mysql的占位符是%s
cursor.execute('insert into user (id,name) values (%s,%s)',['1','liuxv'])
print(cursor.rowcount)

#提交事务
conn.commit()
cursor.close()

#运行查询
cursor=conn.cursor()
cursor.execute('select * from user where id=%s',('1',))
values=cursor.fetchall()
print(values)

cursor.close()
conn.close()

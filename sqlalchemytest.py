#! /usr/bin/env python3
#-*- coding:utf-8 -*-

#导入 各种模块
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类
Base=declarative_base()

#定义user类
class User(Base):
	#表的名字
	__tablename__='user'
	#表的结构
	id=Column(String(20),primary_key=True)
	name=Column(String(20))



#初始化数据库链接
engine=create_engine('mysql+mysqlconnector://root:1234@localhost:3306/test')
#创建DESession类型
DBSession=sessionmaker(bind=engine)



#插入数据
#创建session对象
session=DBSession()
#创建新的User对象
new_user=User(id='5',name='Bob')
#添加到seesion
session.add(new_user)
#提交及保存到数据库
session.commit()
#光比session
session.close()


#查询数据
session=DBSession()
#创建Query查询，filter是where条件
#最后调用one()返回唯一行，如果是all()返回所有行
user=session.query(User).filter(User.id=='5').one()
print('type:',type(user))
print('name:',user.name)

#关闭session
session.close()











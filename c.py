#!/usr/bin/env python3

'a test of class'

__author__='liuxv'

class Student(object):
	"""docstring for Studentt"""
	#def __init__(self, name,age):
	#	self.__name=name
	#	self.__age=age

	def print_student(self):
		print('%s : %s '%(self.__name,self.__age))

	def get_name(self):
		return self.__name

	def get_age(self):
		return self.__age

	def set_name(self,s):
		self.__name=s

	def set_age(self,a):
		self.__age=a

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self,value):
		if not isinstance(value,int):
			raise ValurError("age must be integer!")

		if value<0 or value>100:
			raise VauleError('age must between 0 -100')

		self.__age=value







		

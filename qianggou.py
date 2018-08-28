from splinter.browser import Browser
import time
import os

import platform

from subprocess import Popen, STDOUT

from selenium.common.exceptions import WebDriverException

from selenium.webdriver.common import utils

import time

def login(b):
	b.click_link_by_text("你好，请登录")
	time.sleep(3)
	b.fill("loginname","13201667317")
	b.fill("nloginpwd","123456789liu")
	b.find_by_id("loginsubmit").click()
	time.sleep(3)
	return b

#http://item.jd.com/2707976.html

def loop(b):
	try:
		if b.title=="订单结算页 -京东商城":
			b.find_by_text("保存收货人信息").click()
			b.find_by_text("保存支付方式及配送方式").click()
			b.find_by_id("order-submit").click()
			return b
		else:
			b.visit("http://item.jd.com/2707976.html")
			b.find_by_id("choose-btn-qiang").click()
			time.sleep(10)
			loop(b)
	except Exception as e:
		b.reload()
		time.sleep()
		loop(b)

b=Browser(dirver_name="chrome")
b.visit("http://item.jd.com/2707976.html")
login(b)
b.find_by_id("choose-btn-qiang").click()
time.sleep(10)
while True:
	loop(b)
	if b.is_element_present_by_id("tryBtn"):
		b.find_by_id("tryBtn").click()
		time.sleep(6.5)
	elif b.title=="订单结算页 -京东商城":
		b.find_by_id("order-submit").click()
	else:
		print('抢购成功！')
		break

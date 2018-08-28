#! /usr/bin/env python3
# -*- coding:utf-8 -*-
#

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

def randomchar():
	return chr(random.randint(65,90))

def randomcolor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def randomcolor2():
	return (random.randint(32,127),random.randint(32,177),random.randint(32,177))


width=60*4
height=60
#建立一个新文件
image=Image.new('RGB',(width,height),(255,255,255))

#设置字体
font=ImageFont.truetype('arial.ttf',36)
#画出这个文件
draw=ImageDraw.Draw(image)

#随机颜色
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=randomcolor())
#随机字符
for t in range(4):
	draw.text((60*t+10,10),randomchar(),font=font,fill=randomcolor2())

#虚化
image=image.filter(ImageFilter.BLUR)
#保存
image.save('img/a.jpg','jpeg')


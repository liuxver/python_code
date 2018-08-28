#! /usr/bin/env python3
#-*- coding:utf-8 -*-

from PIL import Image
from PIL import ImageFilter#添加滤镜

im=Image.open('img/a.bmp')

#获得图像尺寸
w,h=im.size
print('image size:%sx%s'%(w,h))

#将图像缩小为1/2
im.thumbnail((w//2,h//2))
print('Resize image to : %sx%s'%(w//2,h//2))

#将缩小后的图像保存
im.save('img/thumbnail.jpg','jpeg')


#将图像模糊后  保存下来
im=Image.open('img/a.bmp')
im2=im.filter(ImageFilter.BLUR)
im2.save('img/blur.jpg','jpeg')


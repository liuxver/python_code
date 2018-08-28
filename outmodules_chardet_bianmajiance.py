#! /usr/bin/env python3
#-*- coding:utf-8 -*-
#

import chardet
print(chardet.detect(b'love you'))

data='床前明月光，疑是地上霜'.encode('gbk')
print(chardet.detect(data))

data='床前明月光，疑是地上霜'.encode('utf-8')
print(chardet.detect(data))

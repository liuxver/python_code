#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from datetime import datetime,timedelta
#now=datetime.now()
#print(now)
dt=datetime(1997,12,12,5,20)
print(dt)
print(dt.timestamp())
print(datetime.fromtimestamp(66666666.0))
cday=datetime.strptime('1997-12-12 5:20:00','%Y-%m-%d %H:%M:%S')
print(cday)
print(dt.strftime('%a,%b %d %H:%M'))

#print(type(now))
dt=datetime.now()
print(dt)
print(dt+timedelta(hours=10))

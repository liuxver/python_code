#! /usr/bin/env python3
#-*- coding:utf-8 -*-



#然后编写一个HTTP服务器，分别处理以下URL：
#/ - 首页返回b'<h1>Index</h1>'；
#/hello/{name} - 根据URL参数返回文本hello, %s!。



import asyncio
from aiohttp import web

async def index(request):
	await asyncio.sleep(1)
	return web.Response(body=b'<h1>index</h1>')

async def hello(request):
	await asyncio.sleep(1)
	text='<h1>Hello,%s !</h1>'%request.match_info['name']
	return web.Response(body=text.encode('utf-8'))

async def init(loop):
	app=web.Application(loop=loop)
	app.router.add_route('GET','/',index)
	app.router.add_route('GET','/hello/{name}',hello)
	srv=await loop.create_server(app.make_handler(),'127.0.0.1',8000)
	print('Server started at http://127.0.0.1:8000 ...')
	return srv

loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


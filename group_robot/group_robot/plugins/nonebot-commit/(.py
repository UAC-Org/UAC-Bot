from nonebot import on_message,on_command
from nonebot.rule import to_me,keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message
import re, json, threading, datetime, os
az = on_message(block = False, priority = -2)
start = on_command("启动统计", block = True, priority = -2, rule = to_me())
close = on_command("关闭统计", block = True, priority = -2, rule = to_me())
look = on_command("查看", block = True, priority = -2, rule =to_me())
clean = on_command("清空", block = True, priority = -2, rule = to_me())
new = on_command("新增统计", block = True, priority = -2, rule = to_me())
Admin = '2654625014'
find = re.compile(r'[(（)）]')
def judge_time_thread():
	while True:
		time = datetime.datetime.now()
		if time.hour == 0 and time.minute == 0 and time.second == 0:
			with open(os.path.abspath('data.json'), 'r', encoding = 'utf-8') as data:
				jsdata = json.load(data)

			jsdata['new'] = 0

			with open(os.path.abspath('data.json'), 'w', encoding = 'utf-8') as data:
				data.write(json.dumps(jsdata))
		else:
		    	pass
thread_new = threading.Thread(target = judge_time_thread)
thread_new.start()
@az.handle()
async def _(bot: Bot, event: Event, state:T_State):
    with open(os.path.abspath('data.json'), 'r', encoding = 'utf-8') as data:
       jsdata = json.load(data)
    if jsdata['start'] == True:
       result = find.findall(str(event.get_message()))
       jsdata['times'] += len(result)
       jsdata['new'] += len(result)
       with open(os.path.abspath('data.json'), 'w', encoding = 'utf-8') as data:
           data.write(json.dumps(jsdata))
    else:
        pass

@start.handle()
async def s(bot: Bot, event: Event, state: T_State):
    with open(os.path.abspath('data.json'), 'r', encoding = 'utf-8') as data:
        jsdata = json.load(data)
    if jsdata['start'] == True:
        await start.send("开启过了")
    else:
        jsdata["start"] = True
        with open(os.path.abspath('data.json'), 'w', encoding = 'utf-8') as data:
            data.write(json.dumps(jsdata))
        await start.send("启动成功")

@close.handle()
async def c(bot: Bot, event: Event, state: T_State):
    global Admin
    if str(event.get_user_id()) == Admin:
        with open(os.path.abspath('data.json'), 'r', encoding = 'utf-8') as data:
            jsdata = json.load(data)
        if jsdata['start'] == False:
            await close.send("关闭过了")
        else:
            jsdata["start"] = False
            with open(os.path.abspath('data.json'), 'w', encoding = 'utf-8') as data:
                data.write(json.dumps(jsdata))
            await close.send("关闭成功")
    else:
       await close.send("对不起，您的权限不足")
@look.handle()
async def l(bot: Bot, event: Event, state: T_State):
	with open(os.path.abspath('data.json'), 'r', encoding = 'utf-8') as data:
        jsdata = json.load(data)
    await look.send("嘿嘿群友好腻害，已经各种括号了%s次了" % (jsdata['times']))
@clean.handle()
async def cl(bot: Bot, event: Event, state: T_State):
	with open(os.path.abspath('data.json'), 'r', encoding = 'utf-8') as data:
		jsdata = json.load(data)
	if str(event.get_user_id()) == Admin:
		jsdata['times'] = 0
		with open(os.path.abspath('data.json'), 'w', encoding = 'utf-8') as data:
			data.write(json.dumps(jsdata))
		await clean.send("Done.")
	else:
		await clean.send("没有这个权利（")
@new.handle()
async def n(bot: Bot, event: Event, state: T_State):
	with open(os.path.abspath('data.json'), 'r', encoding = 'utf-8') as data:
		jsdata = json.load(data)
	await new.send("当日新增%s个各种括号，今天真是括多的一天呢！"%(jsdata['new']))

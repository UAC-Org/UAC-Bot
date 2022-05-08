from nonebot import on_command,on_keyword
from nonebot.rule import to_me,keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message
import datetime
morning = on_command("早上好", rule = to_me(), priority = -1, block = True)
night = on_command("晚上好", rule = to_me(), priority = -1, block = True)
noon = on_command("中午好", rule = to_me(), priority = -1, block = True)
afternoon = on_command("下午好", rule = to_me(), priority = -1, block = True)
@morning.handle()
async def _(bot: Bot, event: Event, state: T_State):
	dt = datetime.datetime.now()
	if dt.hour >= 5 and dt.hour <= 10:
		await morning.send("早啊qwq")
	elif dt.hour < 5:
		await morning.send("请不要熬夜qwq")
	elif dt.hour > 10:
		await morning.send("不早了，挺晚的……")
@noon.handle()
async def __(bot: Bot, event: Event, state: T_State):
	dt = datetime.datetime.now()
	if dt.hour > 10 and dt.hour <=14:
		await noon.send("午好，吃了么？")
	elif dt.hour > 14:
		await noon.send("现在似乎是下午了……")
	else:
		await noon.send("晚")
@night.handle()
async def ___(bot: Bot, event: Event, state: T_State):
	dt = datetime.datetime.now()
	if dt.hour >=18 and dt.hour <= 22:
		await night.send("晚好啊~要涩图吗？（不是）")
	elif dt.hour >22 and dt.hour <5:
		await night.send("晚安~早点睡吧~")
	elif dt.hour >=5 and dt.hour <12:
		await night.send("真晚啊，您美国的吧")
	else:
		await night.send("?您可能不太理解什么叫'晚'")
@afternoon.handle()
async def ____(bot: Bot, event: Event, state: T_State):
	dt = datetime.datetime.now()
	if dt.hour > 14 and dt.hour < 18:
		await afternoon.send("下午好！要来杯下午猹吗？")
	else:
		await afternoon.send("现在不是下午呢，没有猹。不过要来份意大利面吗")


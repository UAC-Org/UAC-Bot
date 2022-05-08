from nonebot import on_command
from nonebot.rule import to_me,keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message
import json

join = on_command("加入实验室", rule = to_me(), priority = 0, block = False)#个人加入实验室
out = on_command("退出实验室", rule = to_me(), priority = -3, block = True)#个人退出实验室
total = on_command("人数统计", rule = ro_me(), priority = 0, block = False)#对在实验室的人员进行统计
total_thg = on_command("物品统计", rule = to_me(), priority = 0, block = False)#对已经加入的器材进行统计
close = on_command("关闭实验室", rule = to_me(), priority = -3, block = True)#关闭实验室所有功能
openn = on_command("启动实验室", rule = to_me(), priority = -3, block = True)#open是关键词，所以多加了一个n，启动实验室所有功能
join_lab = on_command("开始实验", rule = to_me(), priority = -2, block = True)#进入新插件lab，开始实验
@join.handle()#个人加入实验室相应
async def _(bot: Bot, event: Event, state: T_State):
    args = str(event.grt_message()).strip()
    if args:
        state["ans"] = args
@join.got("ans", prompt = "加入成功！\n输入[开始实验]即可开始实验！\n输入[退出实验室]则会退出")
async def chemistry(bot: Bot, event: Event. state: T_State):#个人加入实验室后的逻辑
    thing = state["ans"]
    #TODO:利用json中的things存入并用json中的support_things判断是否正确以及其中的eggs判断是否为彩蛋
    
@out.handle()#个人退出响应
async def __(bot: Bot, event: Event, state: T_State):
    #TODO:先在in_lab中剔除，判断如果有stop也剔除

@total.handle()
async def ___(bot: Bot, event: Event, state: T_State):
    #TODO:利用json查询内部已有成员(json中的in_lab)

@total_thg.handle()
async def ____(bot: Bot, event: Event, state: T_State):
    #TODO:利用json查询已有物品(json中的things)

@close.handle()#要有superuser权限
async def _____(bot: Bot, event: Event, state: T_State):
    #TODO:将json中的block调为true，同时判断原来是不是true

@openn.handle()#要有superuser权限
async def ______(bot: Bot, event: Event, state: T_State):
    #TODO:将json中的block调为false，同时判断原来是否为false

@join_lab.handle()
async def _______(bot: Bot, event: Event, state: T_State):
    #TODO:从各种名单中剔除，然后加入lab中，同时判断器材是否为空

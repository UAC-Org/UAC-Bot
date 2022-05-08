#!/usr/bin/python3
#谨以此项目纪念阿云(
from nonebot import on_message, on_command
from nonebot.typing import T_State
from nonebot.rule import to_me
from nonebot.adapters import Bot
from nonebot.adapters.cqhttp.event import GroupMessageEvent
schedule = on_command("日程", priority = 0, block = False)
@schedule.handle()
async def sce(bot: Bot, event:GroupMessageEvent):
    

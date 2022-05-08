#! /usr/bin/python3
from xml.dom import NoModificationAllowedErr
from nonebot import on_message, on_command
from nonebot.typing import T_State
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
import os
start_collect = on_message(block = False, priority = -100)
read = on_command("record", block = False, priority = 0, rule = to_me())
@start_collect.handle()
async def record(bot: Bot, event: Event, state: T_State):
    usr = str(event.user_id)
    if usr == "706327600" or usr == "2654625014":
        file = open("record.txt","a")
        msg = str(event.get_message())
        file.write(usr + ' ' + msg + '\n\n')
        file.close()
@read.handle()
async def _(bot: Bot, event: Event, state: T_State):
    try:
        await bot.call_api("upload_group_file", group_id = event.group_id, file = os.path.abspath("record.txt"), name = "rec.txt")
    except NoModificationAllowedErr:
       await  read.send("ERROR:There's no file!")
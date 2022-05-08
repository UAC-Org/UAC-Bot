from nonebot import on_command,on_keyword
from nonebot.rule import to_me,keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message
record = on_keyword("",priority=0,block=False)
put_up = on_keyword("调取",rule=to_me(),priority=0,block=False)
file = open("记录.txt","a")
Aming=[2654625014,3403388302]
@record.handle()
async def record_handle(bot: Bot, event:Event , state: T_State):
    gi = event.group_id
    msg = str(event.get_message())
    file.write(msg)
    file.save()
    file = open("记录.txt","a")
@put_up.handle()
async def put_handle(bot: Bot, event:Event , state: T_State):
    gi = event.group_id
    if event.user_id in Aming:
        await bot.upload_file(group_id = gi, file = "C:/Users/yang/group_robot/记录.txt", name = "记录", folder = "group_robot")
        await put_up.send("操作成功！已经上传了~~~")
    else:
        await put_up.send("权限不足，操作失败")

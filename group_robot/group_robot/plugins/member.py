from nonebot import on_command
from nonebot.rule import to_me,keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message
member = on_command("版本", rule = to_me(), priority=-70, block=True)
@member.handle()
async def member_handle(bot: Bot, event : Event, state = T_State):
    await member.send('''当前版本：正式版\n版本号:2.2.0\n开发者:铭心,贝壳\n技术支持:NCBM,RK\n恭喜我于1.15上服运行！''')

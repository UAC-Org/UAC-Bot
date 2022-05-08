from nonebot.permission import SUPERUSER
from nonebot import on_command
from nonebot.adapters import Bot
from nonebot.rule import to_me,keyword
from nonebot.adapters.cqhttp import MessageEvent
import subprocess as sub
update = on_command("更新",rule=to_me())
@update.handle()
async def update(bot: Bot,event: MessageEvent):
    try:
        if await SUPERUSER(bot,event):
                sub.run(["git","pull"])
                await update.send("更新成功")
        else:
            await update.send("没门")
    except:
        await update.send("出现了一些错误，似乎没法更新呢")

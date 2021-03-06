from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event, Message

from .run import run

runcode = on_command('code', priority=5)


@runcode.handle()
async def _(bot: Bot, event: Event):
    code = str(event.get_message()).strip()
    res = await run(code)
    await runcode.send(message=Message(res), at_sender=True)

__usage__ = """
发送
code [语言] [-i] [inputText]
[代码]
-i：可选 输入 后跟输入内容
运行代码示例(python)(无输入)：
    code py
        print("sb")
运行代码示例(python)(有输入)：
    code py -i 你好
        print(input())
        
目前仅支持c/cpp/c#/py/php/go/java/js
运行于：https://glot.io/
"""
from nonebot import on_command
from nonebot.rule import to_me,keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message
feedback = on_command("反馈-实验室",priority= -35,block = True,rule = to_me())
@feedback.handle()
async def feed_back_handle(bot: Bot, event: Event, state: T_State):
    global user_id
    user_id=event.user_id
    args = str(event.get_message()).strip()
    if args:
        state["feed"] = args
@feedback.got("feed",prompt="请说出您对我的建议，我会尽快改进的，爱你哟")
async def feed_feed(bot: Bot, event: Event, state: T_State):
    global user_id
    ans = str(user_id)+"给了你一个建议：" + str(state["feed"])
    await bot.send_private_msg(user_id= 2654625014, message= ans)
    msg = "[CQ:at,qq=%s]"%(user_id) + "反馈成功awa"
    await feedback.send(Message(msg))

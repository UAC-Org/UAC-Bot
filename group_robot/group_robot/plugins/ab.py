from nonebot import on_command,on_keyword
from nonebot.rule import to_me,keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message
import random as ran
classs = ["整一个","[CQ:at,qq=2751308385]随机事件 整一个 南舟是**",
          "[CQ:at,qq=2751308385] 随机事件 114514 1919810",
          "[CQ:at,qq=2751308385] 随机事件 NCBM好屑 Rk好屑啊"]
high_medicine = ["pirnt(f'asjflaksfjiqo%s'%sss)",
                 "int miam()",
                 "retrun 0;",
                 "1号元素是He",
                 "你暴沸了",
                 "你喝的盐酸，不是矿泉水",
                 "你作业被我撕了",
                 "别升压了，再升压医生也救不了你了",
                 "你玻璃位置放错了",
                 "1145141919810提醒您：我不臭",
                 "你家进苦力怕了",
                 "你合金块掉虚空里面了",
                 "你下矿挖到毒蜘蛛洞穴了",
                 "你线蓝了",]
hello = on_command("你好",rule=to_me(), priority=0,block=True)
abaaba = on_command("教训",priority=-20,block=True)
high = on_command("升压药",priority=-30,block=True)
dangerous = on_command("危",priority=-60,block=True)
@hello.handle()
async def hello_handle(bot: Bot, event: Event, state: T_State):
    msg = f"[CQ:at,qq={event.user_id}] 我很不好"
    await hello.send(Message(msg))
@abaaba.handle()
async def abaaba_handle(bot: Bot, event: Event, state: T_State):
    get_msg = str(event.get_message())
    if "整" in get_msg:
        await abaaba.send("我怎么能和那玩楞相提并论")
    else:
        msg = classs[ran.randint(0,3)]
        await abaaba.send(Message(msg))
@high.handle()
async def high_handle(bot: Bot, event: Event, state: T_State):
    global user_id
    user_id = event.user_id
    args = str(event.get_message()).strip()
    if args:
          state["ans"] = args
@high.got("ans",prompt="回复[我确定]以获得升压药")
async def high_high(bot: Bot, event: Event, state: T_State):
    global user_id
    answer=state["ans"]
    if answer == "我确定":
        msg = "[CQ:at,qq=%s]"%(user_id) + high_medicine[ran.randint(0,13)]
        await high.send(Message(msg))
    else :
        await high.send("你是故意找茬的是吧？！")
@dangerous.handle()
async def danger_handle(bot: Bot, event: Event, state: T_State):
    await dangerous.send("谁？我要看看又有谁要有席了！！我要吃小孩那桌！！")



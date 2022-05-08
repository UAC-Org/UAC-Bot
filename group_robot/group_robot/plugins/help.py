from nonebot import on_command,on_keyword
from nonebot.rule import to_me,keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message
import random as ran
help_text='''目前可用功能:
1.实验室功能:@我并说"加入实验室"即可使用,@我并说“查询”可以知道自己加的仪器，回复“关"退出实验室"可退出，期间你不想被打扰的话，回复'禁止打扰'即可
2.与南舟白明对线（Pardon专用）功能:只要发“教训”即可~
3.升压药功能:注意请慎用！发“升压药”即可
4.招呼功能:@我并发“你好/早上好/晚上好/中午好”即可
5.反馈功能:@我并发“反馈-南舟”或“反馈-实验室”就会直接将你接下来的反馈给对应开发者~
6.相对分子质量计算（暂不能加前标）@我并在后面写上对应元素符号和下标（1不能省略）
7.涩图功能（珍爱你的群，慎用）：发送'se图'或'咳咳'即可使用（
8.掷骰子(不可私聊食用)：发rd/ROLL/掷骰,之后输入{x}d{y}代表你要掷出x个总点数为y的骰子
9.自动加一(不可私聊食用)：你可以试着发两遍同一内容
10.有机化学(正在开发)
11.自动（）()统计，@我并说查看即可查看你们已经发了多少括号力'''
helpp = on_command("帮助",rule=to_me(),priority = -10,block=True)
@helpp.handle()
async def help_handle(bot: Bot, event: Event, state:T_State):
    await helpp.send(help_text)

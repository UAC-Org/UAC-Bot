from nonebot import on_command,on_keyword
from nonebot.rule import to_me,keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message
biao = {"H": 1, "He": 4, "Li": 7, "Be": 9, "B": 11, "C": 12, "N": 14, "O": 16, "F": 19,
        "Ne": 20, "Na":23, "Mg": 24, "Al": 27, "Si": 28, "P": 31, "S": 32, "Cl": 35.5,
        "Ar": 40, "K": 39, "Ca": 40, "Sc": 45, "Ti": 48, "V": 51, "Cr": 52,
        "Mn": 55, "Fe": 56, "Co": 59, "Ni": 59, "Cu": 64, "Zn": 65, "Ga": 70,
        "Ge": 73, "As": 75, "Se": 79, "Br": 80, "Kr": 84}
clam = on_command("计算", rule = to_me(), priority = -10, block = True)
@clam.handle()
async def clam_hanlde(bot: Bot, event: Event, state: T_State):
    msg = str(event.get_message()).strip()
    if msg:
        state["ans"] = msg
@clam.got("ans",prompt = "请继续说出你要计算的相对分子质量")
async def clam_reply(bot: Bot, event: Event, state: T_State):
    global biao
    give=0
    LC = []
    Lint = []
    sint = ""
    a = state["ans"].split()
    for c in a:
        if c in biao.values():
            LC.append(c)
            Lint.appent(sint)
            sint = ""
        else:
            sint = sint + c
    Lint.append(sint)
    Lint.pop(0)
    for i in range(0, len(LC)):
        give += int(biao[LC[i]]) * int(Lint[i])
    await clam.send("计算结果:%s"%(give))

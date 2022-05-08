import json
import os
from threading import get_ident
from tokenize import group
from nonebot import on_notice,on_command,on_message
from nonebot.adapters import Bot
from nonebot.adapters.cqhttp import GroupIncreaseNoticeEvent, Message
from nonebot.adapters.cqhttp.event import GroupMessageEvent
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from random import randint, choice

grpdata = []
vrydata = {}
chars = []

async def verify():
    global chars
    width = 180
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype(r'simsun.ttc', 42)
    draw = ImageDraw.Draw(image)
    with open(os.path.abspath("chaeacters.txt")) as infile:
        contents = infile.read()
        for i in range(4):
            chars.append(choice(contents))
    for i in range(4):
        draw.text((40*i+10, 10), chars[i], font = font, fill = tuple([randint(0, 64) for i in range(3)]))
    boxes = [(40*i+10, 0, 40*i+50, 60) for i in range(4)]
    reverse_chars = [randint(0, 3) for i in range(2)]
    for i in range(4):
        region = image.crop(boxes[i])
        if i in reverse_chars:
            region = region.rotate(choice(range(170, 190)))
        else:
            region = region.rotate(choice(range(-20, 20)))
        image.paste(region, boxes[i])
    for x in range(width):
        for y in range(height):
            data = image.getpixel((x, y))
            if(data[0] | data[1] | data[2]) == 0 or data[0] == data[1] == data[2] == 255:
                draw.point((x, y), fill = tuple([randint(128, 255) for i in range(3)]))
    image.save('verify.jpg', 'jpeg')

async def die(bot: Bot, gid, uid):
    await bot.send_group_msg(message=Message(f"[CQ:at,qq={uid}]验证失败！"), group_id=gid)
    await bot.send_group_msg(message=Message("已移除群聊"), group_id = gid)
    #await bot.call_api("set_group_kick", group_id=gid, user_id=uid)

check = on_notice(priority = -100000, block = False)
_init = on_command("start verify", priority = 0, block = False)
_verify = on_message(priority = 0, block = False)
test = on_command("debug verify", priority = 0, block = False)

@test.handle()
async def _test(bot: Bot, event: GroupMessageEvent):
    await verify()
    imgcqcode = "[CQ:image,file=file://%s]" % (os.path.abspath("verify.jpg"))
    atcqcode = "[CQ:at,qq=%s]" % (event.user_id)
    msg = atcqcode + "\n[verify] DEBUG:\n" + imgcqcode
    await test.send(Message(msg))

@check.handle()
async def _(bot: Bot, event: GroupIncreaseNoticeEvent):
    await verify()
    imgcqcode = "[CQ:image,file=file://%s]" % (os.path.abspath("verify.jpg"))
    atcqcode = "[CQ:at,qq=%s]" % (event.user_id)
    msg = atcqcode + "您好,为了验证您是人,请您尽快输入验证码:\n" + imgcqcode
    await check.send(Message(msg))
@_init.handle()
async def initt(bot: Bot, event: GroupMessageEvent):
    global vrydata, grpdata
@_verify.handle()
async def verify_hook(bot: Bot, event: GroupMessageEvent):
    global vrydata, grpdata
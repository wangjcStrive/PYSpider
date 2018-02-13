# -*- coding: utf-8 -*-
# @Time    : 2/13/2018 2:35 PM
# @FileName: weChat.py
# Info: use WeChat

import itchat
from weather import get_weather_info


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])


itchat.auto_login(hotReload=True)

weather_info = get_weather_info('http://www.weather.com.cn/weather/101020100.shtml')


# auto reply when someone send you message
@itchat.msg_register(itchat.content.TEXT)
def simple_reply(msg):
    print(msg['FromUserName'])
    itchat.send_msg(weather_info, toUserName=msg['FromUserName'])


itchat.run()

# print(weather_info)
# print(itchat.get_friends())
# username = itchat.search_friend('文件传输助手')[0]['UserName']
# print(itchat.send(msg=weather_info, toUserName='夏日清晨'))
# print(itchat.search_friends(userName=msg['FromUserName']))

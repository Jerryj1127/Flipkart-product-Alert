#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("BOT STARTED")
import telegram
from requests import get
from re import search
from time import sleep


from flipkart import (
    token, 
    url, 
    tgm_userid, 
    sleep_time, 
    refresh_rate
)
print("sleep_time: {}, refresh_rate: {}".format(sleep_time, refresh_rate))

bot = telegram.Bot(token)
bot.sendMessage(chat_id= tgm_userid, text = "Bot Started for website: ".format(url))

def get_data():
    data = get(url)
    if 'NOTIFY ME' not in data.text:
        price = search('₹[0-9,]*', data.text).group()
        bot.sendMessage(chat_id= tgm_userid, text = "In stock, Price: {}".format(price))
        sleep(sleep_time)
    else:
        print('Out of stock')

while True:
    try:
        get_data()
        sleep(refresh_rate)
    except:
        sleep(refresh_rate*2)
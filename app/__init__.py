import logging
from telethon import TelegramClient
import telethon.tl.types
import time
import sqlite3

import config

channel_link=config.channel_link
message=config.message
phone_number=config.phone_number
API_ID=config.API_ID
API_HASH=config.API_HASH

menu_num_all={"1":"Собрать всех пользователей в текстовый файл из группы",
                "2":"Рассылка сообщения всем из открытой группы",
                "3":"Приглашать пользователей из открытой группы в другую открытую группу"}

class Bot(TelegramClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.me = None 

bot = Bot("testing", API_ID, API_HASH)
bot.parse_mode = 'HTML'
logging.basicConfig(level=logging.INFO)

import app.send_spam
import app.grep_users
import app.sqllite
import app.add_to_open_group_from_open_group

sqllite.run_bd()

banner="""
######################################################
##############TELEGRAM UTILS##########################
######################################################
"""
print(banner)

async def start():
    await bot.connect()
    if not await bot.is_user_authorized():
        await bot.send_code_request(phone_number)
        myself = await  bot.sign_in(phone_number, input('Enter code: '))

    menu_num=0
    while menu_num not in menu_num_all:
        msg_menu="\nМеню: \n"
        for i in menu_num_all:
            msg_menu=msg_menu + f"{i}. {menu_num_all[i]} \n"
        msg_menu=msg_menu + "Выберите нужный пункт.\n Мой выбор: "
        menu_num = input(msg_menu)

    if menu_num=="1":
        user_ignore=[]
        out_file=input("Введите название выходного файла: ")
        if out_file=="":
            out_file="users_grep.txt"
        user_list_sending = await grep_users.grep_user_group(channel_link,user_ignore,out_file)

    if menu_num=="2":
        user_ignore=[]
        user_list_sending = await grep_users.grep_user_group(channel_link,user_ignore)
        await send_spam.sending_spam(user_list_sending, message)
    
    if menu_num=="3":
        user_ignore=[]
        user_list_sending = await grep_users.grep_user_group(config.channel_invite_from,user_ignore)
        await add_to_open_group_from_open_group.invite_users(user_list_sending, config.channel_invite_to)
    print(len(user_list_sending))

def run():
    bot.loop.run_until_complete(start())



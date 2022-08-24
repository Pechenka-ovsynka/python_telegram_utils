from telethon import TelegramClient
import telethon.tl.types
import sqlite3
from  app.sqllite import is_send,sucs_bd
from app import bot
import time
import config

async def sending_spam(entity_list, message):
    for index, user in enumerate(entity_list):
        try:
            if is_send(user.id):
                print(f"Already sending to id:{user.id} username: {user.username}")
                continue
            else:
                print(f"Sending to id:{user.id} username: {user.username}")
                await bot.send_message(user, message)
                sucs_bd(user.id)
            if index%config.spam_users_one_time==0:
                time.sleep(config.spam_users_delay)
        except Exception as e:
            with open("log_error.txt","ab") as d:
                d.write(f"Error {e}! {user}\n".encode())
            print(f"Error {e}! {user}\n")
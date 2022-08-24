from telethon import TelegramClient
import telethon.tl.types
from app import bot
from app.sqllite import insert_bd
import time

async def grep_user_group(channel_link, user_ignore, out_file="", add_bd_spam=1):
    user_list_sending=[]
    channel = await bot.get_entity(channel_link)
    i=0

    async for user in bot.iter_participants(channel):
        if out_file !="":
            with open(out_file,"ab") as f:
                f.write(f"{user}\n".encode())
        if user.username in user_ignore:
            continue
        if i%100==0:
            time.sleep(2)
            print(f"Grep {i} users")

        user_list_sending.append(user)
        if add_bd_spam:    
            insert_bd(user.id)
        i+=1
    return user_list_sending
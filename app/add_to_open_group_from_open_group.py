from app import bot
import time
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
import telethon
import config

async def invite_users(users,channel):
    for user in users:
        try:
            await bot(telethon.tl.functions.channels.InviteToChannelRequest(channel,[user]))
            print("Waiting 60 Seconds...")
            time.sleep(config.invite_delay)
        except PeerFloodError:
            print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        except UserPrivacyRestrictedError:
            print("The user's privacy settings do not allow you to do this. Skipping.")
        except Exception as e:
            print(f"Error {e}")

import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e485a1d51cf862ce6dfe6.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
Hello, I am video chat song player
┏━━━━━━━━━━━━━━━━━┓
‎┣★القناة : [MAH BOT UPDATES](https://t.me/PP77Y)
‎┣★قروبنا: [Tamil Chatting Group | Tamil Friendship Group](https://t.me/TTET6)
┣★𝗢𝘄𝗻𝗲𝗿 : [𓆩˹𝒌𝒏𝒈˼𓆪ツمسطول](https://t.me/N_4_8)
┗━━━━━━━━━━━━━━━━━┛
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
‎                        "⚡ ❰عليك فقط اضافتي في المجموعة او الشات🤍 ❱ ⚡", url=f"https://t.me/TTET6")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "Sumit"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a1ee9df1df15bf2e183cc.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
‎                        "⚡قروبنا⚡", url=f"https://t.me/TTET6")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["Angel", "Group", "@Channel", "/Channel", "Channel"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e485a1d51cf862ce6dfe6.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
‎                        "⚡القناة⚡", url=f"https://t.me/PP77Y")
                ]
                
            ]
        ),
    )

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>โจ Welcome</b> {message.from_user.mention}!\n\n๐ญ [PRINCE MUSIC](t.me/PRINCEBOTS) <b>allows you to play music on groups through the new Telegram's voice chats!</b>\n\n๐ก <b>Find out</b> all the <b>Bot</b>'s <b>commands</b> and how they <b>work</b> by clicking on the ยป ๐ <b>Commands</b> button!""",
        reply_markup=InlineKeyboardMarkup(
           [ 
                 [
                    InlineKeyboardButton(
                        "๐ผ Join My Music Group ๐ง", url=f"https://t.me/hindi_music_chat")
                ],[
                    InlineKeyboardButton(
                         "๐ Commands", url=f"https://t.me/PRINCEBOTS/4"
                    ),
                    InlineKeyboardButton(
                        "๐ Donate", url=f"https://t.me/DEVILDAD_PRINCE")
                ],[
                    InlineKeyboardButton(
                        "๐ฅ Official Group", url=f"https://t.me/PRINCEBOTSUPPORT"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ Official Channel", url=f"https://t.me/PRINCEBOTS")
                ],[
                    InlineKeyboardButton(
                        "โ How to use Me", url=f"https://t.me/PRINCEBOTS/4")
                ],[
                    InlineKeyboardButton(
                        "๐งช Source Code ๐งช", url="https://t.me/PRINCEBOTS"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""__**BOT WORKING FROM 21-SEP**__""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ท๏ธ UPDATE CHANNEL ๐ท๏ธ", url="https://t.me/PRINCEBOTS")
                ]
            ]
        )
   )



from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>┏━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┓\n× ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/ElitesCrewBot'>Eʟɪᴛᴇs ᴀᴅᴍɪɴs</a>\n× ʜᴇɴᴛᴀɪ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/+befOBiGrQ7Y2ZGE9'>ʜᴇᴀɴɪᴍᴇ ʜᴜʙ</a>\n× ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/anime_elites'>ᴀɴɪᴍᴇ ᴇʟɪᴛᴇs</a>\n× ʙᴏᴛs ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/elites_bots'>ᴇʟɪᴛᴇs ʙᴏᴛᴢ</a>\n× sᴇʀɪᴇs ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/+78IZqN1ZqP0zMThl'>sᴇʀɪᴇs ᴇʟɪᴛᴇs</a>\n┗━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┛</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("☠️ ᴄʟᴏꜱᴇ ☠️", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

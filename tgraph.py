import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file

tgraph = Client(
    "TELEGRAPH BOT",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """ Hai {} š¤, 
Am a Simple telegraph uploader bot I can upload images, videos and gif under 5Mb to [Telegra.ph]
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('SOURCE CODE', url="https://github.com/MR-JINN-OF-TG/TGRAPHBOT")
        ]]
    )

@tgraph.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.first_name),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )

@tgraph.on_message(filters.media)
async def media(client, message):
    msg = await message.reply_text("šššš š šššššš š“ ššššššššš šš ššššššššš.........")
    download_location = await client.download_media(
        message=message, file_name='root/tg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("šššš šš ššš ššššš šššššš šš šššš šššš 5 šš.") 
    else:
        await msg.edit_text(f'**šššššššš šš ššššššššš!\n\nš https://telegra.ph{response[0]}\n\nšš telegra.ph**',
            disable_web_page_preview=True,
        )        

print(
    """
TELEGRAPH BOT DEPLOYED SUCCESSFULLY 
JOIN @NAZRIYASUPPORT
"""
)

tgraph.run()        

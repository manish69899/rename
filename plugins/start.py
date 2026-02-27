from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start"))
async def start_handler(client, message):
    txt = (
        "👋 **Hello! Main Advanced Renamer Bot hoon.**\n\n"
        "Main Bulk me files rename kar sakta hoon.\n"
        "1. Files Bhejo\n"
        "2. Mode Select Karo\n"
        "3. Rename Start!\n\n"
        "👇 **Files bhejna shuru karein!**"
    )
    # Koi button chahiye toh yahan add karein
    await message.reply(txt)
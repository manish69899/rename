from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import get_data  # Database import kiya

@Client.on_message(filters.document | filters.video | filters.audio)
async def cache_files(client, message):
    user_id = message.from_user.id
    data = get_data(user_id)
    
    # Agar user abhi processing kar raha hai, toh nayi file mat lo
    if data['step'] == 'processing':
        await message.reply("⚠️ Ruk jao! Abhi purana kaam chal raha hai.")
        return

    # 1. File Database me daalo
    data['files'].append(message)
    data['step'] = 'collecting'
    
    total = len(data['files'])
    
    # 2. Control Panel (Buttons)
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"✅ DONE ({total} Files)", callback_data="done")],
        [InlineKeyboardButton("❌ Reset / Cancel", callback_data="cancel")]
    ])
    
    await message.reply_text(
        f"📂 **File Saved!**\nTotal: `{total}`\n\n"
        "Jab saari files bhej do, tab **DONE** dabana.",
        reply_markup=buttons,
        quote=True
    )
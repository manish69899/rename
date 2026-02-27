from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import get_data, clear_data

@Client.on_callback_query()
async def callback_handler(client, query):
    data = query.data
    user_id = query.from_user.id
    user_data = get_data(user_id)
    
    # --- CANCEL ---
    if data == "cancel":
        clear_data(user_id)
        await query.message.edit("❌ **Task Cancelled.** Files list clear kar di gayi.")
        return

    # --- DONE CLICKED -> SHOW MODES ---
    if data == "done":
        if not user_data['files']:
            await query.answer("Empty List!", show_alert=True)
            return
            
        user_data['step'] = 'selecting_mode'
        
        btns = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Start (Prefix)", callback_data="set_start"),
                InlineKeyboardButton("End (Suffix)", callback_data="set_end")
            ]
        ])
        await query.message.edit(
            "⚙️ **Configuration**\n\nText kahan add karna hai?",
            reply_markup=btns
        )
        return

    # --- MODE SELECTED -> ASK TEXT ---
    if data in ["set_start", "set_end"]:
        mode = "start" if data == "set_start" else "end"
        user_data['mode'] = mode
        user_data['step'] = 'waiting_for_text'
        
        display_mode = "SHURU (Start)" if mode == "start" else "AAKHIR (End)"
        
        await query.message.edit(
            f"👍 Mode: **{display_mode}**\n\n"
            "✍️ Ab wo **TEXT** bhejo jo file me add karna hai.\n"
            "Example: `[Dual Audio]`"
        )
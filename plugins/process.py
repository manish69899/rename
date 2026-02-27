import os
import time
from pyrogram import Client, filters
from config import Config
from database import get_data, clear_data
from utils import progress_bar, human_readable_time

@Client.on_message(filters.text & filters.private)
async def renaming_engine(client, message):
    user_id = message.from_user.id
    data = get_data(user_id)
    
    # Check: Kya bot text ka wait kar raha hai?
    if data['step'] != 'waiting_for_text':
        return

    # --- 1. CLEAN CUSTOM TEXT (Space -> Underscore) ---
    raw_text = message.text
    # "Dual Audio" -> "Dual_Audio"
    custom_text = raw_text.replace(" ", "_")
    
    files = data['files']
    mode = data['mode']
    
    # Status Message
    status_msg = await message.reply(f"🚀 **Premium Rename Started...**\nStyle: `⟪_{custom_text}_⟫__File_Name`")
    
    start_time = time.time()
    total_files = len(files)
    success = 0
    
    for i, file_msg in enumerate(files, start=1):
        try:
            # --- Progress Bar Logic ---
            elapsed = time.time() - start_time
            if i > 1:
                avg_time = elapsed / (i-1)
                eta = (total_files - i + 1) * avg_time
            else:
                eta = 0
            
            bar = progress_bar(i-1, total_files)
            await status_msg.edit(
                f"⚡ **Renaming...**\n{bar}\n\n"
                f"📂 File: `{i}/{total_files}`\n"
                f"⏳ ETA: `{human_readable_time(eta)}`"
            )

            # --- File Details ---
            media = file_msg.document or file_msg.video or file_msg.audio
            original_name = media.file_name or "Unknown_File"
            
            # --- 2. CLEAN ORIGINAL NAME (Space -> Underscore) ---
            name_part, ext_part = os.path.splitext(original_name)
            # "Avengers Endgame" -> "Avengers_Endgame"
            clean_name = name_part.replace(" ", "_")
            
            # --- 3. PREMIUM FORMATTING LOGIC ---
            if mode == "start":
                # Format: ⟪_Text_⟫__Name.mkv
                new_name = f"⟪_{custom_text}_⟫__{clean_name}{ext_part}"
            else:
                # Format: Name__⟪_Text_⟫.mkv
                new_name = f"{clean_name}__⟪_{custom_text}_⟫{ext_part}"
            
            # Paths set karna
            dl_path = f"{Config.DOWNLOAD_PATH}/{original_name}"
            new_path = f"{Config.DOWNLOAD_PATH}/{new_name}"
            
            # --- Download -> Rename -> Upload ---
            await client.download_media(file_msg, file_name=dl_path)
            
            if os.path.exists(dl_path):
                os.rename(dl_path, new_path)
            
            await client.send_document(
                chat_id=user_id,
                document=new_path,
                caption=f"✅ `{new_name}`",
                force_document=True
            )
            
            # Cleanup
            if os.path.exists(new_path):
                os.remove(new_path)
            success += 1
            
        except Exception as e:
            print(f"Error on file {i}: {e}")
            continue 
    
    # Final Done Message
    clear_data(user_id)
    duration = human_readable_time(time.time() - start_time)
    await status_msg.edit(
        f"💎 **Premium Task Complete!**\n\n"
        f"✅ Total Files: `{success}`\n"
        f"⏱ Time Taken: `{duration}`"
    )
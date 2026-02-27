import asyncio  # Nayi line: asyncio import karein
from pyrogram import Client
from config import Config
from keep_alive import keep_alive

if __name__ == "__main__":
    # Render ke liye dummy web server background me start karna
    keep_alive()
    
    # Ye do lines ERROR FIX karne ke liye hain:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    # Plugins dictionary use karke hum folder bata rahe hain
    app = Client(
        "ModularRenamer",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins=dict(root="plugins") 
    )
    
    print("✅ Bot Successfully Started!")
    print("Files bhejna shuru kar sakte hain.")
    app.run()
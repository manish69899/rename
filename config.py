import os
from dotenv import load_dotenv

# Ye line local me .env file ko load karegi
load_dotenv()

class Config:
    # os.environ.get() se hum .env ya Render se data fetch karte hain
    # API_ID integer (number) hota hai, isliye int() lagana zaroori hai
    API_ID = int(os.environ.get("API_ID", 0))  
    API_HASH = os.environ.get("API_HASH", "")
    
    # BotFather se milega
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    
    # Files yahan save hongi
    DOWNLOAD_PATH = "./downloads/"
    
    # Folder bana lo agar nahi hai
    if not os.path.exists(DOWNLOAD_PATH):
        os.makedirs(DOWNLOAD_PATH)
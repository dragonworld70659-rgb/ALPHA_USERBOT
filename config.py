import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "27079591")) #optional
API_HASH = getenv("API_HASH", "c81ae4c3dc026ea4bf49842a8ce4a5f9") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7403621976").split()))
OWNER_ID = int(getenv("OWNER_ID",'https://t.me/sexyspectorr')
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://files.catbox.moe/4b14yr.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT,|────────────────────|
| '⚡ ʜᴇʏ, ɪ ᴀᴍ : ˹ 𝐔sᴇʀʙᴏᴛ 𝐇ᴏsᴛᴇʀ ˼
| ⚙️ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴɪᴍᴀᴛɪᴏɴ + ғᴜɴ ᴛᴏᴏʟs
| 🔐 ғᴀsᴛ • sᴇᴄᴜʀᴇ • ᴍᴏᴅᴜʟᴀʀ
|────────────────────|

| ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ: Click Tips
| ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ: @AnanyaSessionBot
|────────────────────|
| ᴄʟᴏɴᴇ ʙᴏᴛ ɪɴ 2 sᴇᴄᴏɴᴅs:
| /clone session_string
| ʀᴇᴍᴏᴠᴇ ᴄʟᴏɴᴇ:
| /delclone session_string
| /logout session_string
|────────────────────|
| ᴘᴏᴡᴇʀᴇᴅ ʙʏ: ˹Sona Bots˼
|────────────────────|')
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/TEAMPURVI/ALPHA_USERBOT")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")

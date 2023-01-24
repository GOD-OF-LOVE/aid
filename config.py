import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "9181844")) #optional
API_HASH = getenv("API_HASH", "996a3e7194a4f07576fda5c20bb1138b") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5630946962").split()))
OWNER_ID = int(getenv("OWNER_ID", "5354500761"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://karthika:karthika@cluster0.6jms6m3.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5941662739:AAEQ56IVr9aOCrApC1VwwqPGfkzTqX5a1-k")
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/3870413e25d66bbfacf43.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT", "Im Alone x UserBot")
PM_LOGGER = getenv("PM_LOGGER", "-1001522073183")
LOG_GROUP = getenv("LOG_GROUP", "-1001888105987")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQCIdNZn_qW4d87yyrzQRKsj1dNmtuPZ4KoSICNdmBwysBmKXd_SFwJRfO7WGZNhoPfHZ8anNNaOf75HYc7TkNrXJbKJS_1GEO6KkV2atW6yeedPK4oh8X3rbKNK-HsQwmSrW1Xl1qlOql1JoL3anGIEmIBABfw9obQFKMbzR8m_w3kWPD0DSg8ZdC5bkWv74avpyj7HBa-t4SWEEFRKrmkPFonwmHWRFzZ3a_XSjrtLyb_KpeAluggOSiChJFS86YO-yyUnX8NLP0EWn7Ahj_a2GxM9eahU5RwC4a_FK3ctItVKDZ6dqMLje8URa-h_OHtiw2hYfZbxzpsG0AJVu3eFAAAAAVRJn-EA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")

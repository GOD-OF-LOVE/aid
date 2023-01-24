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
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBLzCsQfg7DUMIwN5oBUo8B0atCJVdJRrI1zTJV-9_XvAkoId6iQXQ2wgXrFxIy_56yiYkE8jKMB7BGsZkW_nLUTY6uXOSnmazUWLElX1Hb6AnE7rjAxImOxvEVYGcySURLvkiAusaVcjJh_6-Gh7tkI1esOXX_zOnBKkEOvUkSU0d2x35NMXDVfxoIr4M2QowXVfDwc-WKHGSasNPOEBvfKW3NMJ1uZ4P1ZgR933MbIWGnxEsiw9I8d9a9NADVdyPZ1jZft0SqMPU6D36ET8CZDv-WKhuj0_xhqmOHgj06jOLY2NaWAmY989tkvfQnJTnJqG0N63NH7Zbh7sxfXd7MAAAAAVRJn-EA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")

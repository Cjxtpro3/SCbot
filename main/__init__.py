from pyrogram import Client
from telethon.sync import TelegramClient
import logging
import sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 22589525
API_HASH = "2dd2931e17ae61c8680b6cdb6a9edc74"
BOT_TOKEN = "6255680130:AAFWAj9QPUNAqDL5G0s3GLap4b3BUkNs45U"
SESSION = "BQFYsFUAlfvTHAZNW4YLcd9XJpYWfFjHzbJ9-ncMAWjGeMEzWLaR7t3XUq9U2acOojxF5txlS-KW-rgw-HYbTGt2HYCzlGGIESrHR2Qf9TSs4VaO97Ch_ko93eGjAWy8z7ImMNbAAp_p6O9mtY-ZNheExxyHNeusKEmWlZd6zVeR-C65VCy-l-YvndM7fabHYQHyq0dLfsiGbnIR3BoVSElS-FxfHklMkl5CCh2QXiwCRL3Cz7V53gA1lH7yq_2otlNzDJlOooDu28RxbnM18Kp94En_ICPqXFm_p7-dz3vsR7_pvYiWpuKtvvLryDP5gNHxbsvKt6XqGkL83SSDyQTNyLE4dQAAAAAjYvVVAA"
FORCESUB = "Allbothub"
AUTH = 593687893

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

userbot = Client("saverestricted", api_hash=API_HASH, api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)

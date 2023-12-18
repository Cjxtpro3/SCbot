from pyrogram import Client
from telethon.sync import TelegramClient
import logging
import sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 23147177
API_HASH = "6c1b34bf3c56b9957aab7da8a0dd3482"
BOT_TOKEN = "6488628610:AAFzXVYuoOalTxDxUbaawSggSKgF66Z9EYU"
SESSION = "BQFhMqkADUARAwlM9CHEyqzhtsXv5At9utM3bgHG8QdxAhzY4qOBDj45NgwxW4obAuOQoI65yskOmXq4xj2eoyxmR3t6sDTvFQptbEMKhnvmk28-YfvOAYGIer5iRd7B-w07JXsdFn2glugYUZzEMES36hLyPRLBSllru4__1uSHIiVYO6AqheNFgVpbyl-vm3HSZNBwXdIEWN8puOAghtN1jpJpwUdabfgInJcHaHWblCXPRd2-pPE6niSGpYIfdKHCpNPrxVh7plWRAyHEkSuskApJHCDQRBVP4AY1Tq6iCQaZ75UDOFHUJJgfBJaVKvhZHjvFmxpRfXPbH8Yx_SPEYQjeOgAAAAGNRBjKAA"
FORCESUB = "Botlgod"
AUTH = 6665017546

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

userbot = Client("saverestricted", api_hash=API_HASH, api_id=API_ID)

try:
    userbot.start "6488628610:AAFzXVYuoOalTxDxUbaawSggSKgF66Z9EYU"
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

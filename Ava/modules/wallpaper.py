import random
from random import randint
import requests
from pyrogram import enums
from pyrogram.types import Message

from Ava import Jarvis

UNSPLASH_ACCESS_KEY = "UwPT7-Of5XQgwxHx-GfcXa4sK0O_38Pbi-6FrQ5f7AY"

@Jarvis.on_cmd(["wallpaper"])
async def wallpaper(_, msg):
    if len(msg.command) < 2:
        await msg.reply_text("ʜᴇʏ ʙᴀʙʏ ɢɪᴠᴇ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ sᴇᴀʀᴄʜ.")
        return
    query = (
        msg.text.split(None, 1)[1]
        if len(msg.command) < 3
        else msg.text.split(None, 1)[1].replace(" ", "%20")
    )

    if not query:
        await msg.reply_text("ʜᴇʏ ʙᴀʙʏ ɢɪᴠᴇ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ sᴇᴀʀᴄʜ.")
        return

    url = f"https://api.unsplash.com/search/photos?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
    re = requests.get(url).json()
    walls = re.get("results")
    if not walls:
        await msg.reply_text("ɴᴏ ʀᴇsᴜʟᴛs ғᴏᴜɴᴅ!")
        return
    wall_index = randint(0, len(walls) - 1)
    wallpaper = walls[wall_index]
    wallpaper_url = wallpaper.get("urls").get("regular")  # Use 'regular' or 'full' for better quality
    preview = wallpaper.get("urls").get("regular")  # Using 'regular' for both display and preview
    title = wallpaper.get("description") or "No Title"
    
    try:
        await Jarvis.send_chat_action(msg.chat.id, enums.ChatAction.UPLOAD_PHOTO)
        await msg.reply_photo(
            preview, caption=f"🔎 ᴛɪᴛʟᴇ - {title}\nᴊᴏɪɴ [Support](t.me/CertifiedCoders)"
        )
    except Exception as error:
        await msg.reply_text(f"ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀᴇᴅ.\n {error}")


@Jarvis.on_cmd("wall")
async def wall(_, m: Message):
    if len(m.command) < 2:
        return await m.reply_text("ɢɪᴠᴇ ᴍᴇ ᴀ ᴛᴇxᴛ!")
    search = m.text.split(None, 1)[1]
    
    url = f"https://api.unsplash.com/search/photos?query={search}&client_id={UNSPLASH_ACCESS_KEY}"
    re = requests.get(url).json()
    walls = re.get("results")
    
    if not walls:
        await m.reply_text("ɴᴏ ʀᴇsᴜʟᴛs ғᴏᴜɴᴅ!")
        return

    wallpaper_url = random.choice(walls).get("urls").get("regular")  # Use 'regular' or 'full' for better quality
    
    await m.reply_photo(wallpaper_url)

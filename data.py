from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("⛈️ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ⛈️", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("🕸️sᴛʀᴀɴɢᴇʀ ᴜsᴇʀʙᴏᴛ 🕸️", url="https://t.me/Shukla_op_clone1bot")],
        [
            InlineKeyboardButton("❔ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ 🎶", callback_data="about")
        ],
        [
        
            InlineKeyboardButton("⚡ ᴜᴘᴅᴀᴛᴇ's ", url="https://t.me/StrangerAssociation"),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ⛈️️", url="https://t.me/MASTIWITHFRIENDSXD")
      
        ],
        [InlineKeyboardButton("🌿 ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ ᴀɴᴅ ᴍᴏʀᴇ ʙᴏᴛꜱ 🌿", url="https://t.me/StrangerAssociation")],
    ]

    START = """
**┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ⏤͟͟͞͞‌‌‌‌★
┆◍ нᴇʏ {}
┆● ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ ! 
└─────────────────────────•
❖ ɪ ᴀᴍ ᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴇ ʙᴏᴛ
❖ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 
❖ sᴜᴘᴘᴏʀᴛ - ᴘʏʀᴏɢʀᴀᴍ | ᴛᴇʟᴇᴛʜᴏɴ
•─────────────────────────•
❖ ʙʏ : [sᴛʀᴀɴɢᴇʀ ᴀssᴏᴄɪᴀᴛɪᴏɴ](https://t.me/StrangerAssociation) 🚩**
    """

    HELP = """
**ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ** ⚡

/start - ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
/help - ᴏᴘɴᴇʀ ʜᴇʟᴘ ᴍᴇɴᴜ
/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ᴏᴡʀ
/generate - ɢᴇɴᴇʀᴀᴛᴇ ᴛʜᴇ ꜱᴇꜱꜱɪᴏɴ
/cancel - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴀʟʟ ᴘʀᴏᴄᴇꜱꜱ
/restart - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴀʟʟ ᴘʀᴏᴄᴇꜱꜱ
"""

    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜɪꜱ ʙᴏᴛ** 🌙

ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ
ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ʙʏ [sᴛʀᴀɴɢᴇʀ ᴀssᴏᴄɪᴀᴛɪᴏɴ](https://t.me/StrangerAssociation)

◌ ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](https://www.python.org)

◌ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [sʜɪᴠᴀɴsʜ-xᴅ](https://t.me/SHIVANSH474)

◌ ᴅᴇᴠᴇʟᴏᴘᴇʀ : [sʜɪᴠᴀɴsʜ](https://t.me/SHIVANSHDEVS)
    """

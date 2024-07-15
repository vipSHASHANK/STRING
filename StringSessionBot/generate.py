from telethon import TelegramClient
from pyrogram.types import Message
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)

from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

from data import Data


ask_ques = "❖ ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴀ ᴏᴘᴛɪᴏɴ "
buttons_ques = [
    [
        InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ", callback_data="pyrogram"),
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ ʙᴏᴛ", callback_data="pyrogram_bot"),
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ ʙᴏᴛ", callback_data="telethon_bot"),
    ],
]


@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, is_bot: bool = False):
    if telethon:
        ty = "ᴛᴇʟᴇᴛʜᴏɴ"
    else:
        ty = "ᴘʏʀᴏɢʀᴀᴍ ᴠ2"
    if is_bot:
        ty += " ʙᴏᴛ"
    await msg.reply(f"❖ ꜱᴛᴀʀᴛɪɴɢ . . . {ty} ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛɪᴏɴ . . .")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, '❖ ᴄᴏᴘʏ ᴀɴᴅ sᴇɴᴅ ᴛʜɪs ᴀᴘɪ ɪᴅ \n\n❖ API_ID : `28795512`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('❖ ɴᴏᴛ ᴀ ᴠᴀʟɪᴅ ᴀᴘɪ_ɪᴅ (ᴡʜɪᴄʜ ᴍᴜꜱᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ). \n↻ ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀɢᴀɪɴ.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, '❖ ᴄᴏᴘʏ ᴀɴᴅ sᴇɴᴅ ᴛʜɪs ᴀᴘɪ ʜᴀsʜ\n\n❖ API_HASH : `c17e4eb6d994c9892b8a8b6bfea4042a`', filters=filters.text)
    if await cancelled(api_hash_msg):
        return
    api_hash = api_hash_msg.text
    if not is_bot:
        t = "❖ ɴᴏᴡ ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ʏᴏᴜʀ `PHONE_NUMBER` ᴀʟᴏɴɢ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴜɴᴛʀʏ ᴄᴏᴅᴇ. \n❖ ᴇxᴀᴍᴘʟᴇ : `+910000000000`'"
    else:
        t = "❖ ɴᴏᴡ ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ʏᴏᴜʀ `BOT_TOKEN` \n❖ ᴇxᴀᴍᴘʟᴇ : `12345:abcdefghijklmnopqrstuvwxyz`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("❖ ꜱᴇɴᴅɪɴɢ ᴏᴛᴘ...")
    else:
        await msg.reply("❖ ʟᴏɢɢɪɴɢ ᴀꜱ ʙᴏᴛ ᴜꜱᴇʀ...")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name=f"bot_{user_id}", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    else:
        client = Client(name=f"user_{user_id}", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply('❖ `API_ID` ᴀɴᴅ `API_HASH` ᴄᴏᴍʙɪɴᴀᴛɪᴏɴ ɪꜱ ɪɴᴠᴀʟɪᴅ. ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀɢᴀɪɴ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply('❖ `PHONE_NUMBER` ɪꜱ ɪɴᴠᴀʟɪᴅ. ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀɢᴀɪɴ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "❖ ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ꜰᴏʀ ᴀɴ ᴏᴛᴘ ɪɴ ᴏꜰꜰɪᴄɪᴀʟ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ɪꜰ ʏᴏᴜ ɢᴏᴛ ɪᴛ, ꜱᴇɴᴅ ᴏᴛᴘ ʜᴇʀᴇ ᴀꜰᴛᴇʀ ʀᴇᴀᴅɪɴɢ ᴛʜᴇ ʙᴇʟᴏᴡ ꜰᴏʀᴍᴀᴛ. \n\n❖ ɪꜰ ᴏᴛᴘ ɪꜱ `12345`, **ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ɪᴛ ᴀꜱ** `1 2 3 4 5`", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply('❖ ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏꜰ 10 ᴍɪɴᴜᴛᴇꜱ. ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀɢᴀɪɴ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError):
            await msg.reply('❖ ᴏᴛᴘ ɪꜱ ɪɴᴠᴀʟɪᴅ. ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀɢᴀɪɴ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError):
            await msg.reply('❖ ᴏᴛᴘ ɪꜱ ɪɴᴠᴀʟɪᴅ. ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀɢᴀɪɴ', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError):
            try:
                two_step_msg = await bot.ask(user_id, '❖ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʜᴀꜱ ᴇɴᴀʙʟᴇᴅ ᴛᴡᴏ-ꜱᴛᴇᴘ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ. ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇ ᴘᴀꜱꜱᴡᴏʀᴅ.', filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply('❖ ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏꜰ 5 ᴍɪɴᴜᴛᴇꜱ. ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀɢᴀɪɴ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError):
                await two_step_msg.reply('❖ ɪɴᴠᴀʟɪᴅ ᴘᴀꜱꜱᴡᴏʀᴅ ᴘʀᴏᴠɪᴅᴇᴅ. ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀɢᴀɪɴ.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"❖ **{ty.upper()} ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ** \n\n`{string_session}` \n\n❖ GENERATED BY : @SESSIONxGENxBOT"
    try:
        if not is_bot:
            await bot.send_message(msg.chat.id, text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "❖ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ {} ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ. \n\nʙʏ @SESSIONxGENxBOT".format("telethon" if telethon else "pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("❖ ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴘʀᴏᴄᴇꜱꜱ!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("❖ ʀᴇꜱᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("❖ ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴘʀᴏᴄᴇꜱꜱ!", quote=True)
        return True
    else:
        return False

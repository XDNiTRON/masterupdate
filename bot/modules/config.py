# Implement By https://github.com/jusidama18
# Based on this https://github.com/DevsExpo/FridayUserbot/blob/master/plugins/heroku_helpers.py

from pyrogram import filters, types, emoji
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot import app, OWNER_ID
from bot.helper import get_text, check_heroku
from bot import *

# Add Variable

@app.on_message(filters.command('setvar') & filters.user(OWNER_ID))
@check_heroku
async def set_varr(client, message, app_):
    msg_ = await message.reply_text("`Please Wait!`")
    heroku_var = app_.config()
    _var = get_text(message)
    if not _var:
        await msg_.edit("`Here is Usage Syntax: /setvar KEY VALUE`", parse_mode="markdown")
        return
    if not " " in _var:
        await msg_.edit("`Variable VALUE needed !`", parse_mode="markdown")
        return
    var_ = _var.split(" ", 1)
    if len(var_) > 2:
        await msg_.edit("`Here is Usage Syntax: /setvar KEY VALUE`", parse_mode="markdown")
        return
    _varname, _varvalue = var_
    await msg_.edit(f"`Variable {_varname} Added With Value {_varvalue}!`")
    heroku_var[_varname] = _varvalue

# Delete Variable
        
@app.on_message(filters.command('delvar') & filters.user(OWNER_ID))
@check_heroku
async def del_varr(client, message, app_):
    msg_ = await message.reply_text("`Please Wait!`", parse_mode="markdown")
    heroku_var = app_.config()
    _var = get_text(message)
    if not _var:
        await msg_.edit("`Give Var Name As Input!`", parse_mode="markdown")
        return
    if not _var in heroku_var:
        await msg_.edit("`This Var Doesn't Exists!`", parse_mode="markdown")
        return
    await msg_.edit(f"`Sucessfully Deleted {_var} Var!`", parse_mode="markdown")
    del heroku_var[_var]

# CONFIG LIST #

__header__='📕 **PAGE ➤** **{}**\n\n'

@app.on_message(filters.command(BotCommands.ConfigMenuCommand) & filters.user(OWNER_ID))
async def config_menu(_, message):
    await message.reply(
        f"**Hello {message.from_user.mention} 👋**,\n\n**If you want to add or set Variable in Heroku use** `/setvar`\n\n**If you want to delete Variable in Heroku use `/delvar`**\n\n**❗WARNING❗ Very Recommended to do this command in private since it's contain bot info.**\n\n**Here's This is ANonYmoUSFriEND Current Configs**",
        reply_markup=types.InlineKeyboardMarkup(
            [[types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'), types.InlineKeyboardButton(f"BOT CONFIG", callback_data='docs_1')]]
        )
    )

@app.on_callback_query(filters.regex('^docs_') & filters.user(OWNER_ID))
async def config_button(_, query):
    data = query.data.split('_')[1]
    if data == '1':
        return await query.message.edit(
            __header__.format(data)
            + f"**꧁  TELEGRAM CONFIG  ꧂**\n\n\n**➣ BotToken:** `{BOT_TOKEN}`\n\n**➣ TelegramAPI:** `{TELEGRAM_API}`\n\n**➣ TelegramHASH:** `{TELEGRAM_HASH}`\n\n**➣ TelegraphToken:** `{telegraph_token}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_9'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_2')
                    ]
                ]
            )
        )
    elif data == '2':
        return await query.message.edit(
            __header__.format(data)
            + f"**꧁ DRIVE AND INDEX CONFIG ꧂**\n\n\n**➣ DriveFolder:** `{parent_id}`\n\n**➣ UsingTeamDrive:** `{IS_TEAM_DRIVE}`\n\n**➣ UsingServiceAccount:** `{USE_SERVICE_ACCOUNTS}`\n\n**➣ IndexURL:** `{INDEX_URL}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_1'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_3')
                    ]
                ]
            )
        )
    elif data == '3':
        return await query.message.edit(
            __header__.format(data)
            + f"**꧁ MEGA AND UPTOBOX CONFIG ꧂**\n\n\n**➣ MegaAPI:** `{MEGA_API_KEY}`\n\n**➣ MegaEmail:** `{MEGA_EMAIL_ID}`\n\n**➣ MegaPassword:** `{MEGA_PASSWORD}`\n\n**➣ UptoboxToken:** `{UPTOBOX_TOKEN}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_2'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_4')
                    ]
                ]
            )
        )
    elif data == '4':
        return await query.message.edit(
            __header__.format(data)
            + f"**꧁ STOP DUPLICATE CONFIG ꧂**\n\n\n**➣ Mirror:** `{STOP_DUPLICATE_MIRROR}`\n\n**➣ Clone:** `{STOP_DUPLICATE_CLONE}`\n\n**➣ Mega:** `{STOP_DUPLICATE_MEGA}`\n\n**꧁ BLOCK MEGA CONFIG ꧂**\n\n\n**➣ Folder:** `{BLOCK_MEGA_FOLDER}`\n\n**➣ Link:** `{BLOCK_MEGA_LINKS}`\n\n",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_3'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_5')
                    ]
                ]
            )
        )
    elif data == '5':
        return await query.message.edit(
            __header__.format(data)
            + f"**꧁ LIMIT SIZE CONFIG ꧂**\n\n\n**➣ TorrentAndDirect:** `{TORRENT_DIRECT_LIMIT}`\n\n**➣ Clone:** `{CLONE_LIMIT}`\n\n**➣ Mega:** `{MEGA_LIMIT}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_4'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_6')
                    ]
                ]
            )
        )
    elif data == '6':
        user = sudo = ''
        user += '\n'.join(str(id) for id in AUTHORIZED_CHATS)
        sudo += '\n'.join(str(id) for id in SUDO_USERS)
        return await query.message.edit(
            __header__.format(data)
            + f"**꧁ USER ID CONFIG ꧂**\n\n\n**➣ OwnerID:** `{OWNER_ID}`\n\n**➣ AuthorizedChat:**\n`{user}`\n\n**➣ SudoUsers:**\n`{sudo}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_5'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_7')
                    ]
                ]
            )
        )
    elif data == '7':
        return await query.message.edit(
            __header__.format(data)
            + f"**꧁ BUTTON CONFIG ꧂**\n\n\n**➣ ButtonFourName:** `{BUTTON_FOUR_NAME}`\n\n**➣ ButtonFourURL:** `{BUTTON_FOUR_URL}`\n\n**➣ ButtonFiveName:** `{BUTTON_FIVE_NAME}`\n\n**➣ ButtonFiveURL:** `{BUTTON_FIVE_URL}`\n\n**➣ ButtonSixName:** `{BUTTON_SIX_NAME}`\n\n**➣ ButtonSixURL:** `{BUTTON_SIX_URL}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_6'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_8')
                    ]
                ]
            )
        )
    elif data == '8':
        return await query.message.edit(
            __header__.format(data)
            + f"**꧁ HEROKU CONFIG ꧂**\n\n\n**➣ HerokuName:** `{HEROKU_APP_NAME}`\n\n**➣ HerokuAPI:** `{HEROKU_API_KEY}`\n\n**꧁ Shortener Config ꧂**\n\n\n**➣ ShortenerName:** `{SHORTENER}`\n\n**➣ ShortenerAPI:** `{SHORTENER_API}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_7'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_9')
                    ]
                ]
            )
        )
    elif data == '9':
        return await query.message.edit(
            __header__.format(data)
            + f" **꧁ OTHER CONFIG ꧂**\n\n\n**➣ IgnorePendingRequest:** `{IGNORE_PENDING_REQUESTS}`\n\n**➣ ImageURL:** `{IMAGE_URL}`\n\n**➣ Directory:** `{DOWNLOAD_DIR}`\n\n**➣ StatusInterval:** `{DOWNLOAD_STATUS_UPDATE_INTERVAL}`\n\n**➣ ViewLink:** `{VIEW_LINK}`\n\n**➣ DatabaseURL:** `{DB_URI}`\n\n**➣ DeleteMessageDuration:** `{AUTO_DELETE_MESSAGE_DURATION}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_8'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_1')
                    ]
                ]
            )
        )
    elif data == 'end':
        return await query.message.delete()

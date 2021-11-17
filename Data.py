from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

You Can Use Me To Manage Channels With Tons Of Features. Use Below Buttons To Learn More !

By @DKBOTZ
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/DKBOTZFUTURE/502")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/DKBOTZ/300")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/DK_BOTZ")],
    ]

    # Help Message
    HELP = """
Everything is Self Explanatory After You Add a Channel.
To Add a Channel Use Keyboard Button 'Add Channels' or Alternatively For Ease, use /add Command

✨ Available Commands ✨

/about - About The Bot
/help - This Message
/start - Start the Bot

Alternative Commands
/channels - List added Channels
/add - Add a channel
/report - Report a Problem
    """

    # About Message
    ABOUT = """
About This Bot 

A Telegram Channel Automation Bot By @DKBOTZ

ALL BOT STATUS : [Click Here](https://t.me/DKBOTZFUTURE/50)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : [Anonymous](https://t.me/DKBOTZHELP)
    """

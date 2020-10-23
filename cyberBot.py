from discord.ext import commands
from discord import activity

from secrets import token
from util.cogUtil import load_all_cogs, reload_all_cogs
from util.util import (quick_response, error_response)

from util.checks import is_owner

bot = commands.Bot('.')


@bot.event
async def on_ready():
    """On ready event to setup the bot"""
    await bot.change_presence(activity=activity.Game(name="Help: .help"))
    
    print('Online!')


@bot.command()
@commands.check(is_owner)
async def load(ctx: discord.ext.context, extension: str):
    """Load command for cogs"""
    bot.load_extension(f'cogs.{extension}')
    try:
        await quick_response(ctx.channel, f'{extension.title()} loaded.')
    except commands.ExtensionNotLoaded or commands.ExtensionNotFound:
        await error_response(ctx, 'Failed to load!')
        return


@bot.command()
@commands.check(is_owner)
async def unload(ctx, extension: str):
    """Unload command for cogs"""
    bot.unload_extension(f'cogs.{extension}')
    try:
        await quick_response(ctx.channel, f'{extension.title()} unloaded.')
    except commands.ExtensionNotLoaded or commands.ExtensionNotFound:
        await error_response(ctx, 'Failed to unload!')
        return


@bot.command()
@commands.check(is_owner)
async def reload(ctx, extension=None):
    """Reload command for cogs"""
    extensions_loaded = []
    if extension == "all" or extension is None:
        extensions_loaded = reload_all_cogs(bot)
    else:
        try:
            bot.reload_extension(f'cogs.{extension}')
            extensions_loaded.append(extension)
        except commands.ExtensionNotLoaded or commands.ExtensionNotFound:
            await error_response(ctx, 'Failed to reload!')
            return
    await quick_response(ctx.channel, f'{str.join(", ", extensions_loaded)} loaded!')

# load the cogs when the bot starts
load_all_cogs(bot)
# run the bot
bot.run(token)

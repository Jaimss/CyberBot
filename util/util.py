import discord

from util.colorUtil import (bot_color, red_color, orange_color, green_color)


async def quick_response(channel, message, message_color=bot_color):
    return await channel.send(
        embed=discord.Embed(
            description=message,
            color=message_color
        )
    )


async def success_response(channel, message):
    return await quick_response(channel, message, green_color)


async def error_response(channel, message):
    return await quick_response(channel, message, red_color)


async def warn_response(channel, message):
    return await quick_response(channel, message, orange_color)

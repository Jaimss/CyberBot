from discord.ext import commands as com

from util.util import (quick_response, error_response)


class Purge(com.Cog):
    def __init__(self, bot):
        self.bot = bot

    @com.command(name='purge')
    async def purge_command(self, ctx, limit=None):
        if limit is None:
            limit = "50000"

        if limit.isdigit():
            messages = await ctx.channel.purge(limit=int(limit))
            limit = len(messages)
        else:
            await error_response(ctx.channel, 'Please provide a valid integer!')
            return
        await quick_response(ctx.channel, f'Successfully purged {limit} messages!')
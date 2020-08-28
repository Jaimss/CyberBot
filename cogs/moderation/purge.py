from discord.ext import commands as com

from util.util import (quick_response, error_response)

from util.checks import is_pinned


class Purge(com.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TODO: Warn for deleting whole channel.
    @com.command(name='purge')
    @com.has_permissions(manage_messages=True)
    async def purge_command(self, ctx, limit=None):
        if limit is None:
            limit = "50000"

        if limit.isdigit():
            messages = await ctx.channel.purge(limit=int(limit), check=is_pinned)
            limit = len(messages)

        else:
            await error_response(ctx.channel, 'Please provide a valid integer!')
            return
        await quick_response(ctx.channel, f'Successfully purged {limit} messages!')

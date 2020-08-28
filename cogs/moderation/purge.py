from discord.ext import commands as com
from discord import DMChannel

from util.checks import is_pinned
from util.util import (quick_response, error_response, warn_response)


class Purge(com.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TODO: Warn for deleting whole channel.
    @com.command(name='purge')
    @com.has_permissions(manage_messages=True)
    async def purge_command(self, ctx, limit=None):
        if limit is None:
            limit = "50000"

        def check_rxn(reaction, user):
            if user != ctx.message.author:
                return False
            if str(reaction.emoji) == "❌" or "✅":
                return True
            else:
                return False

        if limit == "50000":
            await warn_response(ctx.channel, 'You are about to clear the channel!\nReact ✅ to continue or ❌ to cancel!')
            reaction, user = await self.bot.wait_fot('reaction_add', check=check_rxn)
            if str(reaction.emoji) == "❌":
                await quick_response(ctx.channel, 'Canceled Purge!')
                return

        if limit.isdigit():
            messages = await ctx.channel.purge(limit=int(limit), check=is_pinned)
            limit = len(messages)

        else:
            await error_response(ctx.channel, 'Please provide a valid integer!')
            return
        await quick_response(ctx.channel, f'Successfully purged {limit} messages!')

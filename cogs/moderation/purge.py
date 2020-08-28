import asyncio

from discord.ext import commands as com

from util.checks import is_pinned
from util.util import (quick_response, error_response, warn_response)


class Purge(com.Cog):
    def __init__(self, bot):
        self.bot = bot

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

        if not limit.isdigit():
            await error_response(ctx.channel, 'Please provide a valid integer!')
            return

        if int(limit) >= 1000:
            m = await warn_response(ctx.channel, f'You are about to clear more than 1,000 messages!\n '
                                                 f'React ✅ to continue or ❌ to cancel!')
            await m.add_reaction('✅')
            await m.add_reaction('❌')
            try:
                rxn, _ = await self.bot.wait_for('reaction_add', timeout=60.0, check=check_rxn)
            except asyncio.TimeoutError:
                m = await error_response(ctx.channel, 'No reaction added!')
                await asyncio.sleep(3)
                await m.delete()
                return
            if str(rxn.emoji) == "❌":
                await quick_response(ctx.channel, 'Canceled Purge!')
                return

        messages = await ctx.channel.purge(limit=int(limit), check=is_pinned)
        limit = len(messages)
        await quick_response(ctx.channel, f'Successfully purged {limit} messages!')

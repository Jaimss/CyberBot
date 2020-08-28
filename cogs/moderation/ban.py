from discord.ext import commands as com

from util.util import (error_response, quick_response)


class Ban(com.Cog):
    def __init__(self, bot):
        self.bot = bot

    @com.command(name='ban')
    async def ban_command(self, ctx, banned=None, *, reason=None):
        """Ban a user by ID"""
        guild = ctx.message.guild
        if banned is None or not banned.isdigit():
            await error_response(ctx.channel, 'Please provide a user ID!')
            return

        banned = guild.get_member(int(banned))
        if banned is None:
            await error_response(ctx.channel, 'Could not ban a user not in the guild!')
            return

        await guild.ban(banned, reason=reason)

        await quick_response(ctx.channel, f'Successfully banned `{banned.name}#{banned.discriminator}`!')

    @com.command(name='unban')
    async def unban_command(self, ctx, banned=None, *, reason=None):
        """Unban a user by ID"""
        guild = ctx.message.guild
        if banned is None or not banned.isdigit():
            await error_response(ctx.channel, 'Please provide a user ID!')
            return

        for (_, user) in await guild.bans():
            if int(user.id) == int(banned):
                await guild.unban(user, reason=reason)
                await quick_response(ctx.channel,
                                     f'Successfully unbanned user: `{user.name}#{user.discriminator}`!')
                return

        await error_response(ctx.channel, 'Failed to find a banned user with that ID!')
        return

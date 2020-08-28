from discord import Embed
from discord.ext import commands as com

from util.colorUtil import (bot_color)


class Help(com.Cog):
    def __init__(self, bot):
        self.bot = bot

    @com.command(name='help')
    async def help_command(self, ctx, group=None):
        """A help command for all the bots features"""
        # all the different pages
        help_page = Embed(
            title='Cyber - Help',
            color=bot_color
        ).add_field(
            name='`.help`',
            value='» Shows this page.',
            inline=False
        ).add_field(
            name='`.help misc`',
            value='» Miscellaneous Help Commands',
            inline=False
        ).add_field(
            name='`.help moderation`',
            value='» Moderation Help Commands',
            inline=False
        ).set_footer(text='Bot By: Jaims | https://jaims.dev')
        # misc page
        misc_page = Embed(
            title='Cyber - Help | Miscellaneous',
            color=bot_color
        ).add_field(
            name='`.ping`',
            value='» Check if the bot is on.',
            inline=False
        ).set_footer(text='Bot By: Jaims | https://jaims.dev')
        # moderation page
        moderation_page = Embed(
            title='Cyber - Help | Moderation',
            color=bot_color
        ).add_field(
            name='`.purge [amount]`',
            value='» Purge an optional amount of messages.',
            inline=False
        ).add_field(
            name='`.ban <user id> [reason]`',
            value='» Ban a user with an optional reason.',
            inline=False
        ).add_field(
            name='`.unban <user id> [reason]`',
            value='» Unban a user with an optional reason.',
            inline=False
        ).set_footer(text='Bot By: Jaims | https://jaims.dev')

        # get which page needs to be sent first
        if group == "misc":
            page = misc_page
        elif group == "moderation":
            page = moderation_page
        else:
            page = help_page

        await ctx.channel.send(embed=page)


def setup(bot):
    bot.add_cog(Help(bot))

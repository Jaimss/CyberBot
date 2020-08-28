from discord import Embed
from discord.ext import commands as com

from util.colorUtil import bot_color


class Say(com.Cog):
    def __init__(self, bot):
        self.bot = bot

    @com.command(name='say')
    @com.has_permissions(manage_channels=True)
    async def say_command(self, ctx, *, args):
        await ctx.channel.send(
            embed=Embed(
                description=args,
                color=bot_color
            ).set_footer(text=ctx.message.author.name, icon_url=ctx.message.author.avatar)
        )


def setup(bot):
    bot.add_cog(Say(bot))

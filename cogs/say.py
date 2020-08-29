from discord import Embed
from discord.ext import commands as com

from util.colorUtil import bot_color


class Say(com.Cog):
    def __init__(self, bot):
        self.bot = bot

    @com.command(name='say')
    @com.has_permissions(manage_messages=True)
    async def say_command(self, ctx, *, args):
        # cleanup the message to say
        await ctx.message.delete()
        if args.startswith("-p"):
            await ctx.channel.send(args[3:])
        else:
            await ctx.channel.send(
                embed=Embed(
                    description=args,
                    color=bot_color
                ).set_footer(text=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
            )


def setup(bot):
    bot.add_cog(Say(bot))

from discord.ext import commands as com

from util.util import quick_response


class Ping(com.Cog):
    def __init__(self, bot):
        self.bot = bot

    @com.command(name='ping')
    async def ping_command(self, ctx):
        await quick_response(ctx.channel, 'Pong!')


def setup(bot):
    bot.add_cog(Ping(bot))

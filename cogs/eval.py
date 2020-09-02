import sys
from io import StringIO

from discord import Embed
from discord.ext.commands import (Cog, Context, command)

from util.colorUtil import bot_color, red_color


class EvalCommand(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name='evalpy')
    async def evaluate_command(self, ctx: Context, *, code):
        await ctx.message.delete()
        code = code.replace('```py', '').replace('```', '')

        try:
            old_stdout = sys.stdout
            redirected_out = sys.stdout = StringIO()
            exec(code)
            sys.stdout = old_stdout
        except:
            await ctx.message.channel.send(
                embed=Embed(
                    title='Python Code Evaluation',
                    description='The code you provided generated an exception!',
                    color=red_color
                ).set_footer(text=f'Code By: {ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            )
            return

        await ctx.message.channel.send(
            embed=Embed(
                title='Python Code Evaluation',
                description=f'Code:\n```py\n{code}```Response:\n```\n{redirected_out.getvalue()}```',
                color=bot_color
            ).set_footer(text=f'Code By: {ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        )


def setup(bot):
    bot.add_cog(EvalCommand(bot))

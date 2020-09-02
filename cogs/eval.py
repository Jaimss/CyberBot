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
                    description='Your code generated an exception!',
                    color=red_color
                ).set_footer(text=f'Code By: {ctx.message.author.name}', icon_url=ctx.message.author.avatar_url).add_field(
                    name='Your Code:',
                    value=f'```py\n{code}```'
                )
            )
            return

        await ctx.message.channel.send(
            embed=Embed(
                title='Python Code Evaluation',
                color=bot_color
            ).set_footer(text=f'Code By: {ctx.message.author.name}', icon_url=ctx.message.author.avatar_url).add_field(
                inline=False,
                name='Your Code:',
                value=f'```py\n{code}```'
            ).add_field(
                inline=False,
                name='Output:',
                value=f'```\n{redirected_out.getvalue()}```'
            )
        )


def setup(bot):
    bot.add_cog(EvalCommand(bot))

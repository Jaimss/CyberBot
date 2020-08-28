from discord.ext.commands import Bot

from .ban import Ban
from .purge import Purge


def setup(bot: Bot) -> None:
    """Add the cogs"""
    bot.add_cog(Purge(bot))
    bot.add_cog(Ban(bot))

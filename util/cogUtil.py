def load_all_cogs(bot):
    """Add all the cogs"""
    # remove the help command
    bot.remove_command('help')
    # load moderation cogs
    bot.load_extension('cogs.moderation')

    # add the regular cogs
    bot.load_extension('cogs.ping')
    bot.load_extension('cogs.help')
    bot.load_extension('cogs.say')
    bot.load_extension('cogs.eval')


def reload_all_cogs(bot) -> list:
    """Reload all cogs"""
    all_cogs = []
    # reload the moderation cogs
    bot.reload_extension('cogs.moderation')
    all_cogs.append("Moderation")

    # reload the regular cogs
    bot.reload_extension('cogs.ping')
    all_cogs.append("Ping")
    bot.reload_extension('cogs.help')
    all_cogs.append('Help')
    bot.reload_extension('cogs.say')
    all_cogs.append('Say')
    bot.reload_extension('cogs.eval')
    all_cogs.append('Eval')

    return all_cogs

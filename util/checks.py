async def is_owner(ctx):
    return ctx.message.author.id == 348146715162968065


async def is_pinned(message):
    return message.pinned

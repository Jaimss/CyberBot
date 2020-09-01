async def is_owner(ctx):
    return ctx.message.author.id == 348146715162968065


def is_pinned(message) -> bool:
    return not message.pinned

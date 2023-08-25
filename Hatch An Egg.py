@client.event
async def on_message(message):
    if message.author == client.user:
        return
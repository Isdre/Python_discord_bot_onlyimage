import discord
import json


token = ""

with open('token.json') as f:
    token = json.load(f)['token']

client = discord.Client()

@client.event
async def on_message(ctx):
    if ctx.channel.name == "tylko-obrazki":
        if ctx.attachments == []:
            await ctx.channel.purge(limit=1)

client.run(token)
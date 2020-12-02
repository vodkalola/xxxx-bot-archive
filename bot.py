import discord
import json
from discord.ext import commands

with open("config.json", "r") as read_file:
    config = json.load(read_file)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(config["token"])
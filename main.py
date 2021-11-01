import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='!', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)





client.run("OTA0NTU2ODc5MTMxMzE2MjI1.YX9QPQ.33e4hUwkFbdTtEYpkzlhIXsOnzs")
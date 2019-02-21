import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
Client = discord.Client()
client = commands.Bot (command_prefix = "~")
 


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='in the FG Clan'))
    print("Bot is online and ready to go!")



newUserMessage = """```diff
-Welcome to Fusion Gaming!
Please read the rules in the #rules_and_info channel.
-We have self assign roles!
Tell us what games you play by giving you self a role.
You can also join the clan in the #join fusion channel.
-If you ever leave and want to join back just search 'Fusion' in your DM's
Link:https://discord.gg/DqEhq8w
```"""



@client.event
async def on_member_join(member):
    await client.send_message(member, newUserMessage)

    @client.event
    async def on_message(message):
        if message.content =="magic":
            await client.send_message(message.channel, "magic is good")


client.run("NTQzNDc5MTI1MjAyMTczOTcx.Dz9QKA.xExaSVBUc_S4EyQHEeh5k62bFSU")

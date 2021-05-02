import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()





# client.run(TOKEN)
class CustomClient(discord.Client):
    @client.event
    async def on_ready(self):
        # for guild in client.guilds:
        #     if guild.name==GUILD:
        #         break
        # guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
        # replacement for for
        guild = discord.utils.get(client.guilds, name=GUILD)
        print(guild.name)
        print(guild.id)
        pass
    # @client.event
    # async def on_member_join(self,member):
    #     member.
    @client.event
    async def on_message(self, message):
        if message.author == client.user:
            return
        # if message.author.name=="Ironclad":
        #     await message.channel.send("fat ass")


        if message.content == 'jarvis!':
            await message.channel.send("Hello sir!")
            await message.channel.send("how may i help you "+message.author.name+ " ?")
            await message.channel.send("I haven't been completely built yet sir!")


client = CustomClient()
client.run(TOKEN)

import asyncio
import discord
import random
import os
from github import Github
from discord import ui, app_commands
from datetime import datetime



class aClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=1144327924875542548))
            # await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}")

guilds=[discord.Object(id=1144327924875542548)]
client = aClient()
tree = app_commands.CommandTree(client)
intents = discord.Intents.all()

sad_word = ['sad', 'tired', 'depressed']
motivational = ['hang on', 'come on', 'you can do it!']


class push_modal(ui.Modal, title="Push your code here"):
    language = ui.TextInput(label="Language", style=discord.TextStyle.short, default="py", required=True)
    problem = ui.TextInput(label="Problem", style=discord.TextStyle.short, required=True)
    code = ui.TextInput(label="Code", style=discord.TextStyle.paragraph,placeholder="Write your code here", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        g = Github("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")
        repo = g.get_repo("dmtrung14/leetcode_arxiv")
        filename=f'{self.problem}.{self.language}'
        message= f"update solution to {self.problem}"
        content=f"{self.code}"
        try:
            repo.create_file(path=filename, message=message, content=content, branch="main")
            embed = discord.Embed(title=self.title, description =f"File {self.problem}.{self.language} created successfully", timestamp = datetime.now(), color = discord.Colour.blue())
            embed.set_author(name = interaction.user, icon_url = interaction.user.avatar)
            await interaction.response.defer()
            await asyncio.sleep(5)
            await interaction.followup.send(embed = embed, ephemeral=True)
        except:
            embed = discord.Embed(title=self.title, description =f"Cannot commit {self.problem}.{self.language}. File either already exists or permission denied.", timestamp = datetime.now(), color = discord.Colour.blue())
            embed.set_author(name = interaction.user, icon_url = interaction.user.avatar)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        #why is it not running?
        # try:
        #     repo.create_file(f'/{self.problem}.{self.language}', f"update solution to {self.problem}", self.code, branch="main")
        #     embed = discord.Embed(title=self.title, description =f"File {self.problem}.{self.language} created successfully", timestamp = datetime.now(), color = discord.Colour.blue())
        #     embed.set_author(name = interaction.user, icon_url = interaction.user.avatar)
        #     await interaction.response.send_message(embed = embed, ephemeral=True)
        # except:
        #     embed = discord.Embed(title=self.title, description =f"Cannot commit {self.problem}.{self.language}. File either already exists or permission denied.", timestamp = datetime.now(), color = discord.Colour.blue())
        #     embed.set_author(name = interaction.user, icon_url = interaction.user.avatar)
        #     await interaction.response.send_message(embed=embed, ephemeral=True)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith('\hello'):
        await message.channel.send('Hello')

    if any(word in sad_word for word in msg.split()):
        await message.channel.send(random.choice(motivational))
# @tree.command(name="test", description="test", guilds= guilds)
@tree.command(name="test", description="testing", guild=discord.Object(id = 1144327924875542548))
async def self(interaction: discord.Interaction, name:str):
    await interaction.res
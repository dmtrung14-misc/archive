#Interesting Codes goes here!
try:
            repo.create_file(path=filename, message=message, content=content, branch="main")
            embed = discord.Embed(title=self.title, description =f"File {self.problem}.{self.language} created successfully", timestamp = datetime.now(), color = discord.Colour.blue())
            embed.set_author(name = interaction.user, icon_url = interaction.user.avatar)
            await interaction.response.defer()
            await asyncio.sleep(10)
            await interaction.followup.send(embed = embed, ephemeral=True)
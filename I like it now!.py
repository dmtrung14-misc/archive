@tree.command(name="test", description="testing", guild=discord.Object(id = 1144327924875542548))
async def self(interaction: discord.Interaction, name:str):
    await interaction.response.send_message(f"Hello {name}! I was made with Discord.py", ephemeral=True)

@tree.command(name="push", description="test made aware", guild=discord.Object(id=1144327924875542548))
async def self(interaction: discord.Interaction):
    await interaction.response.send_modal(push_modal())
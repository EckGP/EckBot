import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        await guild.system_channel.send(f'Welcome {member.mention}! Please visit the #roles channel to select your roles.')

client.run(os.environ['DISCORD_TOKEN'])

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

client.run('MTA5MDI1NzgzMzMzMDczNzI2NQ.G6UdTz.bi7y64Qw8dl8I7P3GOd6sZxsKGipf6I9l3qwi4')

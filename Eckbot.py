import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        await guild.system_channel.send(f'Welcome {member.mention}! Please visit the #roles channel to select your roles.')
        
from datetime import datetime, timedelta

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!reminder'):
        try:
            # Parse the reminder time from the message
            reminder_time = message.content.split(' ', 1)[1]
            days, hours, minutes = map(int, reminder_time.split(':'))

            # Calculate the reminder datetime
            reminder_datetime = datetime.now() + timedelta(days=days, hours=hours, minutes=minutes)

            # Send a confirmation message
            await message.channel.send(f'Okay {message.author.mention}, I will remind you at {reminder_datetime.strftime("%Y-%m-%d %H:%M:%S")}')

            # Wait until the reminder datetime
            await discord.utils.sleep_until(reminder_datetime)

            # Send the reminder message
            await message.channel.send(f'{message.author.mention}, this is your reminder!')
        except Exception as e:
            await message.channel.send(f'Sorry {message.author.mention}, I couldn\'t set the reminder. Please use the format `!reminder dd:hh:mm`')

client.run(os.environ['DISCORD_TOKEN'])

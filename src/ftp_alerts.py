import os

import discord
from discord.ext import tasks as discordTasks
from dotenv import load_dotenv

from helper import log_message, log
from camera_mapping import get_camera_name

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
ROOT_USER_ID = int(os.getenv('USER_ID'))
DATA_DIR =  os.getenv('DATA_DIR')

# Bot Set Up
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

send_message = True

@client.event
async def on_ready():
    await tree.sync()
    log(f'{client.user} has connected to Discord!')

    @discordTasks.loop(minutes=1)
    async def periodic_check():
        await check_file_alerts()

    periodic_check.start()

@client.event
async def on_message(message):
    log_message(message)

async def check_file_alerts():
    files = os.listdir(DATA_DIR)
    if files:
        user = await client.fetch_user(ROOT_USER_ID)
        for file in files:
            if send_message:
                discord_file = discord.File(os.path.join(DATA_DIR, file))
                camera_name = get_camera_name(file)
                await user.send(f'New alert from {camera_name}', file=discord_file)
            os.remove(os.path.join(DATA_DIR, file))

@tree.command(name='togglealerts', description='Toggle FTP alerts on or off')
async def toggle_alerts(interaction: discord.Interaction):
    await interaction.response.defer()
    if interaction.user.id != ROOT_USER_ID:
        await interaction.response.send_message('You do not have permission to use this command.', ephemeral=True)
        return
    global send_message
    send_message = not send_message
    status = "enabled" if send_message else "disabled"
    await interaction.followup.send(f'FTP alerts have been {status}.')

def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()
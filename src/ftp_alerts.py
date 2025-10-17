import os

import discord
from discord.ext import tasks as discordTasks
from dotenv import load_dotenv

from helper import log_message, log

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
ROOT_USER_ID = int(os.getenv('USER_ID'))
DATA_DIR = './data'


# Bot Set Up
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    log(f'{client.user} has connected to Discord!')

    @discordTasks.loop(minutes=1)
    async def periodic_check():
        await checkFileAlerts()

    periodic_check.start()

@client.event
async def on_message(message):
    log_message(message)

async def checkFileAlerts():
    files = os.listdir(DATA_DIR)
    if files:
        user = await client.fetch_user(ROOT_USER_ID)
        for file in files:
            discordFile = discord.File(os.path.join(DATA_DIR, file))
            await user.send(f'New alert: {file}', file=discordFile)
            os.remove(os.path.join(DATA_DIR, file))

def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()
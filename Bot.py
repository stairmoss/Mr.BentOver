import os
import asyncio
import discord
from dotenv import load_dotenv

from Gif_prediction import analyze_conversation
from shared import GIF

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Mr. Bentover is ready to cook! Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "$Bentover":
        history = []
        async for msg in message.channel.history(limit=5):
            if msg.content != "$Bentover":
                history.append({"username": msg.author.name, "content": msg.content})

        history.reverse()

        try:
            search_phrase = await asyncio.to_thread(analyze_conversation, history)
            gif_url = await asyncio.to_thread(GIF, search_phrase)
            await message.channel.send(gif_url)
        except Exception as error:
            print("Error running $Bentover:", error)

client.run(os.getenv("DISCORD_TOKEN"))
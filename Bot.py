import os 
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
    print(f"Mr.Bentover ready to cook GIFs {client.user}")
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == "$Bentover":
        history = []
        async for msg in message.channel.history(limit=5):
            history.append({"username":msg.author.name, "content": msg.content})
            
        history.reverse()
            

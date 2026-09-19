import os 
import discord 
from dotenv import load_dotenv
from Gif_prediction import analyze_conversation
from shared import GIF
from shared import gif_url


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
        
        try:
            
            search_phrase = analyze_conversation(history)

            
            gif_url = GIF(search_phrase)

            
            await message.channel.send(gif_url)

        except Exception as error:
            print("Error running $Bentover:", error)

client.run(os.getenv("DISCORD_BOT_TOKEN:"))
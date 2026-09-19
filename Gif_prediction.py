import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HACKCLUB_API_KEY")

API_URL = "https://ai.hackclub.com/proxy/v1/chat/completions"

MODEL = "qwen/qwen3-32b" 

conversation = [
    {
        "username": "Karthik",
        "content": "Bro, exam tomorrow and I haven't studied."
    },
    {
        "username": "Thejus",
        "content": "We're cooked 💀"
    }
]

def format_conversation(history):
    lines = []

    for user_input  in history:
        username = user_input["username"]
        content = user_input["content"]

        line = f"{username}: {content}"

        lines.append(line)

    return "\n".join(lines)


     
def analyze_conversation(history):
    conversation_text = format_conversation(history)

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are Mr. Bentover, a funny Discord reaction bot. Return ONLY a short search phrase for a funny GIF matching the chat and u should give the the one or two word phrase as a if its a dark and conversation make it the the word according to the Humour. No explanation, no punctuation."
            },
            {
                "role": "user",
                "content": conversation_text
            }
        ]
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=data,
        timeout=60
    )

    response.raise_for_status()
    result = response.json()

    content = result["choices"][0]["message"]["content"]
 
    if not content:
        return "funny panic reaction"

    return content.strip()
 
 
if __name__ == "__main__":
    result = analyze_conversation(conversation)
    print("Ai GIF search phrase :", result)
    
  
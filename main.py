from Gif_prediction import analyze_conversation
from shared import GIF

conversation = [
    {"username": "Karthik", "content": "hello"}
]

def show_history():
    print("\n--- Recent messages ---")
    for message in conversation[-4:]:
        print(f'{message["username"]}: {message["content"]}')
    print("-----------------------\n")

while True: 
    user = input("Type your username: ")
    user_input = input("Type your message: ")
    
    if user_input == "$quit":
        break
    
    if user_input == "$Bentover":
        print("Mr. BentOver ready to cook...")
        recent_msg = conversation[-4:]
        show_history()
        
        try:
            gif_search = analyze_conversation(recent_msg)
            print("GIF search phrase:", gif_search)
            print("GIF URL:", GIF(gif_search))
        except Exception as e:
            print(f"Error occurred while analyzing conversation: {e}")
            
        continue

    conversation.append({"username": user, "content": user_input})
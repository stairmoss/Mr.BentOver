
conversation = [
               {
                 "username" : "Karthik",
                 "content" : "hello" 
               },
              
 ]
while True: 
    user = input("type our username :")
    user_input = input("Type your message  : ")
    
  
    
    def show_history(user_input):
        for user_input in conversation[-4:]:   
                 print(f"{user_input["username"]} :  {user_input["content"]}")                                                 
    if user_input == "$Bentover":
     print("Mr.BentOver ready to cook")
     show_history(user_input)
    elif user_input == "$quit":
        break
    
    conversation.append({"username" : user, "content" : user_input})
        


show_history()
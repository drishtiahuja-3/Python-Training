
messages = [
    {
        "sender": "99155 71177",
        "receiver": "99999 11111",
        "conversation":[
            "Hello",
            "How are you", 
            "Its Friday",
            "Lets Party. No Code today"
        ]
    },
    {
        "sender": "99155 71177",
        "receiver": "99999 22222",
        "conversation":[
            "Hello",
            "Kaisa hai bhai", 
            "Aj Friday hai",
            "lets party."
        ]
    },
    {
        "sender": "98765 12345",
        "receiver": "99155 71177",
        "conversation":[
            "Beta",
            "Bahut Kaam Hai", 
            "Sabji leni hai",
            "jaldio aa jana. mummy here"
        ]
    }

]

search_keyword = input("Enter Word to Search: ")
# Logic
# Firday Assignment :)


print(" ")

flag = False

for word in messages:
    sender = word["sender"]
    receiver = word["receiver"]
    conversation = word["conversation"]

    for data in conversation:
        if search_keyword in data:
            print("Sender: {} | Receiver: {}".format(sender,receiver))
            print("Message: {}".format(data))
            print("Word found at index: {}".format(data.find(search_keyword)))
            print("~~~~~~~~~~~~~~~")
            flag = True
        
if flag == False:
    print("Word not Found")
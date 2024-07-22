#%%
dict = {
        "greeting": {
                "hello": "Hi there! How can I help you?",
                "hi": "Hello! What can I do for you today?",
                "hey": "Hey! How can I assist you?"
        },
        "parting": {
                "": "Goodbye! Have a great day.",
                "see you": "See you later!",
                "take care": "Take care!"
        },
        "default": "I'm sorry, I didn't understand that. Can you please clarify?",
        "quit": "end"
    }
#find the index of input
def find(key):
    for i in range(len(list(dict))-1):
        Type = list(dict.keys())[i]
        for k in range(len(dict[Type])):
            if list(dict[Type])[k] == key:
                t = list(dict.keys())[i]
                return [t,k]
#find('hello')

def search(Type, index):
    index = list(dict[Type].keys())[index]
    return (dict[Type][index])
#search('greeting', 0)
def prompt(inp: str):
        try:
             return search(find(inp)[0],find(inp)[1])
        except:
             return dict['default']
             

while True:
    inp = input("You: ")
    if inp.lower() == "quit":
            break
    print("Bot:", prompt(inp))
print('\nqend')
#%%

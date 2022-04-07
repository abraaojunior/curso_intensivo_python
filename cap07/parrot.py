prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# loop infinito, press crtl+c
'''
x = 0
while x >= 0:
    print(x)
    x += 1
'''

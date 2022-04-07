''' # 1o exemplo do cap
#print("digite um texto qualquer: ")
message = input("Digite que eu repito: ")
print(message)

print("continua\n")

name = input("Please enter your name: ")
print("\nHello, " + name + "!")

print("continua\n")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

print("continua\n")

#even_or_odd.py
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\n The number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
print("continua\n")

#7.2 lug em rest

message = "Por favor, me informe: "
message += "\n mesa para quantos? "
quantidade_mesa = input(message)
quantidade_mesa = int(quantidade_mesa)
if quantidade_mesa < 9:
    print("Sua mesa esta pronta!")
else:
    print("Por favor, aguarde enquanto preparamos sua mesa!")
print("continua\n")
 '''
# 7.3 multiplos de dez
'''
number = input("Digite um número qualquer: ")
number = int(number)
if number % 10 == 0:
    #if (number / 10) == (0.1 * number):
        print("é multiplo de dez!")
else:
    print("ñ é multiplo de dez!")

'''
#usando while como exemplo de contador
'''
current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1
'''
#parrot.py
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
#message = ""
while active:
    message = input(prompt)
        if message == 'quit':
        active = False
        else:
            print(message)

'''


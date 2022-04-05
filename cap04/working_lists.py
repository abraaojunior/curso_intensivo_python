lista_de_convidados = []
mae = "Ruth"
pai = "Abraão"
familia_irmao_1 = ["Toni", "Natalia", "Olavo"]
familia_irmao_2 = ["Isaac", "Jose", "Davi"]
familia_irmao_3 = ["Jacob", "Rose", "Benjamin"]

print(mae, pai, familia_irmao_1, familia_irmao_2, familia_irmao_3)

lista_de_convidados.append(pai)
print(lista_de_convidados)

lista_de_convidados.append(mae)
print(lista_de_convidados)

lista_de_convidados.append(familia_irmao_1)
print(lista_de_convidados)

lista_de_convidados.append(familia_irmao_2)
print(lista_de_convidados)

lista_de_convidados.append(familia_irmao_3)
print(lista_de_convidados)

for lista_de_convidado in lista_de_convidados:	print(lista_de_convidado)

magicians = ["\nalice", "david", "carolina"]
for magician in magicians: print(magician)

#magicians = ["\nalice", "david", "carolina"]
#for magician in magicians: 
#	{
#		print(str(magician.title()) + ", that was a great trick!")
#		print("I can't wait to see your next trick, " + str(magician.title()))
#	}
#print("Tank you, everyone. That was a great magic show!")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title()+ ".\n")
print("congratulaionts!!!!\n\n")

pizzas = ["mussarela", "calabresa", "alho", "marguerita", "4 queijos"]
print(pizzas)

print("\n")

for pizza in pizzas:
	print("Gosto de pizza de: " + pizza)
print("Realmente gosto de pizza!!!\n\n")

squares = [value**2 for value in range(1,11)]
print(squares)
print("\n\n")

quadrados = []
for value in range(1,11):
	quadrado = value**2
	quadrados.append(quadrado)
print(quadrados)
print("\n\n")

quadrados = []
for value in range(1,11):
	quadrados.append(value**2)
print(quadrados)
print("\n\n")

um_ate_vinte = []
for value in range(1,21):
	um_ate_vinte.append(value) 
print(um_ate_vinte)

um_ate_vinte_impar = []
for value in range(1,20,2):
	um_ate_vinte_impar.append(value) 
print(um_ate_vinte_impar)

um_ate_milhao = []
for value in range(1,1000001):
	um_ate_milhao.append(value) 
print(um_ate_milhao)

um_ate_milhao = []
for value in range(1,1000001):
	um_ate_milhao.append(value) 
print(sum(um_ate_milhao))
print(min(um_ate_milhao))
print(max(um_ate_milhao))

tres_em_tres = []
for value in range(3,30,3):
	tres_em_tres.append(value)
print(tres_em_tres)

cubes = [value**3 for value in range(1,11)]
print(cubes)
print("\n\n")

#fatiando uma lista

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
print("\n\n")

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:4])
print("\n\n")

print("Os tres primeiros elementos são: ")
print(players[0:3])

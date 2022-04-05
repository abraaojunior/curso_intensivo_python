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

lista_de_convidados.pop()
print(lista_de_convidados)


lista_de_convidados.pop()
print(lista_de_convidados)


lista_de_convidados.pop()
print(lista_de_convidados)


del lista_de_convidados[1]
print(lista_de_convidados)

del lista_de_convidados[0]
print(lista_de_convidados)

cars = ["bmw", "audi", "toyota", "mercedez"]
#cars.split()
cars.sort()
print(cars)

cars = ["bmw", "audi", "toyota", "mercedez"]
#cars.split()
cars.sort(reverse=True)
print(cars)

cars = ["bmw", "audi", "toyota", "mercedez"]
#cars.split()
#cars.sorted()
print("Here is the original list: " + str(cars))

cars.sort()
print("\nHere is the sorted list: " + str(cars))

print(len(cars))


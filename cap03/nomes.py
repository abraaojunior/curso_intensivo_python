names=["Abraão", "Deusiane", "Gabriela", "Olavo", "Davi", "Benjamin"]
message = "Olá me chamo " + names[1]
print(names[1])
print(message)

#for(int i = 0, names[i], i++)
#saudacao = "olá, me chamo: - "
#print(saudacao + names[i])

motorcycles = []
print(motorcycles)


motorcycles.append("honda")
print(motorcycles)

motorcycles.append("yamaha")
print(motorcycles)

motorcycles.append("suzuki")
print(motorcycles)

motorcycles.insert(0, "ducati")
#motorcycles.append("honda")
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

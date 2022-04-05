dimensions = (200, 50)
print(dimensions[0])

#dimensions[0] = 250
print(dimensions)

# exercicio 4.13 - Buffet

buffet = ("strogonoff", "frango", "carne", "peixe", 
"porco")

for prato in buffet:
	print(prato)

sugestao = ("mocoto", "vaca atolada")
buffet_novo=[] 
buffet_novo = buffet + sugestao
for prato in buffet_novo:
	print(prato)

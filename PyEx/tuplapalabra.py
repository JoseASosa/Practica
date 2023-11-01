tupla = ('Rakyos', 'Carro', 'Camioneta', 'Camion', 'Arroz')

contador = 0
for palabra in tupla:
    contador += palabra.count('a')

print(contador)
# Crie uma lista com 10 números aleatórios, itere essa llista e printar em tela os valores que são ímpares e pares
#ex: lista gerada aleatoriamente: [x, x, x, x, x]
#impares: [y, y, y, y]
#pares: [o,o, o, o, o]

import random

lista = []
lista_par = []
lista_impar = []
i = 1

while i<=10:
    lista.append(random.randrange(1, 100, 2))
    i = i+1

print(f'Lista gerada aleatoriamente: {lista}')

for n in lista:
    if n % 2 != 0:
        lista_impar.append(n)   
    else:
        lista_par.append(n)

print(f'Ímpares: {lista_impar}')
print(f'Pares: {lista_par}') 
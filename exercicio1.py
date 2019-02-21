#criar função que receba uma lista de 20 valores aleatórios, retornar apenas o valor e printar em tela
#def bla(lista)
#return

import random

lista =[]
i = 1

while i<=20:
    lista.append(random.randrange(1, 100, 3))
    # append significa acrescentar
    i = i+1

print(f'Lista gerada aleatoriamente: {lista}')

def maior_valor(lista):
    return max(lista, key=int)
    # não precisa por key=int. é só para reforçar que quer retornar um inteiro

print(f'Maior valor é: {maior_valor(lista)}')
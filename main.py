import random

elementos = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
]
parejas = []

n_elementos = len(elementos)

print(elementos)
i = 1
for elemento in elementos:
    print(i,elemento)
    i += 1
print('\n')

boolean = True
while boolean:
    elemento_1 = random.choice(elementos)
    elemento_2 = random.choice(elementos)

    if elemento_1 != elemento_2:
        elementos.pop(elementos.index(elemento_1))
        parejas.append(elemento_1)
        elementos.pop(elementos.index(elemento_2))
        parejas.append(elemento_2)

    if elemento_1 == elemento_2:
        print('procesando...')
    
    if n_elementos == len(parejas):
        boolean = False
print('\n')
print(parejas)

lugar_0 = 0
lugar_1 = 1
n_parejas = int(len(parejas) / 2)
for i in range(n_parejas):
    print(parejas[lugar_0], ' & ', parejas[lugar_1])
    lugar_0 += 2
    lugar_1 += 2
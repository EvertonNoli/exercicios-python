from random import randint

valores = tuple(randint(0,1000)for i in range(10))
maior = menor = valores[0]

for c in valores:
    if c>maior:
        maior = c
    if c<menor:
        menor = c


print(f'Valores sorteados: {valores}')
print(f'O menor número é {menor}')
print(f'O maior número é {maior}')
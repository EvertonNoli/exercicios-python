maior = 0
menor = 0

for c in range(1,6):
    peso=float(input(f'Digite o peso da {c}° pessoa:'))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior=peso
        if peso < menor:
            menor=peso

    c+=1


print(f'O maior peso lido foi de {maior}KG')
print(f'O menor peso lido foi de {menor}KG')
valores = [[], []]
valor = 0

for c in range(1,8):
    valor = int(input('Digite um valor:'))
    if valor%2==0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)


valores[0].sort()
valores[1].sort()
print(f'Valores pares: {valores[0]}')
print(f'Valores ímpares: {valores[1]}')
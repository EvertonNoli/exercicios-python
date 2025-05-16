#create a matriz 3x3
#pegue a soma da segunda linha
#pegue o maior da terceira coluna

matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]

soma = maior = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para: [{l},{c}] '))
        if l == 1:
            soma+=matriz[l][c]
        if c == 2:
            if l == 0:
                maior = matriz[l][c]
            elif maior < matriz[l][c]:
                maior = matriz[l][c]

print('-='*10)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end = '')
    print()

print(f'Soma dos valores da segunda linha {soma}')
print(f'O maior valor na terceira coluna é {maior}')
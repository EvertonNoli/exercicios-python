#pegar o maior valor da segunda linha
#menor valor da primeira coluna
#multiplicar a última linha

matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]

maior = menor = 0
mult = 1

for c in range(0,3):
    for l in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para: [{l},{c}]'))
        if l == 1:
            if c == 0:
                maior=matriz[l][c]
            elif maior<matriz[l][c]:
                maior=matriz[l][c]

        if c==0:
            if l == 0:
                menor = matriz[l][c]
            elif menor>matriz[l][c]:
                menor = matriz[l][c]

        if l == 2:
            mult*=matriz[l][c]

print('-='*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'O maior valor na segunda linha é {maior}')
print(f'O menor valor na primeira coluna é {menor}')
print(f'A multiplicação da última linha é {mult}')
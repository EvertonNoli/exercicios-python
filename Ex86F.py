#maior valor da primeira linha
#menor valor da terceira coluna
#multiplica diagonais

matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]

maior = menor = 0
diagPri = 1
diagSec = 1

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para [{l}, {c}]:'))

        if l == 0:
            if c == 0:
                maior = matriz[l][c]
            elif maior<matriz[l][c]:
                maior = matriz[l][c]

        if c == 2:
            if l == 0:
                menor = matriz[l][c]
            elif menor>matriz[l][c]:
                menor = matriz[l][c]

        if c == l:
            diagPri*=matriz[l][c]
        if l+c==2:
            diagSec*=matriz[l][c]




print('-='*10)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'Maior valor da primeira linha: {maior}')
print(f'Menor valor da terceira coluna: {menor}')
print(f'Multplicação da diagonal primária: {diagPri}')
print(f'Multiplicação da diagonal secundária: {diagSec}')
#maior valor da segunda coluna
#menor valor da primeira linha
#soma diagonal

matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]

maior = menor = diagPri = diagSec = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para [{l},{c}]:'))

        if c == 1:
            if l == 0:
                maior = matriz[l][c]
            elif maior<matriz[l][c]:
                maior=matriz[l][c]

        if l == 0:
            if c == 0:
                menor = matriz[l][c]
            elif menor>matriz[l][c]:
                menor = matriz[l][c]

        if l == c:
            diagPri += matriz[l][c]
        if l + c == 2:
            diagSec += matriz[l][c]

print('-='*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()

print(f'O maior valor na segunda coluna é {maior}')
print(f'O menor valor na primeira linha é {menor}')
print(f'Soma dos valores na diagonal principal: {diagPri}')
print(f'Soma dos valores na diagonal secundária: {diagSec}')
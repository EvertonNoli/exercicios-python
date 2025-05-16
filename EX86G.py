#criar matriz
#maior valor linha 2
#menor valor coluna 3
#media diagonal princ
#mult diagonal secundaria

matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]

maior = menor = soma = 0
media = mult = 1

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para [{l}, {c}]: '))
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            elif maior<matriz[l][c]:
                maior = matriz[l][c]

        if c == 2:
            if l == 0:
                menor = matriz[l][c]
            elif menor>matriz[l][c]:
                menor = matriz[l][c]

        if c==l:
            soma+=matriz[l][c]

        if c+l==2:
            mult*=matriz[l][c]

media=soma/3

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()

print(f'O maior valor na segunda linha é: {maior}')
print(f'O menor valor na terceira coluna é: {menor}')
print(f'A média dos valores na diagonal principal é {media:.2f} e a soma {soma}')
print(f'A multiplicação dos valores na diagonal secundária é {mult}')
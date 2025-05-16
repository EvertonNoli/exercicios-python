matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]
somaPar = somaCol = maior = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        if c == 2:
            somaCol+=matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if matriz[l][c]>maior:
                    maior=matriz[l][c]
        if matriz[l][c]%2==0:
            somaPar+=matriz[l][c]


print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()

print(f'Soma dos números pares: {somaPar}')
print(f'Soma da terceira coluna: {somaCol}')
print(f'O maior valor da segunda linha é: {maior}')
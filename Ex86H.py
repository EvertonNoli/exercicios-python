matriz1 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz2 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matrizSoma = [[0,0,0],
              [0,0,0],
              [0,0,0]]

matrizMult = [[0,0,0],
              [0,0,0],
              [0,0,0]]

matrizSub = [[0,0,0],
             [0,0,0],
             [0,0,0]]

print('-='*10)
print('VALORES DA PRIMEIRA MATRIZ')
for l in range(0,3):
    for c in range(0,3):
        matriz1[l][c]=int(input(f'Digite o valor para [{l},{c}]: '))

print('-='*10)
print('VALORES DA SEGUNDA MATRIZ')
for l in range(0,3):
    for c in range(0,3):
        matriz2[l][c]=int(input(f'Digite o valor para [{l},{c}]: '))

print('-='*10)
print('PRIMEIRA MATRIZ')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz1[l][c]:^5}]',end='')
    print()

print('-='*10)
print('SEGUNDA MATRIZ')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz2[l][c]:^5}]',end='')
    print()

print('-='*10)
print('SOMA DAS MATRIZES')
for l in range(0,3):
    for c in range(0,3):
        matrizSoma[l][c]=matriz1[l][c]+matriz2[l][c]

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matrizSoma[l][c]:^5}]',end='')
    print()

print('-='*10)
print('MULTIPLICAÇÃO DAS MATRIZES')
for l in range(0,3):
    for c in range(0,3):
        matrizMult[l][c]=matriz1[l][c]*matriz2[l][c]

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matrizMult[l][c]:^5}]', end='')
    print()

print('-='*10)
print('SUBTRAÇÃO DAS MATRIZES')
for l in range(0,3):
    for c in range(0,3):
        matrizSub[l][c]=matriz1[l][c]-matriz2[l][c]

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matrizSub[l][c]:^5}]',end='')
    print()
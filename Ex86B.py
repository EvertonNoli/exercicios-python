matriz=[[0,0,0],[0,0,0]]

print('Matriz 2 x 3:')
for l in range(2):
    for c in range (3):
        print(f'{matriz[l][c]:^5}',end=' ')
    print()

print('Matriz 3 x 2:')

matriz2 = ([0,0],
           [0,0],
           [0,0])
for l in range(3):
    for c in range(2):
        print(f'{matriz2[l][c]:^5}',end='')
    print()

matriz3 = ([0,0,0],
           [0,0,0],
           [0,0,0])
print('Matriz 3 x 3')

for l in range(3):
    for c in range(3):
        print(f'{matriz3[l][c]:^5}',end='')
    print()

matriz4 = ([0,0,0,0],
           [0,0,0,0],
           [0,0,0,0])
print("Matriz 3 x 4")

for l in range(3):
    for c in range(4):
        print(f'[{matriz4[l][c]:^5}]',end='')
    print()

matriz5 = ([0,0],
           [0,0],
           [0,0],
           [0,0],
           [0,0])
print('Matriz 2 x 5')

for l in range(5):
    for c in range(2):
        print(f'{matriz5[l][c]:^5}', end='')
    print()
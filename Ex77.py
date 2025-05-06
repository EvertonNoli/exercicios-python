palavra = ('learn', 'cat', 'programation', 'dog', 'shark', 'wolf', 'zebra', 'computer', 'study', 'food')

for c in palavra:
    print(f'\nNa palavra {c} temos: ', end= ' ')
    for l in c:
        if l in 'aeiocu':
            print(l, end='')


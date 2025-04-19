n=int(input('Digite um valor:'))
fat=1

for c in range(1,n+1):
    print(f'{c}', end='')
    if c < n:
        print(' x ', end='')
    else:
        print(' = ', end='')
    fat*=c
    c-=1

print(f'{fat}')
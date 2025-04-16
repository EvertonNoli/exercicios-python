n=int(input('Digite um valor:'))
res=1

for i in range(n,1,-1):
    res*=i
print(f'{n}!={res}')
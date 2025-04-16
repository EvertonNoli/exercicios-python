base=int(input('Valor da base:'))
expoente=int(input('Valor do expoente:'))
res=1

for i in range(1,expoente+1):
    res*=base
print(res)
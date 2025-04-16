n=int(input('Digite um número:'))
ePrimo=0

for i in range(1,n+1):
    if n%i==0:
        ePrimo+=1

if(ePrimo==2):
    print('Número primo!')
else:
    print('Número não primo!')

numero=int(input('Digite um número:'))
div=primo=0


for i in range(1,numero+1):
    if(numero%i==0):
        primo+=1

if(primo==2):
    print('Número primo!')
else:
    print('Número não primo!')

for i in range(1,numero+1):
    if(numero%i==0):
        div+=1

print(f'O número {numero} tem {div} divisores!')
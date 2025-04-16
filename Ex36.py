#for i in range(0,51):
#    if(i%2==0):
#        print(i)

n1=int(input('Primeiro valor:'))
n2=int(input('Segundo valor:'))
soma=0

for i in range(n1,n2+1):
    print(i)
    soma+=i
print(f'A soma dos números entre {n1} e {n2} é igual á {soma}')
print('-'*10)
print('Sequência de Fibonacci')
print('-'*10)
n=int(input('Quantos termos deseja mostrar?'))
t1 = 0
t2 = 1
print(f'{t1}, {t2} ,',end=' ')
cont=3

for cont in range(cont,n+1):
    t3=t1+t2
    print(f'{t3}, ',end=' ')
    t1=t2
    t2=t3
    cont+=1


print('FIM')
import math

x1=x2=0

print('='*30)
print('EQUAÇÃO DE BHASKARA')
print('='*30)

a=int(input('Valor de A:'))
b=int(input('Valor de B:'))
c=int(input('Valor de C:'))

delta=(b**2)-4*a*c

if a==0:
    print('O valor de A deve ser diferente de zero!')
elif delta<0:
    print('Delta negativo!Sem raízes reais!')
else:
    x1=((-b+math.sqrt(delta))/(2*a))
    x2=((-b-math.sqrt(delta))/(2*a))

print(f'Valor do delta: {delta}')
print(f'Raízes: {x1:.2f}, {x2:.2f}')

valores = []
pares = []
impares = []
n = None
cont = 0

while cont < 7:
    n = input('Digite um valor: ')
    if n.isnumeric():
        c = int(n)
        valores.append(c)
        cont+=1
        if(c%2==0):
            pares.append(c)
        else:
            impares.append(c)
    else:
        print('Digite um valor inteiro')

valores.sort()
print(f'Valores digitados: {valores}')
pares.sort()
print(f'Valores pares digitados: {pares}')
impares.sort()
print(f'Valores ímpares digitados: {impares}')
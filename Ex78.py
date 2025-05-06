num = []
pares = []
impares = []
soma = contPares = contImpares = media = 0

for c in range(0, 5):
    n = int(input('Digite um número: '))
    num.append(n)
    if n%2==0:
        pares.append(n)
        contPares +=1
    else:
        impares.append(n)
        contImpares +=1

    soma = sum(num)
    media = soma/5

    if c == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f'Lista original: {num}')
print(f'O maior valor digitado foi {maior} e ele está na posição {num.index(maior)}')
print(f'O menor valor digitado foi {menor} e ele está na posição {num.index(menor)}')
print(f'Valores em ordem crescente: ', end = '')
num.sort()
print(num)
print(f'Valores em ordem decrescente: ', end='')
num.sort(reverse=True)
print(num)
print(f'Soma dos valores digitados: {soma}')
print(f'Média dos valores digitados: {media:.2f}')
print(f'Números pares: {pares}, total de {contPares} valores')
print(f'Números ímpares: {impares}, total de {contImpares} valores')

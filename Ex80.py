num = []
cont=0
n = None

while cont < 5:
    entrada = input('Digite um valor:')
    if entrada.isnumeric():
        n=int(entrada)
        if n not in num:
            num.append(n)
            cont+=1
        else:
            print('Valor já digitado, tente novamente!')
    else:
        print('Digite um número inteiro!')

print(f'Você digitou: {num}')
num.sort()
print(f'Lista dos valores em ordem crescente: {num}')
num.sort(reverse=True)
print(f'Lista dos valores em ordem decrescente: {num}')

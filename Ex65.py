cont=media=soma=0
maior = menor = None


while True:
    n = int(input('Digite um número:'))
    soma+=n
    cont += 1
    media = soma / cont
    if maior is None or n>maior:
        maior = n
    if menor is None or n<menor:
        menor = n
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if pergunta=='N':
        break

print(f'Foram digitados {cont} números')
print(f'A média entre os números é {media:.2f}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
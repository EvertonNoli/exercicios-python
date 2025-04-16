valor=int(input('Exibir a tabuada do:'))
inicio=int(input('Começar por:'))
fim=int(input('Terminar em:'))


if (inicio<fim):
    print(f'Vamos exibir a tabuada do {valor} começando em {inicio} e terminando em {fim}')
    for i in range(inicio,fim+1):
        print(f'{valor} X {i} = {valor*i}')
        i+=1
elif(inicio>fim):
    print(f'Vamos exibir a tabuada do {valor} começando em {inicio} e terminando em {fim}')
    for i in range(inicio, fim-1, -1):
        print(f'{valor} X {i} = {valor*i}')
        i-=1
else:
    print('Início e fim devem ser diferentes!')



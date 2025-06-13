def apresentacao():
    print('-='*10)
    print('Contagem de 0 a 10 de 1 em 1')
    for c in range(0,11):
        print(c, end=' ')

    print('\n' + '-='*10)  # \n quebra a linha antes da próxima parte
    print('Contagem de 0 a 10 de 2 em 2')
    for c in range(0,11,2):
        print(c, end=' ')


def contador():
    print('\n'+'-='*10)
    print('Agora é a sua vez!')
    inicio = int(input('Início: '))
    final = int(input('Fim: '))
    passo = int(input('Passo: '))

    if passo == 0:
        passo = 1

    if inicio<final:
        for c in range(inicio, final+1, abs(passo)):
            print(c, end=' ')

    if inicio>final:
        for c in range(inicio, final+1, -abs(passo)):
            print(c, end=' ')

#programa principal
apresentacao()
contador()
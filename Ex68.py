from random import randint

resultado = vitorias = derrotas = 0

while True:
    print('-=' * 10)
    print('VAMOS JOGAR PAR OU ÍMPAR!')
    usuario = int(input('Digite um valor:'))
    if usuario < 0:
        break
    elif usuario>10:
        print('Digite um valor menor do que 10!')
    else:
        pergunta = ' '
        while pergunta not in 'PI':
            pergunta = str(input('Você escolhe par ou ímpar?[P/I]')).upper().strip()[0]
        computador = randint(1,10)
        resultado = computador+usuario
        if resultado%2==0:
            print(f'Você jogou {usuario} e o computador {computador}! O resultado foi {resultado}! Deu par!')
            print('-'*10)
        else:
            print(f'Você jogou {usuario} e o computador {computador}! O resultado foi {resultado}! Deu ímpar!')
            print('-' * 10)
        if pergunta == 'I' and resultado%2==0:
            print('VOCÊ PERDEU!')
            derrotas+=1
        elif pergunta =='I' and resultado%2!=0:
            print('VOCÊ VENCEU!')
            vitorias+=1
        elif pergunta == 'P' and resultado%2==0:
            print('VOCÊ VENCEU!')
            vitorias+=1
        else:
            print('VOCÊ PERDEU!')
            derrotas+=1


print(f'Você venceu {vitorias} vezes e o computador {derrotas} vezes')

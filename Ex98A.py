from time import sleep

def menu():

    print('-='*10)
    print('0 - Encerrar programa')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Exponenciação')
    return (int(input('Escolha uma opção:')))

def adicao():
    n1 = float(input('Primeiro valor:'))
    n2 = float(input('Segundo valor:'))
    print(f'{n1} + {n2} = {n1+n2:.2f}')

def subtracao():
    n1 = float(input('Primeiro valor:'))
    n2 = float(input('Segundo valor:'))
    print(f'{n1} - {n2} = {n1-n2:.2f}')

def multiplicacao():
    n1 = float(input('Primeiro valor:'))
    n2 = float(input('Segundo valor:'))
    print(f'{n1} x {n2} = {n1*n2:.2f}')

def divisao():
    n1 = float(input('Primeiro valor:'))
    n2 = float(input('Segundo valor:'))
    print(f'{n1} / {n2} = {n1/n2:.2f}')

def potenciacao():
    n1 = float(input('Primeiro valor:'))
    n2 = float(input('Segundo valor:'))
    print(f'{n1} ^ {n2} = {n1**n2:.2f}')

#programa principal
while True:
    opc = menu()

    if opc == 0:
        print('Encerrando o programa')
        sleep(1)
        print('Programa encerrado')
        break

    elif opc == 1:
        adicao()

    elif opc == 2:
        subtracao()

    elif opc == 3:
        multiplicacao()

    elif opc == 4:
        divisao()

    elif opc == 5:
        potenciacao()

    else:
        print('Opção inválida!Tente novamente!')

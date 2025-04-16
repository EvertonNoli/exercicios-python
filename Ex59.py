n1=int(input('Digite um valor:'))
n2=int(input('Digite um valor:'))
opc=0
maior=0
while opc !=5:

    print('''
          [1]Somar
          [2]Multiplicar
          [3]Mostrar o maior
          [4]Novos números
          [5]Encerrar o programa
          -------------''')
    opc=int(input('Escolha uma opcão:'))

    if opc==5:
        break

    elif opc==1:
        print(f'{n1} + {n2} = {n1+n2}')

    elif opc==2:
        print(f'{n1} x {n2} = {n1*n2}')

    elif opc==3:
        if(n1>n2):
            maior=n1
        elif(n2>n1):
            maior=n2
        else:
            maior=n1
        print(f'O maior número digitado foi {maior}')

    elif opc==4:
        n1=int(input('Digite um novo valor:'))
        n2=int(input('Digite um novo valor:'))






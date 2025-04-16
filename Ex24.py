opc=soma=subt=0
div=mult=1

n1=float(input('Primeiro valor:'))
n2=float(input('Segundo valor:'))
print('='*40)
print('''1-Adição
2-Subtração
3-Divisão
4-Multiplicação''')
opc=int(input('Escolha uma opção:'))
print('='*40)
if(opc==1):
    soma=n1+n2
    print(f'{n1} + {n2} = {soma}')
    if(soma%2==0):
        print(f'O número {soma:.2f} é par!')
    else:
        print(f'O número {soma:.2f} é ímpar!')
    if(soma>0):
        print(f'O número {soma:.2f} é positivo!')
    else:
        print(f'O número {soma:.2f} é negativo!')
    if(soma.is_integer()==True):
        print(f'O número {soma:.2f} é inteiro!')
    else:
        print(f'O número {soma:.2f} não é inteiro!')

elif(opc==2):
    subt=n1-n2
    print(f'{n1} - {n2} = {subt}')
    if(subt%2==0):
        print(f'O número {subt:.2f} é par!')
    else:
        print(f'O número {subt:.2f} é ímpar!')
    if(subt>0):
        print(f'O número {subt:.2f} é positivo!')
    else:
        print(f'O número {subt:.2f} é negativo!')
    if(subt.is_integer()==True):
        print(f'O número {subt:.2f} é inteiro!')
    else:
        print(f'O número {subt:.2f} não é inteiro!')

elif(opc==3):
    if(n1==0)or(n2==0):
        print('Erro!Não existe divisão por zero!')
    else:
        div=n1/n2
        print(f'{n1} / {n2} = {div:.2f}')
    if(div%2==0):
        print(f'O número {div:.2f} é par!')
    else:
        print(f'O número {div:.2f} é ímpar!')
    if(div>0):
        print(f'O número {div:.2f} é positivo!')
    else:
        print(f'O número {div:.2f} é negativo!')
    if(div.is_integer()==True):
        print(f'O número {div:.2f} é inteiro!')
    else:
        print(f'O número {div:.2f} não é inteiro!')

elif(opc==4):
    mult=n1*n2
    print(f'{n1} x {n2} = {mult}')
    if(mult%2==0):
        print(f'O número {mult:.2f} é par!')
    else:
        print(f'O número {mult:.2f} é ímpar!')
    if(mult>0):
        print(f'O número {mult:.2f} é positivo!')
    else:
        print(f'O número {mult:.2f} é negativo!')
    if(mult.is_integer()==True):
        print(f'O número {mult:.2f} é inteiro!')
    else:
        print(f'O número {mult:.2f} não é inteiro!')
else:
    print('ERRO!Favor inserir uma opção válida!')

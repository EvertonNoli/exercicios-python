#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

sexo=' '
ideal=0
while sexo not in 'MF':
    sexo=str(input('Digite o sexo:[M/F]')).upper().strip()[0]
    altura=float(input('Digite a altura:'))

    if(sexo=='M'):
       ideal=(72.7*altura)-58
       print(f'Seu peso ideal é de {ideal:.2f} KG')
    elif(sexo=='F'):
        ideal=(62.1*altura)-44.7
        print(f'Seu peso ideal é de {ideal:.2f} KG')
    else:
        print('Erro!Valores inválidos!')


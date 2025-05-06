total18=contM=contF=0


while True:
    print('-'*10)
    print('CADASTRE UMA PESSOA')
    print('-'*10)

    sexo = ' '
    idade = int(input('Idade:'))
    if idade>=18:
        total18+=1
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).strip()[0].upper()
        if sexo == 'M':
            contM+=1
        elif sexo=='F' and idade>20:
            contF+=1

    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar?[S/N] ')).strip()[0].upper()
    if pergunta == 'N':
        break


print(f'Pessoas com mais de 18 anos: {total18}')
print(f'Homens: {contM}')
print(f'Mulheres com mais de 20 anos: {contF}')
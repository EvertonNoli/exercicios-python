cadastro=int(input('Quantas pessoas serão cadastradas?'))
total=cont=0
media=1

while (cont<cadastro):
    idade=int(input('Digite a idade:'))
    if(idade>=0):
        total = total + idade
        cont += 1
    else:
        print('Digite um valor maior do que zero!')

media=total/cont
print(f'Foram cadastradas {cont} pessoas e a média de idade é de {media:.2f} anos')

if(media>=0) and(media<=25.6):
    print('O grupo é de jovens!')
elif(media>25.6 and media<=60):
    print('O grupo é de adultos!')
else:
    print('O grupo é de idosos!')
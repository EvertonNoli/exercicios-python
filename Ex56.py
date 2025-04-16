somaIdade=0
mediaIdade= 0
maiorIdadeHomem = 0
homemVelho = ' '
totMulher20 = 0

for c in range(1,5):
    print('-----{}° PESSOA -----'.format(c))
    nome=str(input('Nome:')).upper().strip()
    sexo = str(input('Sexo [M/F]:')).strip()
    idade = int(input('Idade:'))
    somaIdade += idade

    if c == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        homemVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        homemVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20+=1

mediaIdade = somaIdade/4
print(f'A média de idade do grupo é de {mediaIdade}')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {homemVelho}')
print(f'Ao todo são {totMulher20} mulheres com menos de 20 anos')
#faça um programa que cadastre funcionários
#nome, salário e idade
#exiba o nome do maior e menor e salário
#faça o mesmo com o mais velho e mais novo

rasc = []
princ = []
maior = menor = velho = novo = 0

while True:

    rasc.append(str(input('Nome:')))
    rasc.append(float(input('Salário:')))
    rasc.append(int(input('Idade:')))
    if len(princ)==0:
        maior = menor = rasc[1]
    else:
        if rasc[1]>maior:
            maior = rasc[1]
        if rasc[1]<menor:
            menor = rasc[1]
    if len(princ)==0:
        velho = novo = rasc[2]
    else:
        if rasc[2]>velho:
            velho = rasc[2]
        if rasc[2]<novo:
            novo = rasc[2]
    princ.append(rasc[:])
    rasc.clear()


    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja cadastrar outra pessoa? [S/N]')).upper().strip()
    if opc == 'N':
        break

print('='*20)
print('Listagem de Funcionários')
print('='*20)
print(f"{'NOME:':<15} {'SALÁRIO:':<12} {'IDADE:':<10}")
for pessoa in princ:
    print(f"{pessoa[0]:<15} R${pessoa[1]:<10.2f} {pessoa[2]:<10}")
print('='*20)

for element in princ:
    if element[1]==maior:
        print(f'O maior salário é de R${maior} do funcionário {element[0]}')
for element in princ:
    if element[1]==menor:
        print(f'O menor salário é de R${menor} do funcionário {element[0]}')
for element in princ:
    if element[2]==velho:
        print(f'O funcionário mais velho é o {element[0]} com {velho} anos')
for element in princ:
    if element[2]==novo:
        print(f'O funcionário mais jovem é o {element[0]} com {novo} anos')

soma = 0
media = 1
for element in princ:
    soma += element[1]
media=soma/len(princ)

print(f'Média salarial: R${media:.2f}')

soma=0

for element in princ:
    soma+=element[2]
media=soma/len(princ)

print(f'Média de idade: {media:.2f}')
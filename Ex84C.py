#faça um programa pra cadastrar carros
#cadastre por marca ou modelo
#mostre o mais caro e o mais barato

princ = []
rasc = []
caro = barato = []

while True:

    rasc.append(str(input('Marca do Veículo:')))
    rasc.append(float(input('Preço do Veículo: R$')))
    if len(princ)==0:
        caro = barato = rasc[1]
    else:
        if rasc[1]>caro:
            caro = rasc[1]
        if rasc[1]<barato:
            barato = rasc[1]
    princ.append(rasc[:])
    rasc.clear()


    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja fazer outro cadastro?[S/N]')).strip().upper()
    if opc == 'N':
        break

print('='*20)
print(f'Listagem de veículos: ')
print('='*20)
print(f"{'MARCA:':<15} {'PREÇO:':<10}")
for veiculo in princ:
    print(f"{veiculo[0]:<15} {veiculo[1]:<10}")
for element in princ:
    if element[1]==caro:
        print(f'O carro mais caro é o {element[0]} custando R${caro}')
for element in princ:
    if element[1]==barato:
        print(f'O carro mais barato é o {element[0]} custando R${barato}')

soma = 0
media = 1

for veiculo in princ:
    soma+=veiculo[1]
media = soma/len(princ)

print(f'Media de vendas: R${media:.2f}')
print(f'Soma de vendas: R${soma}')
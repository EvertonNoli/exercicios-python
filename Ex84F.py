#cadastre x produtos
#coloque nome/tipo e preço
#produto mais caro e mais barato
#soma de tudo que foi vendido $$
#quantos cadernos foram vendidos

rasc = []
prod = []
menor = maior = cont_caderno = 0

while True:

    nome = str(input('Tipo: ')).upper().strip()
    rasc.append(nome)
    if nome == 'CADERNO':
        cont_caderno+=1
    rasc.append(float(input('Preço: R$')))
    if len(prod)==0:
        maior = menor = rasc[1]
    else:
        if rasc[1]>maior:
            maior = rasc[1]
        if rasc[1]<menor:
            menor = rasc[1]
    prod.append(rasc[:])
    rasc.clear()

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja cadastrar um novo produto?[S/N]')).strip().upper()
    if opc == 'N':
        break

print('='*10)
print('Listagem de produtos')
print('='*10)
print(f"{'PRODUTO:' :<15}{'PREÇO: R$':<12}")
for p in prod:
    print(f"{p[0]:<15} {p[1]:<12.2f}")
print('='*10)
print('Outras informações')
print('='*10)
print('Produto mais caro e mais barato')
for p in prod:
    if p[1]==maior:
        print(f'O produto mais caro é {p[0]} custando R${maior}')
for p in prod:
    if p[1]==menor:
        print(f'O produto mais barato é {p[0]} custando R${menor}')
print('='*10)
print('Soma e média das vendas')
soma = 0
media = 1
for p in prod:
    soma+=p[1]
media = soma/len(prod)
print(f'A média de vendas é de R${media :.2f}')
print(f'A soma das vendas é de R${soma :.2f}')
print('='*10)
print(f'Total de cadernos vendidos: {cont_caderno}')
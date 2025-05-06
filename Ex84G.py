#cadastro de animes
#nome do mais velho e mais novo
#média de idade
#soma das idades
#qtde de gatos e cães

rasc = []
princ = []
contGato = contCao = velho = novo = 0


while True:

    nome = str(input('Nome do animal:')).upper().strip()
    rasc.append(nome)
    especie = str(input('Espécie do animal:')).upper().strip()
    rasc.append(especie)
    if especie == 'GATO':
        contGato +=1
    elif especie == 'CACHORRO' or especie == 'CÃO':
        contCao +=1
    rasc.append(int(input('Idade do animal:')))
    if len(princ)==0:
        velho = novo = rasc[2]
    else:
        if rasc[2]>velho:
            velho=rasc[2]
        if rasc[2]<novo:
            novo=rasc[2]
    princ.append(rasc[:])
    rasc.clear()


    opc = ' '
    while opc  not in 'SN':
        opc = str(input('Deseja fazer outro cadastro?[S/N]')).upper().strip()
    if opc == 'N':
        break

print('='*10)
print('Cadastro de Animais')
print('='*10)
print(f"{'NOME':<15} {'ESPÉCIE':<12} {'IDADE':<10}")
for a in princ:
    print(f"{a[0]:<15} {a[1]:<12} {a[2]:<10}")
print('='*10)
print('Contadores')
print('='*10)
print(f'Foram cadastrados {contGato} gatos e {contCao} cachorros')
print('='*10)
for a in princ:
    if a[2]==velho:
        print(f'O animal mais velho é {a[0]} com {velho} anos. Na espécie {a[1]}')
for a in princ:
    if a[2]==novo:
        print(f'O animais mais novo é {a[0]} com {novo} anos. Na espécie {a[1]}')
print('='*10)
print(f'Foram cadastrados {len(princ)} animais')
print(f'='*10)
print('Dados sobre idade')

soma = 0
media = 1

for a in princ:
    soma+=a[2]
media = soma/len(princ)

print(f'A média de idade dos animais cadastrados é de {media:.2f} anos')
print(f'A soma das idades dos animais cadastrados é de {soma:.2f} anos')
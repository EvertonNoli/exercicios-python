#cadastre x pessoas
#pergunte a idade
#exiba o mais velho
#exiba o mais nov

princ = []
rasc = []
velho = novo = 0


while True:

    rasc.append(str(input('Nome:')))
    rasc.append(int(input('Idade:')))
    if len(princ)==0:
        velho = novo = rasc[1]
    else:
        if rasc[1]>velho:
            velho = rasc[1]
        if rasc[1]<novo:
            novo = rasc[1]
    princ.append(rasc[:])
    rasc.clear()

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja cadastrar outra pessoa?[S/N]')).upper().strip()
    if opc == 'N':
        break


print(princ)
for element in princ:
    if element[1]==velho:
        print(f'A pessoa mais velha do grupo é {element[0]} com {velho} anos')
for element in princ:
    if element[1]==novo:
        print(f'A pessoa mais jovem do grupo é {element[0]} com {novo} anos')
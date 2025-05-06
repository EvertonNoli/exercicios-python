num = []

while True:
    n=int(input('Digite um valor:'))
    if n in num:
        print('Valor já adicionado!')
    else:
        num.append(n)

    opc = ' '
    while opc not in 'SN':
        opc = str(input("Deseja continuar?[S/N]")).upper().strip()
    if opc == 'N':
        break

print(num)
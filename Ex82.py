valores = []
pares = []
impares = []

while True:
    entrada = input('Digite um valor: ')
    if entrada.isnumeric():
        n = int(entrada)
        valores.append(n)
        if n%2==0:
            pares.append(n)
        else:
            impares.append(n)
    else:
        print('Digite um valor inteiro!')

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar?[S/N]')).strip().upper()
    if opc == 'N':
        break


print(valores)
print(impares)
print(pares)
num = []
n = cont = cont5 = 0


while True:
    entrada = input('Digite um valor: ')
    if entrada.isnumeric():
        n=int(entrada)
        num.append(n)
        cont+=1
    else:
        print('Digite um valor inteiro!')

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N]')).upper().strip()
    if opc == 'N':
        break

for c in num:
    if c == 5:
        cont5+=1
    pos=[i for i, v in enumerate(num) if v == 5]


print(f'Foram digitados {cont} valores')
print(num)
num.sort(reverse=True)
print(f'Lista na ordem decrescente {num}')
if cont5 >0:
    print(f'O valor 5 aparece {cont5}')
else:
    print('O valor 5 não está na lista!')

print(f'O valor 5 aparece na(s) {pos}ª posição(ões)')
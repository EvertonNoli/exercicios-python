pessoas = []
dado = []
maior = menor = 0

while True:

    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1]>maior:
            maior = dado[1]
        if dado[1]<menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja cadastrar outra pessoa?[S/N]')).strip().upper()
    if opc == 'N':
        break
print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior} KG. Peso de ', end='')
for p in pessoas:
    if p[1]==maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor} KG. Peso de ', end='')
for p in pessoas:
    if p[1]==menor:
        print(f'{p[0]}')
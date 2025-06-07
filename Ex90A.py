cadastro = {}

while True:

    cadastro['nome'] = str(input('Nome do animal:')).upper()
    cadastro['especie']=str(input('Espécie do animal:')).upper().strip()
    cadastro['idade']=int(input('Idade do animal:'))

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja realizar outro cadastro?[S/N]')).upper().strip()
    if opc == 'N':
        break

print('-'*20)
print('Cadastro de animais')
for k, v in cadastro.items():
    print(f'{k}:{v}')

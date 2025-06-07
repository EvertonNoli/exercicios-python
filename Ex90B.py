cadastro = {}
lista = []

while True:

    cadastro['nome'] = str(input('Nome do jogador:')).upper()
    cadastro['salario'] = float(input('Salário do jogador:'))
    cadastro['idade'] = int(input('Idade do jogador:'))
    cadastro['time'] = str(input('Time do jogador:')).upper()

    lista.append(cadastro.copy())

    mais_novo = min(lista, key = lambda cadastro:cadastro['idade'])
    maior_salario = max(lista, key = lambda cadastro:cadastro['salario'])

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja realizar outro cadastro?[S/N]')).upper().strip()
    if opc == 'N':
        break

print('-'*30)
print('Cadastro de jogador')

for k, v in cadastro.items():
    print(f'{k}: {v}')


print(maior_salario)
print(mais_novo)
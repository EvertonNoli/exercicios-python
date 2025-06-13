jogador = {}
registro = []

while True:
    jogador.clear()
    jogador['nome']=str(input('Nome: ')).upper()
    partidas = []
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'{" "*8}Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    registro.append(jogador.copy())

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja fazer outro cadastro? [S/N]')).strip().upper()[0].replace(" ", '')
    if opc == 'N':
        break


print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(registro):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca==999:
        break
    if busca >= len(registro):
        print(f'ERRO! Não existe jogador no código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {registro[busca]["nome"]}: ')
        for i, g in enumerate(registro[busca]["gols"]):
            print(f'{" "*7}No jogo {i} fez {g} gols')
    print('-'*40)

print('VOLTE SEMPRE')

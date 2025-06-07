jogador = {
    'nome':str(input('Nome do jogador: ')).upper()
}
partidas = int(input('Quantas partidas o jogador disputou? '))

gols = []

for i in range (partidas):
    gol = int(input(f'Gols na partida {i+1}:'))
    gols.append(gol)


for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print(f"O jogador {jogador['nome']} marcou {sum(gols)} gols")
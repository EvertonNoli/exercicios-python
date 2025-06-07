from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jogador1':randint(1,6),
    'jogador2':randint(1,6),
    'jogador3':randint(1,6),
    'jogador4':randint(1,6)
}

ranking=()

for jogador, valor in jogo.items():
    print(f'O {jogador} tirou o valor {valor}')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} que tirou {v[1]}')
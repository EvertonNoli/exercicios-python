from random import randint
from time import sleep

palpite = []
jogos = []
n = 0

print('-'*20)
print('SORTEIO MEGA SENA')
print('-'*20)
perg = int(input('Quantos jogos deseja sortear?'))

for c in range(0,perg):
    while len(palpite) < 6:
        n = randint(1,60)
        if n not in palpite:
            palpite.append(n)
            palpite.sort()

    jogos.append(palpite[:])
    palpite.clear()

for c in range(0,perg):
   print(f'JOGO {c + 1}: {jogos[c]}')
   sleep(1)
print('-='*20)
print('Boa sorte!')
#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato

eleitores=int(input('Quantidade de eleitores:'))
totA=totB=totC=0

for i in range(eleitores):
    candidato=' '
    while candidato not in 'ABC':
        candidato=str(input('Escolha o seu candidato:A/B/C ')).upper().strip()[0]

        if(candidato=='A'):
            totA+=1
        elif(candidato=='B'):
            totB+=1
        elif(candidato=='C'):
            totC+=1

if(totA>totB) and (totA>totC):
    print(f'O candidato eleito foi o candidato A com {totA} votos')
elif(totB>totA) and (totB>totC):
    print(f'O candidato eleito foi o candidato B com {totB} votos')
elif(totC>totA) and (totC>totB):
    print(f'O candidato eleito foi o candidato C com {totC} votos')
else:
    print('Os candidatos tiveram quantidade igual de votos!')
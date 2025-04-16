while True:
    nome=str(input('Nome:'))
    altura=float(input('Altura:'))
    peso=float(input('Peso:'))

    maisAlto=maisBaixo=altura
    nomeAlto=nomeBaixo=nome
    maisPesado=maisMagro=peso
    nomePesado=nomeMagro=nome

    if(altura>maisAlto):
        maisAlto=altura
        nomeAlto=nome

    elif(altura<maisBaixo):
        maisBaixo=altura
        nomeBaixo=nome

    if(peso>maisPesado):
        maisPesado=peso
        nomePesado=nome

    elif(peso<maisMagro):
        maisMagro=peso
        nomeMagro=nome


    pergunta=' '
    while pergunta not in 'SN':
        pergunta=str(input('Deseja cadastrar outra pessoa?[S/N]')).upper().strip()[0]
    if(pergunta=='N'):
        break

print(f'O mais pesado é {nomePesado} com {maisPesado:.2f}KG')
print(f'O mais alto é {nomeAlto} com {maisAlto:.2f}M')
print(f'O mais magro é {nomeMagro} com {maisMagro:.2f}KG')
print(f'O mais alto é {nomeBaixo} com {maisBaixo:.2f}M')

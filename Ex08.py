cont=total=0
menor=preco=0
nomeMenor=' '

while (cont<3):
    produto = str(input('Nome do produto:'))
    preco = float(input('Preço:R$'))
    cont += 1
    menor=preco
    total+=1
    if(preco<menor):
        menor=preco
        nomeMenor=produto

print(f'O produto de menor valor é o(a) {nomeMenor} que custa:R${menor}')

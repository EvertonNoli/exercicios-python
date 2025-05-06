total = contP = cont1000 = 0
caro = None
barato = None
nome_caro = ''
nome_barato = ''

print('-'*10)
print('LOJA DO SUPER BARATO!')
print('-'*10)

while True:
    produto = str(input('Nome do produto: ')).upper()
    preco = float(input('Preço do produto: $ '))
    total+=preco
    contP+=1
    if preco>1000:
        cont1000+=1
    if caro is None or preco > caro:
        caro = preco
        nome_caro = produto
    if barato is None or preco < barato:
        barato = preco
        nome_barato = produto

    opc=' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N] ')).strip()[0].upper()
    if opc == 'N':
        break

print(f'Total da compra: ${total:.2f}')
print(f'Foram comprados {contP} ítens')
print(f'Foram comprados {cont1000} ítens mais caros do que $1000')
print(f'O produto mais caro é {nome_caro} custando ${caro:.2f} e o mais barato é {nome_barato} custando ${barato:.2f}')
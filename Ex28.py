pgto=' '
desc=total=0
print('='*30)
print('MENU DE OPÇÕES')
print('''1-Filé Duplo
2-Alcatra
3-Picanha''')
carne=int(input('Escolha uma opção:'))
print('='*30)
qtde=float(input('Quantidade em KG:'))
while pgto not in 'SN':
    pgto=str(input('Pagamento no cartão?[S/N]')).upper().strip()[0]
if(pgto=='N'):
    if(carne==1) and (qtde<=5):
        total=qtde*4.9
    elif(carne==1) and (qtde>5):
        total=qtde*5.8
    elif(carne==2) and (qtde<=5):
        total=qtde*5.9
    elif(carne==2) and (qtde>5):
        total=qtde*6.8
    elif(carne==3) and (qtde<=5):
        total=qtde*6.9
    elif(carne==3) and (qtde>5):
        total=qtde*7.8
else:
    if (carne == 1) and (qtde <= 5):
        total = qtde * 4.9
        total = total-(total*(5/100))
        desc = total*(5/100)
    elif (carne == 1) and (qtde > 5):
        total = qtde * 5.8 - (5/100)
        total = total - (total * (5 / 100))
        desc = total * (5 / 100)
    elif (carne == 2) and (qtde <= 5):
        total = qtde * 5.9 - (5/100)
        total = total - (total * (5 / 100))
        desc = total * (5 / 100)
    elif (carne == 2) and (qtde > 5):
        total = qtde * 6.8 - (5/100)
        total = total - (total * (5 / 100))
        desc = total * (5 / 100)
    elif (carne == 3) and (qtde <= 5):
        total = qtde * 6.9 - (5/100)
        total = total - (total * (5 / 100))
        desc = total * (5 / 100)
    elif (carne == 3) and (qtde > 5):
        total = qtde * 7.8 - (5/100)
        total = total - (total * (5 / 100))
        desc = total * (5 / 100)
print(f'Valor do desconto:R${desc:.2f}')

print(f'Total a pagar:R${total:.2f}')

total = litro = desconto = 0
combustivel = ' '

while combustivel not in 'AG':
    combustivel = str(input('Álcool ou Gasolina?[A/G]')).upper().strip()[0]
if (combustivel == 'A'):
    litro = int(input('Total de litros:L'))
    total = litro * 1.9
    if(litro<=20):
        desconto=total-(total*(3/100))
    elif(litro>20):
        desconto=total-(total*(5/100))
    print(f'Total sem desconto:R${total:.2f}')
    print(f'Total com desconto:R${desconto:.2f}')

else:
    litro = int(input('Total de litros:L'))
    total = litro * 2.5
    if(litro<=20):
        desconto=total-(total*(4/100))
    else:
        desconto=total-(total*(6/100))
    print(f'Total sem desconto:R${total:.2f}')
    print(f'Total com desconto:R${desconto:.2f}')

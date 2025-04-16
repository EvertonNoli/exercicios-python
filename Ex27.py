fruta=' '
kilo=total=0

while fruta not in 'MB':
    fruta=str(input('Maçã ou Banana?[M/B]')).upper().strip()[0]
if(fruta=='M'):
    kilo=float(input('Quantidade em KG:'))
    if(kilo<=5):
        total=kilo*1.8
    else:
        total=kilo*1.5
        if(kilo>8) and (total>25):
            total=total-(total*(25/100))
elif(fruta=='B'):
    kilo=float(input('Quantidade em KG:'))
    if(kilo<=5):
        total=kilo*2.2
    else:
        total=kilo*2.50
        if(kilo>8) and (total>25):
            total=total-(total*(25/100))
print(f'Total a pagar:R${total:.2f}')
peso=float(input('Peso do pescado:KG '))
taxa=0

if(peso<=50):
    print(f'Você pescou {peso} KG e não terá taxa!')
else:
    taxa=(peso-50)*4
    print(f'Você pescou {peso} KG e a taxa é de R${taxa:.2f}')
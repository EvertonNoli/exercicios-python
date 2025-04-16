#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
#e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
# ou em galões de 3,6 litros, que custam R$ 25,00.
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor.
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area=float(input('Área em metro:'))
litro=area/6
lata=litro/18
galao=litro/3.6
print(f'Serão gastos {litro:.2f} litros de tinta')
print(f'Serão necessárias {lata:.2f} latas de tinta')
print(f'Serão necessários {galao:.2f} galões de tinta')

preco=1
opc=0

while (opc!=1 and opc!=2):
    opc=int(input('''Como deseja efetuar a compra:
    1-Latas de 18 L
    2-Galões de 3.6 litros\n'''))
    if(opc==1):
        preco=lata*80
        print(f'Total a pagar:R${preco:.2f}')
    elif(opc==2):
        preco=galao*25
        print(f'Total a pagar:R${preco:.2f}')
    else:
        print('ERRO! INSIRA UM VALOR VÁLIDO!')



#tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
#quantas latas
#valor
area=float(input('Área em metro: '))
litro=area/3
lata=litro/18
preco=lata*80

print(f'Serão gastos {litro:.2f} litro(s) de tinta')
print(f'Serão gastas {lata:.2f} lata(s) de tinta')
print(f'Total a pagar:R${preco:.2f}')
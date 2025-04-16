ir=0

hora=int(input('Total de horas trabalhadas:'))
valor=float(input('Valor da hora:R$'))
salarioBruto=valor*hora
sindicato=salarioBruto-(salarioBruto*(3/100))
sindDesc=salarioBruto*(3/100)
inss=salarioBruto-(salarioBruto*(10/100))
inssDesc=salarioBruto*10/100
fgts=salarioBruto-(salarioBruto*(11/100))
fgtsDesc=salarioBruto*(11/100)

if salarioBruto>=900 and salarioBruto<1500:
    ir=(salarioBruto*(5/100))
elif salarioBruto>=1500 and salarioBruto<2500:
    ir=(salarioBruto*(10/100))
elif salarioBruto>=2500:
    ir=salarioBruto*(20/100)

salarioliquido=salarioBruto-(ir+fgtsDesc+sindDesc+inssDesc)


print(f'Salário Bruto:R${salarioBruto:.2f}')
print(f'Desconto sindicato:R${sindicato:.2f}')
print(f'-Sindicato(3%):R${sindDesc:.2f}')
print(f'Desconto INSS:R${inss:.2f}')
print(f'-INSS(10%):R${inssDesc:.2f}')
print(f'Desconto FGTS:R${fgts:.2f}')
print(f'-FGTS(11%):R${fgtsDesc:.2f}')
print(f'Salário liquido:R${salarioliquido:.2f}')

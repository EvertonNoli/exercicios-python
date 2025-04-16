salario=float(input('Salário:R$'))
aumento=percentual=0

if salario<280:
    print("Salário inválido!Aumento não concedido!")
else:
    if salario>=280 and salario<700:
        aumento=salario+(salario*(20/100))
        percentual=20
    elif salario>=700 and salario<1500:
        aumento=salario+(salario*(15/100))
        percentual=15
    elif salario>=1500:
        aumento=salario+(salario*(5/100))
        percentual=5
    print(f'''Salário anterior:R${salario}
    Percentual de aumento:{percentual}%
    Salário com aumento:R${aumento}''')

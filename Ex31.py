nome=sexo=estado=' '
idade=0
salario=0.0

while True:
    nome=str(input('Nome:'))
    idade=int(input('Idade:'))
    salario=float(input('Salário:R$'))
    sexo=str(input('Sexo:[F/M]')).strip().upper()[0]
    estado=str(input('Estado Civil:[S/C/V/D]')).strip().upper()[0]


    if(len(nome)<=3) or (idade<0 or idade>=150) or salario<=0 or sexo not in 'MF' or estado not in 'SCVD':
        print('Informações equivocadas!Comece novamente!')
    else:
        break
print(f'Nome:{nome}')
print(f'Idade:{idade}')
print(f'Salário:R${salario}')
print(f'Sexo:{sexo}')
print(f'Estado Civil:{estado}')
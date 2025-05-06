print('='*10)
print('CAIXA ELETRÔNICO')
print('='*10)

valor = int(input('Valor a ser sacado: $'))
cedula = 50
totCed = 0

while True:
    if valor>=cedula:
        valor-=cedula
        totCed+=1
    else:
        if totCed > 0:
            print(f'Foram retiradas {totCed} de {cedula}')
            if cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 1
            totCed=0
            if valor == 0:
                break

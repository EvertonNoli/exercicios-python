cadastro = {}
carros = []
maisAntigo = maisCaro = 0

while True:

    cadastro['marca']=str(input('Marca do veículo:')).upper()
    cadastro['preco']=str(input('Preço do veículo:'))
    cadastro['ano']=str(input(('Ano do veículo:')))
    cadastro['cor']=str(input('Cor do veículo:')).upper()

    carros.append(cadastro.copy())

    maisAntigo = maisCaro = carros[0]
    for carro in carros[1:]:
        if carro['ano']< maisAntigo['ano']:
            maisAntigo = carro
        if carro['preco']<maisCaro['preco']:
            maisCaro = carro

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja realizar outro cadastro?[S/N]')).upper().strip()
    if opc == 'N':
        break


print('-='*30)
print('Cadastro de veículos')

for k, v in cadastro.items():
    print(f'{k}:{v}')


print(f"Carro mais antigo: {maisAntigo['marca']}({maisAntigo['ano']})")
print(f"Carro mais caro: {maisCaro['marca']} ({maisCaro['marca']})")

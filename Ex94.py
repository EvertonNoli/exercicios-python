pessoa = {}
registro = []
mulheres = []
maiorIdade = []
maiorMedia = []

while True:

    pessoa['nome']=str(input('Nome: ')).upper()
    pessoa['idade']=int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo=str(input('Sexo: [M/F]')).upper().strip()
        if sexo not in 'MF':
            print('Erro, favor utilize M ou F!')
    pessoa['sexo']=sexo
    registro.append(pessoa.copy())

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja fazer outro cadastro?[S/N]')).upper().strip()
    if opc == 'N':
        break

print('-='*30)
print('PESSOAS CADASTRADAS')
for p, pessoa in enumerate(registro, start=1):
    for k, v in pessoa.items():
        print(f'{k}: {v}')
    print('-'*20)

print(f'Foram cadastradas: {len(registro)} pessoas')

totalIdade = 0
for i in registro:
    totalIdade+=i['idade']
    media=totalIdade/len(registro)

print(f'A média de idade é igual a {media:.2f}')

for i in registro:
    if i['sexo']=='F':
        mulheres.append(i)
    if i['idade']>=18:
        maiorIdade.append(i)
    if i['idade']>media:
        maiorMedia.append(i)

print('-='*30)
print('Mulheres')
for p, pessoa in enumerate(mulheres, start=1):
    for k,v in pessoa.items():
        print(f'{k}: {v}')
print('-='*30)
print('Maiores de Idade')
for p, pessoa in enumerate(maiorIdade, start=1):
    for k,v in pessoa.items():
        print(f'{k}: {v}')
print('-='*30)
print('Idade acima da média')
for p, pessoa in enumerate(maiorMedia, start=1):
    for k,v in pessoa.items():
        print(f'{k}: {v}')
print('-='*30)

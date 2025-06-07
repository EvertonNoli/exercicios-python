boletim = {}

boletim['nome'] = str(input('Nome do aluno:'))
boletim['primeira nota'] = float(input(f'Digite a primeira nota do {boletim["nome"]}:'))
boletim['segunda nota'] = float(input(f'Digite a segunda nota do {boletim["nome"]}:'))
boletim['media'] = ((boletim["primeira nota"]+boletim["segunda nota"])/2)
if boletim['media']>=7:
    boletim['situacao']= 'Aprovado'
elif boletim['media']<7 and boletim['media']>=5:
    boletim['situacao'] = 'Recuperação'
else:
    boletim['situacao'] = 'Reprovado'

print('-='*30)
print(f'Média do(a) aluno(a) {boletim["nome"]}: {boletim["media"]:.2f}')
for k, v in boletim.items():
    print(f'{k} é igual a {v}')

aluno={
    'nome':str(input('Nome: ')).upper(),
    'p1':float(input('Primeira nota: ')),
    'p2':float(input('Segunda nota: ')),
    'p3':float(input('Terceira nota: '))
}

total=0
for chave, valor in aluno.items():
    if chave.startswith('p'):
        total+=valor

media=total/3

for k,v in aluno.items():
    print(f'{k}:{v}')

print(f'O(a) aluno(a) {aluno["nome"]} obteve um total de {total} pontos e média {media:.2f}')
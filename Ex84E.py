rasc = []
princ = []
maior = menor = 0


while True:

    rasc.append(str(input('Nome do aluno:')))
    rasc.append(float(input('Nota do aluno:')))
    if len(princ)==0:
        maior = menor = rasc[1]
    else:
        if rasc[1]>maior:
            maior = rasc[1]
        if rasc[1]<menor:
            menor = rasc[1]
    princ.append(rasc[:])
    rasc.clear()

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja fazer outro cadastro?[S/N]')).upper().strip()
    if opc == 'N':
        break

print('='*15)
print('Listagem de alunos')
print('='*15)
print(f"{'NOME:' :<15} {'NOTA:' :<15}")
for a in princ:
    print(f"{a[0]:<15} {a[1] :<12.2f}")
print('='*15)
print('Maior e Menor nota da turma')
for a in princ:
    if a[1]==maior:
        print(f'A maior nota da turma foi {maior} do(a) alun(a) {a[0]}')
for a in princ:
    if a[1]==menor:
        print(f'A menor nota da turma foi {menor} do(a) aluno(a) {a[0]}')
print('='*15)
print('Soma das notas e média da turma')
soma = 0
media = 1
for a in princ:
    soma+=a[1]
    media = soma/len(princ)

print(f'A soma das notas da turma foi {soma:.2f}')
print(f'A média da turma foi de {media:.2f}')
if media < 6:
    print(f'A turma ficou abaixo da média!')
else:
    print(f'A turma ficou acima da média!')
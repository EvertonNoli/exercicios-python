rasc = []
boletim = []

while True:

    rasc.append((str(input('Nome do aluno: '))).upper().strip())
    rasc.append(float(input('Primeira nota: ')))
    rasc.append(float(input('Segunda nota: ')))
    rasc.append(float((rasc[1]+rasc[2])/2))
    boletim.append(rasc[:])
    rasc.clear()

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja fazer outro cadastro? [S/N]')).upper().strip()
    if opc == 'N':
        break


listado = False
while listado == False:

    nome = str(input('Digite o nome do aluno:')).upper().strip()
    for aluno in boletim:
        if nome == aluno[0]:
            print(f'Média do(a) aluno(a) {aluno[0]}: {aluno[3]:.2f}')
            listado = True
            break
    else:
     print('Aluno não encontrado! Tente novamente!')

#print(boletim)
#print('-'*20)
#print('LISTAGEM DE ALUNOS:')
#print('-'*20)
#print(f"{'NOME ':<15} {'PRIMEIRA NOTA ':<15} {'SEGUNDA NOTA ' :<15} {'MÉDIA FINAL ' :<15}")
#for aluno in boletim:
 #   print(f"{aluno[0]:<15} {aluno[1]:<15.2f} {aluno[2]:<15.2f} {aluno[3]:<15.2f}")


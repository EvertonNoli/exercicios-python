nota = 0

while True:
    nota = float(input('Digite a nota do aluno:'))
    if (nota >= 0) and (nota <= 10):
        break
    else:
        print('Valor inválido! Tente novamente!')
print(f'O aluno teve nota {nota}')

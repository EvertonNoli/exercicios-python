#Faça um programa que calcule o número médio de alunos por turma.
#Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma
#As turmas não podem ter mais de 40 alunos

turma=int(input('Quantidade de turmas:'))
media=0

for i in range(turma):
    while True:
        aluno=int(input(f'Quantidade de alunos na turma {i+1}: '))
        if(aluno<=40):
            break
    media=((media*i)+aluno)/(i+1)

print(f'Média de alunos por turma: {media:.2f}')

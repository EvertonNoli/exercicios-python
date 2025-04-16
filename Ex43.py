cadastro=int(input('Quantas notas deseja cadastrar?'))
total=cont=nota=0
media=1

for i in range(1,cadastro+1):
    nota=float(input('Nota:'))
    total=nota+total
    cont+=1
media=(total/cont)

print(f'Foram cadastradas {cont} nota(s) e a média é igual a {media:.2f}')

cont=total=0
media=1

n=int(input('Quantas notas deseja cadastrar?'))
print(10*'=')
print('Somente notas entre 0 e 10 são contadas!')
print(10*'=')

while(cont<n):
    nota=(float(input('Nota:')))
    if(nota>=0) and (nota<=10):
        total=total+nota
        cont+=1
    else:
        print('Digite uma nota entre 0 e 10!')

media=total/cont
print(f'Foram cadastradas {cont} notas e a média é {media:.2f}')

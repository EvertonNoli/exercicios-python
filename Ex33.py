a=int(input('População A:'))
b=int(input('População B:'))
cresA=float(input('Crescimento da população A:'))
cresB=float(input('Crescimento da população B:'))
ano=0

if(a>b):
    print('A população A já é a maior!')
else:
    while(a<b):
        a=a+(a*(cresA/100))
        b=b+(b*(cresB/100))
        ano+=1

print(f'Levará {ano} ano(s) para a população A ultrapassar a B!')


inocente=suspeita=cumplice=assassino=0
cont1=cont2=cont3=cont4=cont5=total=0
p1=p2=p3=p4=p5=' '

while p1 not in 'SN':
    p1=str(input('Telefonou para a vítima?[S/N]')).upper().strip()[0]
    if(p1=='S'):
        cont1+=1
while p2 not in 'SN':
    p2=str(input('Esteve no local do crime?[S/N]')).upper().strip()[0]
    if(p2=='S'):
        cont2+=1
while p2 not in 'SN':
    p3=str(input('Mora perto da vítima?[S/N]')).upper().strip()[0]
    if(p3=='S'):
        cont3+=1
while p4 not in 'SN':
    p4=str(input('Devia para a vítima?[S/N]')).upper().strip()[0]
    if(p4=='S'):
        cont4+=1
while p5 not in 'SN':
    p5=str(input('Já trabalhou com a vítima?[S/N]')).upper().strip()[0]
    if(p5=='S'):
        cont5+=1

total=(cont1+cont2+cont3+cont4+cont5)

if(total<2):
    print('Inocente!')
elif(total==2):
    print('Suspeito(a)!')
elif(total>=3 and total<=4):
    print('Cúmplice!')
else:
    print('Culpado(a)!')
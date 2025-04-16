dia=32
uDia=dDia=resDia=0
mes=13
uMes=dMes=resMes=0
ano=-1
uAno=dAno=cAno=mAno=resAno=anoAst=0
digAno=cenAno=digDezAno=0

while dia>31 or dia<=0:
    dia=int(input('Dia de nascimento:'))
    if(dia>31) or (dia<=0):
        print('Digite um valor entre 1 e 31!')
    else:
        dDia=dia//10
        uDia=dia%10
        resDia=uDia+dDia
        #print(resDia)
while(mes>12) or (mes<=0):
    mes=int(input('Mês de nascimento:'))
    if(mes>12) or (mes<=0):
        print('Digite um valor entre 1 e 12!')
    else:
        dMes=mes//10
        uMes=mes%10
        resMes=uMes+dMes
        #print(resMes)
while ano<=0:
    ano=int(input('Ano de nascimento:'))
    mAno=ano//1000
    cAno=ano%1000
    digAno=cAno//100
    dAno=ano%1000
    cenAno=dAno%100
    digDezAno=cenAno//10
    uAno=ano%10
    resAno=mAno+digAno+digDezAno+uAno
    #print(resAno)

anoAst=resDia+resMes+resAno
print(f'''Dia de Nascimento:{dia}
Mês de Nascimento:{mes}
Ano de Nascimento:{ano}
Seu número atrológico:{anoAst}''')
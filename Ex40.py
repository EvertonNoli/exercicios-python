numero=dezena=unidade=res=0

while True:
    numero=int(input('Digite um número MENOR do que 100:'))
    if (numero>100):
        print('O número deve ser menor do que 100!')
    else:
        dezena=numero//10
        unidade=numero%10
        res=dezena+unidade
        break

print(f'{dezena} + {unidade} = {res}')
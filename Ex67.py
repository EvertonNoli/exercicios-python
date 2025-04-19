while True:
    n=int(input('Digite um número ou um valor negativo para encerrar:'))
    if n<0:
        break
    else:
        for c in range(0,11):
            print(f'{n} X {c} = {n*c}')
        print('-'*30)

print('Programa encerrado!')

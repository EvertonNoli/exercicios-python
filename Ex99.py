from time import sleep

def maior(*num):

    cont=maior=menor=0
    print('-='*30)
    print('Analisando os valores passados')
    sleep(1)
    for c in num:
        print(f'{c}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = c
            menor = c
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor = c
        cont+=1
    print()

    print(f'Foram analisandos {cont} valores. O maior valor é {maior} e o menor é {menor}')
    sleep(1)

#programa principal

maior(9,5,7,8,9,10)
maior(5,6,7,2)
maior(3,6,7)
maior(7)
maior()
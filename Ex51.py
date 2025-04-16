#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos:
#[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

c1=c2=c3=c4=c5=0

while True:
    n=int(input('Digite um número positivo ou negativo para encerrar:'))

    if(n>=0) and (n<=25):
        c1+=1

    elif(n>=26) and (n<=50):
        c2+=1

    elif(n>=51) and (n<=75):
        c3+=1

    elif(n>=76) and (n<=100):
        c4+=1

    elif(n>100):
        c5+=1

    else:
        break

print(f'Números entre 0 e 25: {c1}')
print(f'Números entre 26 e 50: {c2}')
print(f'Números entre 51 e 75: {c3}')
print(f'Números entre 76 e 100: {c4}')
print(f'Números maiores que 100: {c5}')
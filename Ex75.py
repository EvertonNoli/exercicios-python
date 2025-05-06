tupla = ()
cont9=0
pares = ()
n = 3
pos3 =[]

while True:
    valores = int(input('Digite um valor ou um número negativo para encerrar:'))
    if valores>=0:
        tupla+=(valores, )
    else:
        break
    if valores == 9:
        cont9+=1
    if valores%2==0:
        pares+=(valores, )

pos3 = [i+1 for i, valor in enumerate(tupla) if valor == n]
if pos3:
    print(f'O número {n} aparece nas posições {pos3}')
else:
    print(f'O número {n} não aparece na tupla!')

print(tupla)
print(cont9)
print(pares)
#print(f'O número 3 está na {tupla.index(3)}ª posição')

n=int(input('Quantidade de termos da sequência:'))
ultimo=penultimo=1
if(n==1) or (n==2):
    print('1')
else:
    for cont in range(2,n):
        termo=ultimo+penultimo
        penultimo=ultimo
        ultimo=termo
        cont+=1
        print(termo)
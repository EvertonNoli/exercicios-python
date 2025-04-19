print('Gerador de PA')
print('='*10)
primeiro = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão da PA:'))
termo = primeiro
pergunta = -2
cont = 0

for c in range(0,10):
    print(f'{termo}, ',end='')
    termo+=razao
    c+=1
    cont +=1

print('PAUSA!')
while pergunta !=0:
    pergunta=int(input('Quantos termos deseja mostrar a mais?'))
    if pergunta==0:
        break
    else:
        for c in range(0,pergunta):
            print(f'{termo}, ', end='')
            termo+=razao
            c+=1
            cont +=1
    print('PAUSA!')

print(f'Foram contados {cont} números')
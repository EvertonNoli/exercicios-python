from datetime import date

atual=date.today().year
maiorIdade=0
menorIdade=0

for c in range(1,8):
    ano=int(input(f'Digite o ano de nascimento da {c}° pessoa:'))
    c+=1

    if(atual-ano)>=18:
        maiorIdade+=1
    else:
        menorIdade+=1

print(f'{maiorIdade} pessoa(s) são maiores de idade')
print(f'{menorIdade} pessoa(s) são menores de idade')
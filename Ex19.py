n=int(input('Digite um número inteiro menor do que 1000:'))

if n>=1000:
    print('O valor deve ser inferior a 1000!')
else:
    centena=n//100
    dezena=(n%100)//10
    unidade=(n%10)

print(f'O número tem {centena} centena(s), {dezena} dezena(s)  {unidade} unidade(s)')
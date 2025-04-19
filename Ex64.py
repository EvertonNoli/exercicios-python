n=total=soma=0

while n!=999:
    n = int(input('Digite um número ou 999 para parar:'))
    if n==999:
        break
    else:
        total += 1
        soma += n

print(f'Foram digitados {total} número(s) e a soma entre eles é {soma}!')
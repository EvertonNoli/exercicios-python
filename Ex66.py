c = soma = 0

while True:
    n = int(input('Digite um valor ou 999 para encerrar:'))
    if n==999:
        break
    else:
        c+=1
        soma+=n


print(f'A soma dos {c} números digitados é {soma}')
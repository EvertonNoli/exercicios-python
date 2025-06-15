print('Gerador de PA')
print('='*10)
primeiro = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão da PA:'))
termo = primeiro

for c in range(1,11):
    print(f'{termo}, ', end='')
    termo+=razao
    c+=1

print('FIM!')
tabela = ('Palmeiras', 'Flamengo', 'Fluminense', 'Bragantino', 'Ceará',
          'Corinthians','Cruzeiro','Vasco da Gama', 'Juventude', 'São Paulo',
          'Mirassol','Internacional','Bahia','Fortaleza','Botafogo','Vitória','Atlético-MG',
          'Santos', 'Grêmio', 'Sport')

print('=-'*10)
print('Dados Brasileirão')
print('=-'*10)
print(f'Os cinco primeiros colocados são {tabela[0:5]}')
print('=-'*10)
print(f'Os cinco últimos colocados são {tabela[-5:]}')
print('=-'*10)
print(f'O Vasco está na {tabela.index('Vasco da Gama')}° posição!')
print('=-'*10)
print(f'Times por ondem alfabética: {sorted(tabela)}')
print('=-'*10)
print(f'Ordem alfabética reversa: {sorted(tabela, reverse=True)}')

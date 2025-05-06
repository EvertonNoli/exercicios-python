print('='*45)
print('Listagem de Preços')
print('='*45)
produtos = ('Lápis',1.20, 'Borracha', 2, 'Caderno', 15.9, 'Mochila',120.23, 'Estojo', 13.40, 'Compasso', 7.89, 'Canetas', 6, 'Livros', 99.87)

for c in produtos:
    if type(c) is str:
        print(f'{c:.<32}', end=' ')
    else:
        print(f'R${c:.2f}')

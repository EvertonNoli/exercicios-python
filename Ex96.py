def area():
    largura = float(input('Largura em metros: '))
    comprimento = float(input('Comprimento em metros: '))
    print(f'A área de um terreno de {largura} x {comprimento} é de {largura*comprimento:.2f}')

def cabecalho():
    print('-'*30)
    print('Cadastro de terrenos')

cabecalho()
area()
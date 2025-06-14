from time import sleep
from math import sqrt
from math import pi

def menu():

    print('-='*10)
    print('Cálculo de Área')
    print('0 - Encerrar programa')
    print('1 - Retângulo')
    print('2 - Triângulo')
    print('3 - Quadrado')
    print('4 - Cilindro')
    print('5 - Circunferência')
    return int(input('Selecione uma opção:'))

def retangulo():
    base = float(input('Base:'))
    altura = float(input('Altura:'))
    print(f'A área do retângulo é de {base*altura:.2f}')

def triangulo():
    l1 = float(input('Primeiro lado:'))
    l2 = float(input('Segundo lado:'))
    l3 = float(input('Terceiro lado:'))

    if l1 < l2+l3 and l2 < l1+l3 and l3<l1+l2:
        s = (l1+l2+l3)/2 #semiperimetro
        area = sqrt(s*(s-l1)*(s-l2)*(s-l3))
        print(f'A área do triângulo é de {area:.2f}')
    else:
        print('Com essas medidas não é possível formar um triângulo')

def quadrado():
    lado = float(input('Medida do lado:'))
    print(f'Medida da área: {lado**2:.2f}')

def cilindro():
    base = float(input('Base:'))
    altura = float(input('Altura:'))
    raio = base/2
    print(f'{2*pi*raio*(altura+raio):.2f}')

def circunferencia():
    diametro = float(input('Informe o diâmetro:'))
    raio = diametro/2
    print(f'{pi*(raio**2):.2f}')

#programa principal
while True:

    opc = menu()

    if opc == 0:
        print('Encerrando programa...')
        sleep(1)
        print('Programa encerrado!')
        break

    elif opc == 1:
        retangulo()

    elif opc == 2:
        triangulo()

    elif opc == 3:
        quadrado()

    elif opc == 4:
        cilindro()

    elif opc == 5:
        circunferencia()

    else:
        print('Opção inválida!')

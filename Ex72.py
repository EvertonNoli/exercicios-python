n = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
     'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')


while True:
    cont = (int(input('Digite um valor:')))
    if cont>20 or cont <0:
        print('Digite um valor entre zero e vinte!')
    else:
        break


print(f'Você digitou o valor: {n[cont]}')
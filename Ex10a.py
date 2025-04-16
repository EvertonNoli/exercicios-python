#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno=' '
while turno not in 'MVN':
    turno=str(input('Em que turno você estuda:[M/V/N]')).strip().upper()[0]
    if(turno=='M'):
        print('Período matutino!')
        break
    elif(turno=='V'):
        print('Período vespertino!')
        break
    elif(turno=='N'):
        print('Período noturno!')
        break
    else:
        print('Valor inválido!')





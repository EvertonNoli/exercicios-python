expressao = str(input('Digite uma expressão: '))
parenteses = []

for simbolo in expressao:
    if simbolo == '(':
        parenteses.append(simbolo)
    elif simbolo == ')':
        if len(parenteses)>0:
            parenteses.pop()
        else:
            parenteses.append(simbolo)
            break

if len(parenteses)==0:
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')
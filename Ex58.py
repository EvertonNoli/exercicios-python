from random import randint

computador=randint(1,10)
#print(computador)
cont=0

while True:
    print('Hi!Im the computer. Im thinking of a number from 0 to 10! Try to guess!')
    usuario=int(input('Type a number:'))
    cont+=1
    if usuario<computador:
        print('Try a bigger one...')
    elif usuario>computador:
        print('Try a smaller one...')
    else:
        break

print(f'Congratulations! You hit the number which was {usuario} and only needed {cont} guesses for that!')

input('Press enter to close...')



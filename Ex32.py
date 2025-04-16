popA=80000
popB=200000
cont=0

while(popA<popB):
    popA=popA+(popA*(3/100))
    popB=popB+(popB*(1.5/100))
    cont+=1

print(popA)
print(popB)
print(f'Levará {cont} anos para a população A ultrapassar a B')
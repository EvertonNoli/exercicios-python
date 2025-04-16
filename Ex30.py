nome=senha=' '
while True:
    nome=str(input('Digite seu nome:')).upper().strip()
    senha=str(input('Digite a senha:')).upper().strip()
    if(senha==nome):
        print("Senha e nome precisam ser diferentes!")
    else:
        break

print('Usuário cadastrado com sucesso!')
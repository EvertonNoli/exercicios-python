funcionario = {}

funcionario['nome']=str(input('Nome: ')).upper()
funcionario['nasc']=int(input('Ano de nascimento: '))
funcionario['clt']=int(input('Carteira de Trabalho(0, caso não tenha): '))
if funcionario['clt']==0:
    for k,v in funcionario.items():
        print(f'{k}: {v}')
else:
    funcionario['contrato']=int(input('Ano de contratação: '))
    funcionario['salario']=float(input('Salário: R$'))
    idade = 2025 - funcionario['nasc']
    tempo_servico = 2025-funcionario['contrato']
    funcionario['aposentadoria']=35-tempo_servico+idade

    for k,v in funcionario.items():
        print(f'{k}: {v}')


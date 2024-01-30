print('Verificação de idade')
verificacao_idade = int(input("Por favor insira sua idade:"))
if 0 < verificacao_idade <= 12:
    print('Você é uma criança')
elif 12 < verificacao_idade <= 18:
    print(' Você é uma adolescente')
elif verificacao_idade > 18:
    print('Você é um adulto')
else:
    print("Parametros sem resposta correta")

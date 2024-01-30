print('Cadastro de usuário')
nome_usuario = 'Thiago10'
senha_usuario = 'Thiago100'


usuario = input('Insira nome de usuário:')
senha = input('Insira a senha:')


if nome_usuario== usuario and senha_usuario == senha:
    print('Acesso permitido')
else:
    print('Acesso negado')

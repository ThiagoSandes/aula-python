import os
# restaurantes = ['saborsertao', 'sabornenca']
restaurantes = [{'nome': 'Saborsertao', 'categoria': 'Almoço', 'Ativação': True},
                {'nome': 'NordesteJantar', 'categoria': 'Jantar', 'Ativação': False},
                {'nome': 'Pizzariatodo', 'categoria': 'Pizza', 'Ativação': True}
                ]


def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def exibir_nome(exibir_titulo):
    os.system('cls')
    print(exibir_titulo)


def limpar_terminal():
    input('Selecione qualquer tecla para recomecar:')
    main()


def finalizar_app():
    os.system('cls')
    # os.system('clear')
    print('Finalizando o app')


def opcao_incorreta():
    print('você inseriu uma opção incorreta!\n')
    limpar_terminal()


def listar_restaurante():
    exibir_nome('Listar Restaurantes Cadastrados:\n')
    for nome_restaurante in restaurantes:
        filtro_nome = nome_restaurante['nome']
        filtro_categoria = nome_restaurante['categoria']
        filtro_status = nome_restaurante['Ativação']
        filtro_status = 'Ativado' if filtro_status else 'Desativado'
        print(f'{filtro_nome}|{filtro_categoria}|{filtro_status}')
    limpar_terminal()


def filtrar_restaurante():
    while True:
        filtro_restaurante = input('Informe Ativado ou Desativado: ')
        if filtro_restaurante.lower() == 'ativado':
            filtro_restaurante = True
            break
        elif filtro_restaurante.lower() == 'desativado':
            filtro_restaurante = False
            break
        else:
            print('Dados não correspondente')
            continue
    return filtro_restaurante


def cadastrar_restaurante():
    exibir_nome('Cadastar Restaurante!\n')
    nome_restaurante = input('Informe o nome do restaurante: ')
    categoria_restaurante = input('Informe o nome da categoria: ')
    filtro_restaurante = filtrar_restaurante()
    tratamento_restaurante = {'nome': nome_restaurante,
                              'categoria': categoria_restaurante, 'Ativação': filtro_restaurante}
    restaurantes.append(tratamento_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    limpar_terminal()


def alterando_status_restaurante():
    exibir_nome('Ativer ou Desativar Restaurente\n')
    restaurante_status = input(
        'Escreva o nome do restaurante que desejar ativar ou desativar: ')
    restaurante_encontrado = False
    for nome_restaurante in restaurantes:
        if restaurante_status == nome_restaurante['nome']:
            restaurante_encontrado = True
            print(f'Restaurante Localizado {nome_restaurante['nome']} | {
                  nome_restaurante['Ativação']}')
            nome_restaurante['Ativação'] = not nome_restaurante['Ativação']
            mensagem = f'O restaurante {restaurante_status} foi ativado com sucesso ' if nome_restaurante['Ativação'] else f'O restaurante {
                restaurante_status} foi desativado.'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não localizado.')
        novo_cadastro = input(
            'Deseja cadastrar um novo restaurante? (sim/nao): ')
        if novo_cadastro.lower() == 'sim':
            cadastrar_restaurante()
    limpar_terminal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alterando_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_incorreta()
    except:
        opcao_incorreta()
    limpar_terminal()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()

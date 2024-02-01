import os
# restaurantes = ['saborsertao', 'sabornenca']
restaurantes = [{'nome': 'Saborsertao', 'categoria': 'Almoço', 'Ativação': True},
                {'nome': 'NordesteJantar', 'categoria': 'Jantar', 'Ativação': False},
                {'nome': 'Pizzariatodo', 'categoria': 'Pizza', 'Ativação': True}]


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
    print('você inseriu uma opção incorreta\n!')
    limpar_terminal()


def listar_restaurante():
    exibir_nome('Listar Restaurantes Cadastrado:\n')
    for nome_restaurante in restaurantes:
        filtro_nome = nome_restaurante['nome']
        filtro_categoria = nome_restaurante['categoria']
        filtro_status = nome_restaurante['Ativação']
        filtro_status = 'Ativado' if filtro_status == True else 'Desativado'
        print(f'{filtro_nome}|{filtro_categoria}|{filtro_status}')
    limpar_terminal()


def cadastrar_restaurante():
    exibir_nome('Cadastar Restaurante!\n')
    nome_restaurante = input('Informe o nome do restaurante:')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    limpar_terminal()


def alterando_status_restaurante():
    exibir_nome('Ativer ou Desativar Restaurente')

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


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()

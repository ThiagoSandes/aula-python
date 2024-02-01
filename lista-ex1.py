import os

lista_numero = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
lista_nome = ['Pedro', 'Maria', 'Joao', 'Thiago']
lista_ano = [1994, 2024]


def recomecar_system():
    input('Selecione qualquer tecla para recomecar:')
    main()


def listar_nome():
    print('1.Listar numero\n2.Listar Nome\n3.Listar Ano\n')


def selecionar_opcao():
    selecione_lista = int(input('Selecione lista que deseja imprimir:\n'))
    if selecione_lista == 1:
        for numero in lista_numero:
            print(numero)
    elif selecione_lista == 2:
        print(lista_nome)
    elif selecione_lista == 3:
        print(lista_ano)
    else:
        print('tecla inserida não correspondente')
        recomecar_system()


def main():
    os.system('cls')
    listar_nome()
    selecionar_opcao()
    recomecar_system()


if __name__ == '__main__':
    main()

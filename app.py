import os

restaurantes = [{'nome':'superdog', 'categoria':'cachorro quente', 'ativo':False},
                 {'nome':'mega pizza', 'categoria':'pizza', 'ativo':True},
                 {'nome':'sonho italiano', 'categoria':'massa', 'ativo':False}]

def exibir_nome_prog():
    '''Exibe o nome'''
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      ''')

def exibir_opcoes():
    '''mostra as opções de açoes'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Termina o app'''
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    '''Retorna para o menu das opções'''
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    '''Mostra que não tem opção com tal comando'''
    print('opção invalida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''mostra o suntitulo da ação'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante
    
    Inputs:
    - nome do restaurante
    - categoria

    Output:
    - adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante,
                            'categoria':categoria,
                            'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa funcão pega todas os resaurantes cadastrados na lista e mostra na tela'''
    exibir_subtitulo('Listando os restaurantes')

    # print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Altera o restaurante para ativo ou inativo
    
    input:
    - nome de um restaurante cadastrado

    output:
    - altera o estado dele (ativo e inativo)
    
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''Exibi as opções disponivel para otras funções
    
    input:
    - numero da ação

    output:
    - ativa a função correspondente ao número

    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except: opcao_invalida()

   


def main():
    '''exibe o nome, opções e escolhas do app'''
    os.system('cls')
    exibir_nome_prog()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()


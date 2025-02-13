import menu_options  # Importa o módulo menu_options que contém as funções de manipulação

def exibir_menu():
    print("\n===== Menu =====")  # Exibe o cabeçalho do menu
    print("1. Exibir Tarefas")  # Opção para exibir as tarefas
    print("2. Sair")  # Opção para sair do programa

def exibir_tarefas(): 
    # Vai Exibir uma listagem de 8 opções que usuário pode escolher
    print("\n===== Tarefas existentes =====")
    print("[1] - Registrar um produto novo na tabela de produtos")
    print("[2] - Remover um produto da tabela de produtos")
    print("[3] - Inserir uma linha na tabela de entrada de produtos")
    print("[4] - Inserir uma linha na tabela de saída de produtos")
    print("[5] - Relatório de produtos a serem comprados")
    print("[6] - Relatório de produtos a serem vendidos")
    print("[7] - Mostrar o relatório de produtos em estoque")
    print("[8] - Mostrar o relatório de produtos cadastrados ")
    tarefaSelecionada = input("\nEscolha a tarefa a ser executada: ")
    
    # Bloco de condições que chama a função correspondente com base na escolha do usuário
    if tarefaSelecionada == '1':
        menu_options.registrarNovoProduto()
    elif tarefaSelecionada == '2':
        menu_options.removerProdutoNulo()
    elif tarefaSelecionada == '3':
        menu_options.inserirProdutoTabelaEntrada()
    elif tarefaSelecionada == '4':
        menu_options.inserirProdutosTabelaSaida()
    elif tarefaSelecionada == '5':
        menu_options.relatorioCompras()
    elif tarefaSelecionada == '6':
        menu_options.relatorioVendas()
    elif tarefaSelecionada == '7':
        menu_options.relatorioEstoque()
    elif tarefaSelecionada == '8':
        menu_options.relatorioProdutosCadastrados()
    else:
        print("Opção inválida!")  # Mensagem de erro para opção inválida
        return exibir_tarefas()  # Chama recursivamente a função exibir_tarefas para nova escolha

def main():
    while True:  # Loop infinito para manter o programa em execução
        exibir_menu()  # Chama a função para exibir o menu principal
        
        opcao = input("Escolha uma opção: ")  # Solicita ao usuário escolher uma opção do menu principal
        
        if opcao == "1":
            exibir_tarefas()  # Chama a função para exibir e lidar com as tarefas
            break  # Sai do loop e encerra o programa após a execução de uma tarefa
        elif opcao == "2":
            break  # Encerra o loop e o programa
        else:
            print("Opção inválida. Tente novamente.")  # Mensagem de erro para opção inválida

if __name__ == "__main__":
    main()  # Executa a função main se o arquivo for executado diretamente
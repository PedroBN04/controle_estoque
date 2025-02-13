import random # Importação do módulo random
import painel # Importação do módulo personalizado para exibir o painel de menu para o usuário

def validaCodigoProduto(diretorio):
    arqRead = open(f"{diretorio}", "r")  # Abre o arquivo para leitura
    conteudo = arqRead.read()  # Lê todo o conteúdo do arquivo
    codigos = eval(conteudo) if conteudo else []  # Converte o conteúdo para lista se não estiver vazio, senão cria uma lista vazia
    
    arqRead.close()  # Fecha o arquivo de leitura
    novoCodigo = random.randint(1, 999)  # Gera um novo código aleatório
    while novoCodigo in codigos:  # Checa se o código já existe na lista de códigos do arquivo "cod_produtos.txt"
        novoCodigo = random.randint(1, 999)  # Gera um novo código até que seja único
    
    codigos.append(novoCodigo)  # Adiciona o novo código à lista
    arqWrite = open("cod_produtos.txt", "w")  # Abre o arquivo para escrita (sobrescreve se já existir)
    arqWrite.write(str(codigos))  # Escreve a lista atualizada no arquivo
    arqWrite.close()  # Fecha o arquivo de escrita
    
    return novoCodigo  # Retorna o novo código gerado

def registrarNovoProduto():
    print("\n===== Registre um novo produto na Tabela de Produtos =====")
    print("Exemplo de dados a serem inseridos: 'Iphone Smartphones'")
    dadosProduto = input("\nRegistre o produto: ").split()  # Recebe entrada do usuário e divide em lista
    if (len(dadosProduto) != 2): # Verifica se existe mais ou menos que dois elementos dentro da lista de dados do produto
        print("Digite apenas o Nome do produto e o Setor do produto")
        return registrarNovoProduto()  # Chama a função novamente se os dados não estiverem corretos

    codigo = validaCodigoProduto("cod_produtos.txt")  # Valida e gera um código para o produto
    chaves = ["Codigo", "Nome", "Setor"]
    dadosProduto.insert(0, codigo)  # Insere o código gerado na primeira posição da lista
    dic = dict(zip(chaves, dadosProduto))  # Cria um dicionário a partir das chaves e valores do produto
    
    arqRead = open('./tables/produtos/produtos_table.txt', 'r')  # Abre o arquivo de tabela de produtos para leitura
    for produto in arqRead:  # Itera sobre cada linha no arquivo
        produtoFormatado = eval(produto)  # Converte a string para dicionário
        if (produtoFormatado["Nome"] == dic["Nome"]):  # Verifica se o nome do produto já existe
            print("\n### Esse produto ja foi cadastrado. Tente novamente! ###")
            return registrarNovoProduto()  # Chama a função novamente se o produto já existir
    
    arqWriter = open("./tables/produtos/produtos_table.txt", "a")  # Abre o arquivo para adicionar dados ao final
    arqWriter.write(str(dic) + "\n")  # Escreve o dicionário como string no arquivo
    arqWriter.close()  # Fecha o arquivo de escrita
        
    print(f"\nNovo produto registrado: {dic}")  # Mostra o produto registrado
    return painel.main()  # Retorna para o menu principal

def removerProdutoNulo():
    print("\n===== Remover um produto da tabela de produtos (caso a quantidade em estoque seja nula) =====")
    relatorioProdutosCadastrados()  # Mostra relatório de produtos cadastrados para consulta
    relatorioEstoque()  # Mostra relatório de estoque para consulta
    
    codigo = int(input("\nInsira o código do produto a ser removido: "))  # Recebe o código do produto a remover
    if (codigo < 1): # Valida se o código é menor que 1 (So podem existir códigos entre 1 e 999)
        print("Digite código do produto válido")
        return  # Retorna se o código não for válido

    listaEstoque = [] # Inicializa uma lista vazia para armazenar, posteriormente, dicionários relativo à um produto
    arqEstoque = open("./tables/estoque/estoque_table.txt", "r")  # Abre arquivo de estoque para leitura
    
    for linha in arqEstoque:
        produtoFormatado = eval(linha)  # Converte linha para dicionário
        listaEstoque.append(produtoFormatado)  # Adiciona dicionário à lista de estoque
    
    for produto in listaEstoque:
        if produto["Codigo"] == codigo and produto["Quantidade"] == 0:  # Verifica se o código digitado e o do produto percorrido pelo "for" corresponde, e se a quantidade do produto é zero
            arqCodigos = open("cod_produtos.txt", "r")  # Abre arquivo de códigos para leitura
            conteudoCod = arqCodigos.read()  # Lê conteúdo do arquivo
            codigos = eval(conteudoCod) if conteudoCod else []  # Converte o conteúdo para lista se não estiver vazio, senão cria uma lista vazia
            if not codigos or codigo not in codigos: # Verifica se a lista "codigos" esta vazia ou se o código inserido pelo usuário não existe dentro da lista "códigos"
                print("Código inserido não esta vinculado a nenhum produto!")
                return removerProdutoNulo()  # Retorna se não encontrar o código
            
            codigos.remove(codigo)  # Remove o código da lista
            arqCodigos.close()  # Fecha o arquivo
            
            arqCodigos = open("cod_produtos.txt", "w")  # Abre arquivo para escrita
            arqCodigos.write(str(codigos))  # Escreve a lista atualizada
            arqCodigos.close()  # Fecha o arquivo
            
            arqProdutos = open("./tables/produtos/produtos_table.txt", "r")  # Abre arquivo de produtos para leitura
            linhas = arqProdutos.readlines()  # Lê todas as linhas
            arqProdutos.close()  # Fecha o arquivo
            
            novosProdutos = []  # Lista para novos produtos
            produtoRemovido = {}  # Dicionário para o produto removido
            
            for linha in linhas:
                produtos = eval(linha)  # Converte linha para dicionário
                print(produtos)  # Imprime cada produto
                if codigo != produtos["Codigo"]:  # Mantém produtos que não são para remover
                    novosProdutos.append(produtos)
                else:
                    produtoRemovido = produtos  # Guarda produto removido
            
            arqProdutos = open("./tables/produtos/produtos_table.txt", "w")  # Abre arquivo para escrita
            for produto in novosProdutos:
                arqProdutos.write(str(produto) + "\n")  # Escreve produtos atualizados
            arqProdutos.close()  # Fecha arquivo

            print(f"\n===== Produto removido =====")
            print(f"Nome: {produtoRemovido["Nome"]} \nSetor: {produtoRemovido["Setor"]}")  # Imprime dados do produto removido
            return painel.main()  # Retorna para o menu principal
    arqEstoque.close()
    print("\n#### O produto selecionado ainda tem quantidade excedente em estoque! ####")
    return removerProdutoNulo()  # Chama a função novamente se a quantidade não for zero
    
def inserirProdutoTabelaEntrada():
    relatorioProdutosCadastrados()  # Mostra o relatório de produtos cadastrados
    
    print("\n===== Realize a compra do produto =====")
    print("===== Digite: Código - Data - Unidade (gramas) - Preço =====")
    codigo = int(input("- Código: "))  # Solicita o código do produto
    data = str(input("- Data (dia/mês/ano): "))  # Solicita a data da compra
    quantidade = int(input("- Quantidade: "))  # Solicita a quantidade comprada
    unidade = str(input("- Unidade (Ex: 10g): "))  # Solicita a unidade da quantidade
    preco = float(input("- Preço: "))  # Solicita o preço da compra
    
    if (codigo and quantidade and preco > 0):  # Verifica se os valores inseridos são válidos
        listaDadosEntrada = [codigo, data, quantidade, unidade, preco] # Armazena os dados isneridos pelo usuário dentro de uma lista em ordem que será armazenada na tabela 
        chaves = ["Codigo", "Data", "Quantidade", "Unidade", "Preco"]
        
        arqCodigos = open("cod_produtos.txt", 'r')  # Abre o arquivo de códigos para leitura
        conteudoCod = arqCodigos.read()  # Lê o conteúdo do arquivo
        codigos_tabela = eval(conteudoCod) if conteudoCod else []  # Converte o conteúdo para lista se não estiver vazio, senão cria uma lista vazia
        
        if codigo not in codigos_tabela: # Valida se o códig inserido pelo usuário não existe dentro da lista "codigos_tabela"
            print("\nProduto não encontrado, tente novamente!")
            return inserirProdutoTabelaEntrada()  # Solicita a reentrada dos dados se o código não existir
        
        arqEntrada = open("./tables/entrada/entrada_table.txt", "a")  # Abre o arquivo de entrada para adicionar dados
        dic = dict(zip(chaves, listaDadosEntrada))  # Cria um dicionário com os dados da compra
        arqEntrada.write(str(dic) + "\n")  # Escreve os dados no arquivo
        arqEntrada.close()  # Fecha o arquivo
        print("\nProduto(s) comprado(s) com sucesso!")
        return painel.main()  # Retorna ao menu principal
    else:
        print("\nDigite valores positivos para os dados inseridos")
        return inserirProdutoTabelaEntrada()  # Solicita a reentrada dos dados se forem inválidos

def inserirProdutosTabelaSaida():
    relatorioEstoque()  # Mostra o relatório de estoque
    
    print("\n===== Realize a Venda do produto =====")
    print("===== Digite: Código - Data - Unidade (gramas) - Preço =====")
    codigo = int(input("- Código: "))  # Solicita o código do produto
    data = str(input("- Data (dia/mês/ano): "))  # Solicita a data da venda
    quantidade = int(input("- Quantidade: "))  # Solicita a quantidade vendida
    unidade = str(input("- Unidade (Ex: 10g): "))  # Solicita a unidade da quantidade
    preco = float(input("- Preço: "))  # Solicita o preço da venda
    
    if (codigo and quantidade and preco > 0):  # Verifica se os valores inseridos são válidos
        listaProduto = [codigo, data, quantidade, unidade, preco]
        chavesSaida = ["Codigo", "Data", "Quantidade", "Unidade", "Preco"]
        
        arqCodigos = open("cod_produtos.txt", 'r')  # Abre o arquivo de códigos para leitura
        conteudoCod = arqCodigos.read()  # Lê o conteúdo do arquivo
        codigos_tabela = eval(conteudoCod) if conteudoCod else []  # Converte o conteúdo para lista se não estiver vazio, senão cria uma lista vazia
        
        if codigo not in codigos_tabela:
            print("\nProduto não encontrado, tente novamente!")
            return inserirProdutosTabelaSaida()  # Solicita a reentrada dos dados se o código não existir
        
        arqEstoque = open("./tables/estoque/estoque_table.txt", "r");  # Abre o arquivo de estoque para leitura
        for produto in arqEstoque:
            produtoFormatado = eval(produto);  # Converte linha para dicionário
            
            if (codigo == produtoFormatado["Codigo"]):
                if (quantidade <= produtoFormatado["Quantidade"]):  # Verifica se a quantidade em estoque é suficiente
                    arqSaida = open("./tables/saida/saida_table.txt", "a")  # Abre o arquivo de saída para adicionar dados
                    dicSaida = dict(zip(chavesSaida, listaProduto))  # Cria um dicionário com os dados da venda
                    arqSaida.write(str(dicSaida) + "\n")  # Escreve os dados no arquivo
                    arqSaida.close()  # Fecha o arquivo
                    print("\nProduto(s) Vendido(s) com sucesso!")
                    return painel.main();  # Finaliza a função
                else:
                    print("A quantidade de produtos no estoque não é suficiente para atender a demanda.")
                    return inserirProdutosTabelaSaida();  # Solicita a reentrada dos dados se a quantidade em estoque for insuficiente
        arqEstoque.close();
    else:
        print("\nDigite valores positivos para os dados inseridos")
        return inserirProdutoTabelaEntrada()  # Solicita a reentrada dos dados se forem inválidos

def relatorioCompras():
    print("\n===== Relatório de Produtos Comprados =====")
    
    arq = open('./tables/entrada/entrada_table.txt', "r")  # Abre o arquivo de entrada para leitura
    valorTotalEntrada = 0 # Inicializa, com valor zero, a variável que armazenará o valor total a ser pago
    for produto in arq:
        produtoFormatado = eval(produto)  # Converte linha para dicionário
        valorTotalEntrada += produtoFormatado.get("Preco", 0)  # Soma o preço ao valor total
        print(produtoFormatado)  # Imprime cada produto comprado
    arq.close()
    
    print(f"\nValor Total a ser pago: R${valorTotalEntrada:.2f}")  # Imprime o valor total das compras
    return painel.main();  # Retorna ao menu principal

def relatorioVendas():
    print("\n===== Relatório de Produtos Vendidos =====")
    
    arq = open('./tables/saida/saida_table.txt', "r")  # Abre o arquivo de saída para leitura
    valorTotalSaida = 0 # Inicializa, com valor zero, a variável que armazenará o valor total a ser recebido
    for produto in arq:
        produtoFormatado = eval(produto)  # Converte linha para dicionário
        valorTotalSaida += produtoFormatado.get("Preco", 0)  # Soma o preço ao valor total
        print(produtoFormatado)  # Imprime cada produto vendido
    arq.close()
    
    print(f"\nValor Total a ser recebido: R${valorTotalSaida:.2f}")  # Imprime o valor total das vendas
    return painel.main();  # Retorna ao menu principal

def relatorioEstoque():
    print("\n===== Relatório do Estoque =====")
    
    def lerArquivo(diretorio):
        lista = [] # Inizializado como lista vazia, para armazenar uma lista de dicionários
        arq = open(diretorio, "r")  # Abre o arquivo para leitura
        for linha in arq:
            if linha.strip():  # Verifica se a linha não está vazia
                linhaConvertida = eval(linha)  # Converte linha para dicionário
                lista.append(linhaConvertida)  # Adiciona dicionário à lista
        arq.close()  # Fecha o arquivo
        return lista  # Retorna a lista de dicionários
    
    listaEntradaProdutos = lerArquivo("./tables/entrada/entrada_table.txt")  # Lê dados de produtos comprados
    listaSaidaProdutos = lerArquivo("./tables/saida/saida_table.txt")  # Lê dados de produtos vendidos
    listaProdutosCadastrados = lerArquivo("./tables/produtos/produtos_table.txt")  # Lê dados de produtos cadastrados

    entradas = {}  # Dicionário para armazenar quantidades compradas, de forma que, a chave seja o código do produto e a quantidade seja seu valor
    saidas = {}  # Dicionário para armazenar quantidades vendidas, de forma que, a chave seja o código do produto e a quantidade seja seu valor
    
    for entrada in listaEntradaProdutos:
        codigoEntrada = entrada["Codigo"]
        quantidadeEntrada = entrada["Quantidade"]
        entradas[codigoEntrada] = quantidadeEntrada  # armazena dentro da chave "codigoEntrada" do dicionário "entradas" a quantidade relativa a tabela de entrada
    
    for saida in listaSaidaProdutos:
        codigoSaida = saida["Codigo"] # Armazena o valor associado ao Código do produto
        quantidadeSaida = saida["Quantidade"] # Armazena o valor associado a Quantidade do produto
        saidas[codigoSaida] = quantidadeSaida  # armazena dentro da chave "codigoSaida" do dicionário "saidas" a quantidade relativa a tabela de entrada
    
    listaTodosProdutos = [] # Inicializa a lista vazia, que irá armazenar diversas listas com dados dos produtos para o estoque
    chavesEstoque = ["Codigo", "Nome", "Setor", "Quantidade"]
    
    for codigo in entradas:
        quantidadeEstoque = (entradas.get(codigo, 0) - saidas.get(codigo, 0))  # Calcula a quantidade em estoque subtraindo as vendas das compras
        nomeProduto = ""
        setorProduto = ""
        for produto in listaProdutosCadastrados:
            if produto["Codigo"] == codigo:  # Localiza o produto pelo código
                nomeProduto = produto["Nome"]
                setorProduto = produto["Setor"]
                break  # Sai do loop após encontrar o produto
        
        listaTodosProdutos.append([codigo, nomeProduto, setorProduto, quantidadeEstoque])  # Adiciona o produto à lista de estoque
    
    arqEstoque = open("./tables/estoque/estoque_table.txt", "w")  # Abre arquivo de estoque para escrita
    for produtoAtualizado in listaTodosProdutos:
        dic = dict(zip(chavesEstoque, produtoAtualizado))  # Cria um dicionário com os dados atualizados
        arqEstoque.write(str(dic) + "\n")  # Escreve cada produto atualizado no arquivo
    arqEstoque.close()  # Fecha o arquivo
    
    arqEstoque = open("./tables/estoque/estoque_table.txt", "r")  # Abre arquivo de estoque para leitura
    for produtoEstoque in arqEstoque:
        produtoEstoqueFormatado = eval(produtoEstoque)  # Converte linha para dicionário
        print(produtoEstoqueFormatado)  # Imprime cada produto em estoque
    arqEstoque.close()  # Fecha o arquivo
    return;

def relatorioProdutosCadastrados():
    print("\n===== Relatório Produtos Cadastrados =====")
    
    arq = open('./tables/produtos/produtos_table.txt', "r")  # Abre o arquivo de produtos cadastrados para leitura
    for produto in arq:
        produtoFormatado = eval(produto)  # Converte linha para dicionário
        print(produtoFormatado)  # Imprime cada produto cadastrado
    arq.close()  # Fecha o arquivo
    return;
    
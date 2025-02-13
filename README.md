# 📌 Gerenciador de Produtos

Este projeto consiste em um sistema de gerenciamento de produtos que permite cadastrar, remover e visualizar produtos em estoque, além de gerar relatórios de compras e vendas.

## 📄 Descrição
O sistema é composto por dois módulos principais:

1. **menu_options.py**: Contém as funções responsáveis por cadastrar, remover e gerenciar produtos, além da geração de relatórios.
2. **painel.py**: Gerencia a interface do usuário e a navegação entre as opções do sistema.

## 🛠️ Funcionalidades
- **Registrar um novo produto**
- **Remover um produto do estoque** (caso esteja com quantidade zerada)
- **Inserir novos produtos na tabela de entrada**
- **Registrar saída de produtos vendidos**
- **Gerar relatórios**:
  - Produtos comprados
  - Produtos vendidos
  - Produtos em estoque
  - Produtos cadastrados

## 🚀 Como Executar

1. **Clone o repositório**:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. **Navegue até o diretório do projeto**:
   ```sh
   cd nome-do-projeto
   ```
3. **Execute o arquivo `painel.py`**:
   ```sh
   python painel.py
   ```

## 🔧 Estrutura dos Arquivos
```
/
├── menu_options.py  # Gerenciamento de produtos e relatórios
├── painel.py        # Interface do menu principal
├── tables/
│   ├── produtos/produtos_table.txt  # Armazena os produtos cadastrados
│   ├── estoque/estoque_table.txt    # Armazena os produtos em estoque
│   ├── entrada/entrada_table.txt    # Registra as compras de produtos
│   ├── saida/saida_table.txt        # Registra as vendas de produtos
├── cod_produtos.txt  # Lista com os códigos dos produtos
```

## 📌 Autor
Pedro Humberto Bitencourt Nascimento  
📧 phbn181104@gmail.com  

Se precisar de melhorias ou sugestões, entre em contato! 🚀


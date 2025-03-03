# 🐍 Este código está escrito em Python, uma linguagem de programação de alto nível,
# conhecida por sua simplicidade e legibilidade. Python é amplamente utilizado
# para desenvolvimento web, automação, análise de dados, inteligência artificial,
# entre outras áreas.

# 💻 Este código foi escrito numa IDE chamada Visual Studio Code.
# IDE (Integrated Development Environment) é um ambiente de desenvolvimento integrado
# que fornece ferramentas abrangentes para escrever, testar e depurar código.
# Visual Studio Code é uma IDE popular que suporta várias linguagens de programação
# e oferece recursos como destaque de sintaxe, autocompletar, e integração com sistemas de controle de versão.

# 👤 Este código foi escrito e codificado por João Teixeira
# github.com/joaocvteixeira
# linkedin.com/in/joaocvteixeira

# 🎯 Objetivo do código:
# O objetivo deste código é criar um sistema de rolagem de dados para RPG de mesa,
# permitindo ao usuário rolar um dado com um número especificado de lados ou rolar vários dados
# e exibir os resultados no console.

# 📦 Importação do módulo random
# O módulo random fornece funções para gerar números aleatórios.
# Um módulo em Python é um arquivo que contém definições e instruções em Python.
# O módulo random é uma biblioteca padrão do Python que contém várias funções para gerar números aleatórios.
import random

# 🎲 Definição da função rolar_dado
# A palavra-chave 'def' é usada para definir uma função em Python.
# Uma função é um bloco de código que realiza uma tarefa específica e pode ser reutilizado em diferentes partes do programa.

# Esta função rola um dado com o número especificado de lados.
def rolar_dado(lados):
    """
    Rola um dado com o número especificado de lados.
    
    Args:
        lados (int): O número de lados do dado.
        # 'Args' é uma seção da docstring que descreve os parâmetros que a função espera receber.
        # 'lados' é o nome do argumento.
        # '(int)' indica que o argumento deve ser um número inteiro.
        # A descrição explica o que o argumento representa.

    Returns:
        int: O resultado da rolagem do dado.
        # 'Returns' é uma seção da docstring que descreve o valor que a função retorna.
        # 'int' indica que o valor retornado é um número inteiro.
        # A descrição explica o que o valor retornado representa.
    """
    # Uma docstring é uma string literal que aparece logo no início de uma definição de função, método, classe ou módulo.
    # Ela é usada para documentar o propósito e o comportamento do bloco de código onde está inserida.
    # Docstrings são úteis para fornecer informações sobre o código para outros desenvolvedores e para ferramentas de documentação.

    # A função random.randint(1, lados) é usada para simular a rolagem de um dado.
    # Ela gera um número inteiro aleatório entre 1 e o valor de 'lados' (inclusive).
    # Por exemplo, se 'lados' for 6, a função retornará um número entre 1 e 6.
    return random.randint(1, lados)
    # A palavra-chave 'return' é usada para sair de uma função e retornar um valor ao chamador da função.
    # Neste caso, a função retorna o resultado da rolagem do dado.

# 🎱 Definição da função rolar_varios_dados
# Esta função rola vários dados e retorna os resultados em uma lista.
def rolar_varios_dados(quantidade, lados):
    """
    Rola vários dados e retorna os resultados em uma lista.

    Args:
        quantidade (int): O número de dados a serem rolados.
        lados (int): O número de lados de cada dado.
        # 'Args' é uma seção da docstring que descreve os parâmetros que a função espera receber.
        # 'quantidade' e 'lados' são os nomes dos argumentos.
        # '(int)' indica que os argumentos devem ser números inteiros.
        # A descrição explica o que cada argumento representa.

    Returns:
        list: Uma lista com os resultados de cada rolagem de dado.
        # 'Returns' é uma seção da docstring que descreve o valor que a função retorna.
        # 'list' indica que o valor retornado é uma lista.
        # A descrição explica o que o valor retornado representa.
    """
    # Uma docstring é uma string literal que aparece logo no início de uma definição de função, método, classe ou módulo.
    # Ela é usada para documentar o propósito e o comportamento do bloco de código onde está inserida.
    # Docstrings são úteis para fornecer informações sobre o código para outros desenvolvedores e para ferramentas de documentação.

    resultados = []
    
    # O loop 'for' é usado para iterar sobre uma sequência (neste caso, um range).
    # Um loop é uma estrutura de controle que permite repetir um bloco de código várias vezes.
    # O 'for' é um tipo de loop que itera sobre uma sequência de valores.
    # O 'range' é uma função que gera uma sequência de números.
    # O 'in' é usado para verificar a presença de um valor em uma sequência.
    # No contexto do loop 'for', 'in' é usado para iterar sobre cada valor na sequência gerada por 'range'.
    # O '_' é uma convenção para indicar que a variável do loop não será usada.
    for _ in range(quantidade):
        # Adiciona o resultado da rolagem de um dado à lista de resultados.
        resultados.append(rolar_dado(lados))
    return resultados
    # A palavra-chave 'return' é usada para sair de uma função e retornar um valor ao chamador da função.
    # Neste caso, a função retorna uma lista com os resultados de cada rolagem de dado.

# 🔄 Definição da função principal
# Esta função gerencia o sistema de rolagem de dados para RPG de mesa.
def main():
    """
    Função principal que gerencia o sistema de rolagem de dados para RPG de mesa.
    """
    # Um loop é uma estrutura de controle que permite repetir um bloco de código várias vezes.
    # O loop 'while True' cria um loop infinito que só será interrompido por um 'break'.
    # O 'while' é uma estrutura de controle que permite repetir um bloco de código enquanto uma condição for verdadeira.
    # 'True' é uma constante booleana que sempre é verdadeira.
    # Uma booleana é um tipo de dado que pode ter um de dois valores: True (verdadeiro) ou False (falso).
    while True:
        print("\nSistema de Rolagem de Dados para RPG de Mesa")
        print("1. Rolar um dado")
        print("2. Rolar vários dados")
        print("3. Sair")
        # 'print' é uma função que exibe uma mensagem ou valor no console.      
        # A função 'input' é usada para capturar a entrada do usuário.
        # O texto dentro dos parênteses é exibido como um prompt para o usuário.
        # Um 'prompt' é uma mensagem exibida para o usuário, solicitando que ele insira algum dado.
        escolha = input("Escolha uma opção: ")

        # A estrutura 'if' é usada para executar um bloco de código se uma condição for verdadeira.
        # Uma condição é uma expressão que pode ser avaliada como verdadeira ou falsa.
        if escolha == '1':
            # Solicita ao usuário o número de lados do dado
            lados = int(input("Quantos lados tem o dado? "))
            # A função 'int' converte a entrada do usuário (que é uma string) em um número inteiro.
            # 'int' é um tipo de dado em Python que representa números inteiros.
            # Rola o dado e exibe o resultado
            resultado = rolar_dado(lados)
            # A função 'print' é usada para exibir a saída no console.
            # 'print' é uma função que exibe uma mensagem ou valor no console.
            print(f"Você rolou um dado de {lados} lados e obteve: {resultado}")
        # A estrutura 'elif' (else if) é usada para verificar múltiplas condições.
        elif escolha == '2':
            # Solicita ao usuário a quantidade de dados e o número de lados de cada dado
            quantidade = int(input("Quantos dados você quer rolar? "))
            lados = int(input("Quantos lados têm os dados? "))
            # Rola os dados e exibe os resultados
            resultados = rolar_varios_dados(quantidade, lados)
            print(f"Você rolou {quantidade} dados de {lados} lados e obteve: {resultados}")
            # A função 'print' é usada para exibir a saída no console.
        elif escolha == '3':
            # Sai do sistema de rolagem de dados
            print("Saindo do sistema de rolagem de dados. Até a próxima!")
            break
            # A palavra-chave 'break' é usada para sair de um loop.
            # Quando 'break' é executado, ele interrompe o loop imediatamente.
        else:
            # Informa ao usuário que a opção é inválida
            print("Opção inválida. Tente novamente.")
            # A função 'print' é usada para exibir a saída no console.

# 🔄 Ponto de entrada do programa
# A condição 'if __name__ == "__main__":' verifica se o script está sendo executado diretamente (não importado como módulo).
# 'main' é uma convenção para a função principal de um programa. É o ponto de entrada do programa.
if __name__ == "__main__":
    main()
    # A função 'main' é chamada para iniciar o programa.
    # Ela gerencia o sistema de rolagem de dados para RPG de mesa.

# ▶️ Como rodar este código:
# 1. Requer instalar Python:
#    - Acesse o site oficial do Python: https://www.python.org/
#    - Baixe e instale a versão mais recente do Python.
#    - Certifique-se de marcar a opção "Add Python to PATH" durante a instalação.
# 2. Abra o Visual Studio Code.
# 3. Abra o terminal integrado pressionando `Ctrl + `` (Ctrl + acento grave) ou indo em `Terminal` > `Novo Terminal`
#    geralmente encontrado na parte superior da tela.
# 4. Navegue até o diretório onde o arquivo `dados.py` está localizado usando o comando `cd`.
#    Exemplo: cd C:/Users/usuário/OneDrive/Desktop
# 5. Execute o código Python usando o comando `python` seguido do nome do arquivo.
#    Exemplo: python dados.py
# 6. Interaja com o programa escolhendo uma das opções do menu.
# 7. Veja os resultados exibidos no console.
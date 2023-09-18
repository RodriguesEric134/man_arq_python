import csv

# Função para exibir informações com base na escolha do usuário
def exibir_informacoes(escolha):
    with open('d:/filmes.csv', 'r', encoding='utf-8', newline='') as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)  # Lê a primeira linha (cabeçalho)

        # Determina o índice da coluna com base na escolha do usuário
        coluna_index = opcoes_menu[escolha]

        print(f"Filmes por {escolha}:")
        for linha in csv_reader:
            print(linha[coluna_index])

# Dicionário que mapeia opções do menu para funções
opcoes_menu = {
    "1": "titulo",
    "2": "diretor",
    "3": "genero",
}

# Loop principal
while True:
    print("\nEscolha uma opção:")
    print("1. Exibir filmes por título")
    print("2. Exibir filmes por diretor")
    print("3. Exibir filmes por gênero")
    print("4. Sair")

    opcao = input("Digite o número da opção: ")

    if opcao == "4":
        break
    elif opcao in opcoes_menu:
        escolha = opcoes_menu[opcao]
        exibir_informacoes(escolha)
    else:
        print("Opção inválida. Tente novamente.")

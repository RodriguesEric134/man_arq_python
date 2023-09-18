#rm550249
#Eric de Carvalho Rodrigues
import csv
continua = "sim"
categorias = [
    ['titulo', 'genero', 'duração', 'classificação_indicativa', 'diretor']
]

    
with open('d:/filmes.csv', 'a', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    while True:
        print("Programa para adicionar filmes")
        titulo = input("digite o título: ")
        genero = input("digite o gênero: ")
        duração = input("digite a duração: ")
        classificacao = input("digite a classificação: ")
        diretor = input("digite o nome do diretor: ")

        csv_writer.writerow([titulo, genero, duração, classificacao, diretor])

        continua = input("Deseja adicionar outro filme? (sim/não): ").lower()
        if continua != "sim":
            break

print("filmes adicionados com sucesso!")
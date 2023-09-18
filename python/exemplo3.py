import csv
novos_dados = [
    ['Marcelo', 'mdias', 'senha', '49', '07977457857'],
    ['Beatriz', 'bia', 'lipe000', '48', '16680679869']
]
with open('d:/usuarios.csv', 'a', encoding='utf-8', newline='') as f:
    escreve_csv = csv.writer(f) 
    for i in novos_dados:
        escreve_csv.writerow(i)
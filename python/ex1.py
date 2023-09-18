# rm98832 matheus zanardi

import csv

filmes = []


print('casdastre os filmes')

resp = input('gostaria de cadastrar um filme?(sim/não) ').lower()

while resp == 'sim':

    nome  = input('digite o nome do filme: ')

    genero  = input('digite o genero do filme: ')

    duracao  = input('digite a duração do filme: ')

    censura = input('digite a censura do filme:')

    diretor = input('digite o nome do diretor do filme')

  
    

    filmes.append(nome)
    filmes.append(genero)
    filmes.append(duracao)
    filmes.append(diretor)
    

    with open(f'd:/filmes.csv', 'w')as arquivo:
        escreve_csv = csv.writer(arquivo)
        escreve_csv.writerow(filmes)


   
    resp = input('gostaria de cadastrar mais um usuario?(sim/não) ').lower()




import csv

print('escolha por qual fator você quer procurar um filme disponivel:')
print('(1)nome')
print('(2)genero')
print('(3)nome do diretor do filme')
resp = int(input('escolha um categoria; '))


with open(f'd:/filmes.csv', 'r')as arquivo:
    filmes = csv.reader(arquivo)
    

    if resp == 1:
        print('digite o nome do filme que deseja buscar')
        nome__filme = input(':')
        for i in filmes:
            if  i[0] == nome__filme:
                print(i)
            

    elif resp == 2:
        print('digite o nome do genero do fime')
        genero = input(':')
        for i in filmes:
            if genero == i[1]:
                print(i)
            

    elif resp == 3:
        print('digite o nome do firetor')
        nome__diretor = input(':')
        for i in filmes:
            if nome__diretor == i[4]:
                print(i)
            
    
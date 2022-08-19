import random

print('>>> SORTEIO <<<')
aluno1 = str(input('Nome do 1º aluno: '))
aluno2 = str(input('Nome do 2º aluno: '))
aluno3 = str(input('Nome do 3º aluno: '))
aluno4 = str(input('Nome do 4º aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)

print('O aluno sorteado foi {} !!!!'.format(sorteio.upper()))
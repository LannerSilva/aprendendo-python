from operator import itemgetter
from random import randint
from time import sleep

print(' DESAFIO 91')
print(' Crie um programa onde \33[33m4 jogadores\33[m joguem um \33[34mdado\33[m e tenham resultados \33[34maleatórios\33[m.\n'
      'Guarde esses resultados em um \33[33mdicionário\33[m em Python. No final, coloque esse dicionário em \33[33mordem\33[m,\n'
      'sabendo que o \33[34mvencedor\33[m tirou o \33[33mmaior número\33[m no dado.')
print('\33[34m==\33[m' * 50)
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('\33[34m==\33[m' *50)
print('\33[36m============================================== RANKING ==============================================\33[m')
for i, v in enumerate(ranking):
    print(f'{i+1}º \33[34mlugar\33[m: {v[0]} com {v[1]}.')
    sleep(1)


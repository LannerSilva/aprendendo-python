#BIBLIOTECA
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor  % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')




print('       \33[1:4:34mDESAFIO 100 - Funções para sortear e somar\33[m.')
print('Um programa que tenha uma \33[1:34mlista\33[m chamada \33[1:33mnúmeros\33[m e \33[1:34mduas funções\33[m chamadas \33[1:33msorteia()\33[m e \33[1:33msomaPar()\33[m.\n'
      'A primeira função vai sortear \33[1:34m5 números\33[m e vai colocá-los dentro da lista e a segunda função vai\n'
      'mostrar a \33[1:34msoma\33[m entre todos os valores \33[1:33mPARES\33[m sorteados pela função anterior.')
print()
# PROGRAMA PRINCIPAL
numeros = list()
sorteia(numeros)
somaPar(numeros)

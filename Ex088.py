from random import randint
from time import sleep
lista = list()
jogos = list()
print('\33[34mDESAFIO 88\33[m')
print('Faça um programa que ajude um jogador da \33[32mMEGA SENA\33[m a criar palpites.\n'
      'O programa vai perguntar quantos jogos serão gerados e vai sortear \33[32m6 números\33[m entre 1 e 60 para cada jogo,\n'
      'cadastrando tudo em uma lista composta.')
print('\33[36m=\33[m' * 40)
print('     JOGO PARA MEGA SENA')
print('\33[36m=\33[m' * 40)
quant = int(input('Quantos jogos você quer jogar? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=' * 10, f'SORTEANDO {quant} JOGOS', '=' * 10)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('=' * 12, '<-< BOA SORTE! >->', '=' * 12)

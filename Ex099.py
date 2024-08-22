from time import sleep

def maior( * núm):
    cont = maior = 0
    print('==' * 30)
    print('\33[1:35mAnalisando os valores passados...\33[m ')
    for valor in núm:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

print('\33[1:4:36mDESAFIO 99\33[m')
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
# programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
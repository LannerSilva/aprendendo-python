def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O numeor a ser calculado.
    :param show: (opcional) Mostrar ou  não a conta.
    :return: O valor do Fatorial de um Número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#Exercicio do  Curso em video???
print('\33[1:4:34mDESAFIO 102 - Função para Fatorial\33[m\n'
      'Crie um programa que tenha uma \33[1:34mfunção\33[m \33[1:33mfatorial()\33[m que receba dois parâmetros: o primeiro que indique o \33[1:34mnúmero\33[m\n'
      'a calcular e outro chamado \33[1:34mshow\33[m, que será um valor \33[1:34mlógico\33[m\33[1:33m(opcional)\33[m indicando se será mostrado ou não na tela\n'
      'o processo de cálculo do fatorial.')
# Programa Principal
num = int(input('Digite um valor: '))
print(fatorial(num, show=True))
help(fatorial)
def lin():
    print('\33[31m==\33[m' * 40)
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')



print('DESAFIO 96')
lin()
print('Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular\n'
      '(largura e comprimento) e mostre a área do terreno.')
lin()
#progama principal
print(' Controle de Terrenos')
lin()
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
lin()
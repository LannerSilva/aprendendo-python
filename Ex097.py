def lin():
    print('\33[31m==\33[m' * 40)
def escreva(msg):
    tam = len(msg) + 2
    print('~' * tam)
    print(f'{msg}')
    print('~' * tam)


lin()
print('DESAFIO 97')
print('Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro\n'
      'e mostre uma mensagem com tamanho adaptável.')
lin()
escreva('Lanner Silva')
escreva('Curso de Python')
escreva('CeV')
escreva('Olá, Mundo!')


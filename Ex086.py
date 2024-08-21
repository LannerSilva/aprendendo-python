print('\33[34mDESAFIO 86\33[m')
print('Crie um programa que declare uma \33[31mmatriz\33[m de \33[34mdimensão 3×3\33[m e preencha com valores lidos pelo teclado.\n'
      'No final, mostre a \33[31mmatriz\33[m na tela, com a formatação correta.')
print('-=' * 30)
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
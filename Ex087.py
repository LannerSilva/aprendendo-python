print('\33[34mDESAFIO 87\33[m')
print(' Aprimore o \33[34mdesafio anterior\33[m, mostrando no final:\n'
      '     \33[34mA)\33[m A \33[34msoma\33[m de todos os \33[31mvalores pares\33[m digitados.\n'
      '     \33[34mB)\33[m A \33[34msoma\33[m dos valores da \33[31mterceira coluna\33[m.\n'
      '     \33[34mC)\33[m O \33[34mmaior\33[m valor da \33[31msegunda linha\33[m.')
print('-=' * 30)
matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para: \33[36m[\33[m{l}, {c}\33[36m]\33[m: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'\33[36m[\33[m{matriz[l][c]:^5}\33[36m]\33[m', end='')
        if matriz[l][c] % 2 ==0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é \33[34m{spar}\33[m.')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma do valores da terceira coluna é \33[34m{scol}\33[m.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é \33[34m{mai}\33[m')

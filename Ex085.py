print('\033[34mDESAFIO 85\033[m')
print(' Crie um programa onde o usuário possa digitar \033[34msete valores numéricos\033[m e cadastre-os em uma \33[31mlista\n'
      ' única\33[m que mantenha separados os valores \33[34mpares\33[m e \33[34mímpares\33[m.\n'
      ' No final, mostre os valores pares e ímpares em ordem \33[31mcrescente\33[m.')
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 40)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
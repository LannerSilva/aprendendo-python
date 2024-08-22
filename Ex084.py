print('DESAFIO 84')
print('Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:\n'
      'A) Quantas pessoas foram cadastradas.\n'
      'B) Uma listagem com as pessoas mais pesadas.\n'
      'C) Uma listagem com as pessoas mais leves.')
temp =[]
princ = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    princ.append(temp[:])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Os dados foram {princ}')
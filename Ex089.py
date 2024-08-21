print('\33[34mDESAFIO 89\33[m')
print('Crie um programa que leia \33[34mnome\33[m e \33[34mduas\33[m notas de vários alunos e guarde tudo em uma \33[31mlista composta\33[m.\n'
      'No final, mostre um \33[34mboletim\33[m contendo a \33[31mmédia\33[m de cada um e permita que o usuário possa mostrar\n'
      'as \33[34mnotas\33[m de cada aluno individualmente.')

ficha = list()
while True:
      nome = str(input('Nome: '))
      nota1 = float(input('Nota 1: '))
      nota2 = float(input('Nota 2: '))
      media = (nota1 + nota2) / 2
      ficha.append([nome, [nota1, nota2], media])
      resp = str(input('Quer continuar? [S/N]'))
      if resp in 'Nn':
            break
print('--' * 35)
print(f'{"No.":<4}{"NOME":<10}{"MÈDIA":>8}')
print('--' * 35)
for i, a in enumerate(ficha):
      print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
      print('--' * 35)
      opc = int(input(' Mostrar notas de qual aluno? (999 interrompe):'))
      if opc == 999:
            print('FINALIZADO...')
            break
      if opc <= len(ficha) -1:
            print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

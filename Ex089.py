print('\33[34mDESAFIO 90\33[m')
print(' Faça um programa que leia \33[34mnome e média\33[m de um aluno, guardando também a \33[34msituação\33[m em um \33[31mdicionário\33[m.\n'
      'No final, mostre o conteúdo da estrutura na tela.')
aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('--' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')

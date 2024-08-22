print('DESAFIO 94')
print('\33[32m---\33[m' * 38)
print('Crie um programa que leia \33[1:34mnome\33[m, \33[1:34msexo\33[m e \33[1:34midade\33[m de \33[1:33mvárias pessoas\33[m, guardando os dados de cada pessoa em um \33[1:33mdicionário\33[m\n'
      'e todos os dicionários em uma \33[1:33mlista\33[m. No final, mostre:\n'
      '\33[1:34mA)\33[m Quantas pessoas foram cadastradas\n'
      '\33[1:34mB)\33[m A \33[1:33mmédia\33[m de idade\n'
      '\33[1:34mC)\33[m Uma lista com as \33[1:33mmulheres\33[m\n'
      '\33[1:34mD)\33[m Uma lista de pessoas com \33[1:33midade\33[m acima da \33[1:33mmédia\33[m')
print('\33[32m---\33[m' * 38)
print(' \33[36m-\33[m \33[1:4:36mUnindo Dicionários e Listas\33[m')
print('')
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas \33[1:36mM\33[m ou \33[1:36mF\33[m.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos')
print('As mulheres cadastradas foram ',end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('       ',end='')
        for k, v in p.items():
            print(f'{k} = {v}:',end='')
        print()
print('< < \33[1:34mENCERRADO\33[m > >')
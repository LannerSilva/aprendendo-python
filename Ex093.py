print('Desafio 93')
print(' Crie um programa que gerencie o aproveitamento de um \33[33mjogador de futebol\33[m.\n'
      'O programa vai ler o \33[34mnome do jogador\33[m e \33[34mquantas partidas\33[m ele jogou.\n'
      'Depois vai ler a \33[34mquantidade de gols\33[m feitos em \33[33mcada partida\33[m.\n'
      'No final, tudo isso será guardado em um \33[33mdicionário\33[m, incluindo o \33[34mtotal de gols\33[m feitos durante o campeonato.')
print('=' * 110)
print('')
print('\33[34m == CADASTRO DE JOGADOR DE FUTEBOL ==\33[m ')

jogador = dict()
partidas =  list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na {c+1}ª partida? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-' * 30)
print(jogador)
print('-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor de {v}')
print('-' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
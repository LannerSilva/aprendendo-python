print('\33[1:34mDESAFIO 95\33[m')
print('')
print('Aprimore o desafio 93 para que ele funcione com vários jogadores,\n'
      'incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.')
print('\33[1:33m===\33[m' * 30)
jogador = dict()
partidas =  list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na {c+1}ª partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'* 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca =  int(input('Mostrar dados de qual jogador? (999 interrompe): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe este jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<<< VOLTE SEMPRE >>>')

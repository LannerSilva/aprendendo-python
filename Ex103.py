def ficha(jog, gol):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


print('\n\33[1:4:32mDESAFIO 103 - Ficha do Jogador\33[m \n'
      'Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:\n'
      'o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,\n'
      'mesmo que algum dado não tenha sido informado corretamente.')
print('===' * 40)
# Programa principal
n = str(input("Nome do jogador: "))
g = str(input("Número de gols:"))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

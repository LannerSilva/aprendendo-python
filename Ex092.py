from datetime import datetime
print('DESAFIO 92')
print('-' * 40)
print(' Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.\n'
      'Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.\n'
      'Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.')
print('-' * 40)
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano da Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35)- datetime.now().year)
print('-' * 40)
for k, v in dados.items():
    print(f' - {k} será com {v}')
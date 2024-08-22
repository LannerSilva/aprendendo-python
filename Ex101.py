def voto(ano):
    from datetime import date
    atual =date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: \33[1:31mNÂO VOTA\33[m.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: \33[1:33mVOTO OPCIONAL\33[m.'
    else:
        return f'Com {idade} anos: \33[1:34mVOTO OBRIGATORIO\33[m.'


print('\33[1:34mDESAFIO 101 - Funções para votação?\33[m')
print('Crie um programa que tenha uma \33[1:34mfunção\33[m chamada \33[1:33mvoto()\33[m que vai receber como \33[1:34mparâmetro\33[m o \33[1:33mano de nascimento\33[m de uma pessoa,\n'
      '\33[1:34mretornando\33[m um valor \33[1:34mliteral\33[m indicando se uma pessoa tem voto \33[1:33mNEGADO\33[m, \33[1:33mOPCIONAL\33[m e \33[1:33mOBRIGATÓRIO\33[m nas eleições.')
print('====' * 30)
#programa principal
nasc = int(input('Digite o ano de nascimento: '))
print(voto(nasc))
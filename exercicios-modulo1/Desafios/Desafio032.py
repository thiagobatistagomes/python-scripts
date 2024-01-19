# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
print('====== Desafio 32 ======')
ano = int(input('Digite o ano: '))
print('Analisando se {} é um ano bissexto...'.format(ano))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano bissexto!')
else:
    print('O ano não é bissexto!')

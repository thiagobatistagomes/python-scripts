# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
print('====== Desafio 32 ======')
from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
print('Analisando se {} é um ano BISSEXTO...'.format(ano))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano BISSEXTO!')
else:
    print('O ano não é BISSEXTO')
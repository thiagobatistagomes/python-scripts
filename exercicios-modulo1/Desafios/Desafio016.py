# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira. Ex: 6.127 tem a parte inteira 6
from math import trunc
print('====== DESAFIO 16 ======')
n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(n, trunc(n)))
# print('O número {} tem a parte inteira {}.'.format(n, int(num)))

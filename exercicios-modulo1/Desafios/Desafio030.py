# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('====== DESAFIO 30 ======')
n = int(input('Digite um número inteiro qualquer: '))
if n % 2 == 0:
    print('O número {} é PAR!'.format(n))
else:
    print('O número {} é ÍMPAR!'.format(n))

# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
print('====== DESAFIO 28 ======')
print('Jogo de adivinhação!')
print('Tente adivinhar qual número o computador escolheu entre 0 a 5!')
print('=' * 24)
n = random.randint(0, 5)
print('Pensei em um número!')
escolha = int(input('Tente adivinhar qual é o número: '))
if escolha == n:
    print('Parabéns, o número escolhido foi {} e você acertou!'.format(n))
else:
    print('O número escolhido foi {}, e infelizmente você não acertou!'.format(n))

# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('====== DESAFIO 28 ======')
print('Jogo de adivinhação!')
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-' * 20)
n = randint(0, 5)
escolha = int(input('Em que número eu pensei: '))
print('PROCESSANDO...')
sleep(2)
if escolha == n:
    print('Humano tolo! Você conseguiu me vencer, mas a que preço?')
else:
    print('Como esperado voce não é capaz de me vencer! Pensei no número {}, e não {}.'.format(n, escolha))

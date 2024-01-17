# Faça um programa que leia de 0 a 9999 e mostre na tela cada um dos dígitos separados. Ex: Digite um número: 1834 Unidade:4, Dezena:3, Centena:8, Milhar:1.
print('====== DESAFIO 23 ======')
n = int(input('Digite um número qualquer entre 1 e 1999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando o número {}'.format(n))
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u, d, c, m))

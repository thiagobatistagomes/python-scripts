# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
print('====== DESAFIO 18 ======')
angulo = float(input('Digite o valor do ângulo: '))
rad = radians(angulo)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)
print('O seno de {}° é: {:.2f}\nO cosseno de {}° é: {:.2f}\nA tangente de {}° é: {:.2f}'.format(angulo, seno, angulo, cosseno, angulo, tangente))

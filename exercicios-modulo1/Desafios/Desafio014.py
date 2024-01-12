# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit
print('====== DESAFIO 14 ======')
c = float(input('Qual temperatura em Celsius deseja converter para Fahrenheit? '))
f = (c * 9/5) + 32
print('{}°C é igual a {:.1f}°F'.format(c, f))

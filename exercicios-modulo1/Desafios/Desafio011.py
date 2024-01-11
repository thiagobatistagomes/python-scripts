# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-la sabendo que  cada litro de tinta, pinta uma área de 2 metros quadrados.
print('====== DESAFIO 11 ======')
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print('Area da parede: {} Metros quadrados\nQtd de tinta necessária: {} litros.'.format(area, tinta))

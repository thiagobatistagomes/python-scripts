# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.
# import math (se importar a biblioteca math, é possivel usar o método sqrt() para calcular a raiz quadrada

print('====== DESAFIO 06 ======')
n = int(input('Digite um numero inteiro: '))
print('Dobro: {}\nTriplo: {}\nRaiz Quadrada: {:.2f}'.format((n * 2), (n * 3), (n ** (1/2))))

#print('Dobro: {}\nTriplo: {}\nRaiz Quadrada: {}'.format(n * 2, n * 3, math.sqrt(n)))
#print('Dobro: {}\nTriplo: {}\nRaiz Quadrada: {:.2f}'.format((n * 2), (n * 3), pow(n, 1/2)))
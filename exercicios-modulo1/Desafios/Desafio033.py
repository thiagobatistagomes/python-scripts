# Faça um programa que leia três números e mostre qual é o menor e qual é o maior.
print('====== DESAFIO 33 ======')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1 < n2 and n1 < n3:
    print('Menor: {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('Menor: {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('Menor: {}'.format(n3))  
if n1 > n2 and n1 > n3:
    print('Maior: {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('Maior: {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('Maior: {}'.format(n3))

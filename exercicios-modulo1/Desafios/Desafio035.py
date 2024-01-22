# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('====== DESAFIO 035 ======')
print('-=-' * 12)
print('Analisador de Triângulos')
print('-=-' * 12)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and b + c > a and a + c > b:
    print('Os segmentos podem formar um triângulo!')
else:
    print('Os segmentos não formam um triângulo!')

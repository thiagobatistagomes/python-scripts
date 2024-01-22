# Desenvolva um programa que pergunte a distância de uma viagem em Kms. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
print('====== DESAFIO 31 ======')
from time import sleep
distancia = int(input('Digite a distância da sua viagem em Kms: '))
print('Calculando o preço da passagem...')
sleep(2)
if distancia <= 200:
    print('Valor da passagem: R${:.2f}.'.format(distancia * 0.5))
else:
    print('Valor da passagem: R${:.2f}.'.format(distancia * 0.45))

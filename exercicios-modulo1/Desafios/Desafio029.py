# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
print('=' * 6, 'Desafio 29', '=' * 6)
vel = int(input('Digite a velocidade do carro: '))
if vel > 80:
    print('Voce foi multado!\nValor da multa: R${}.'.format((vel - 80) * 7))

# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
print('=' * 6, 'Desafio 29', '=' * 6)
vel = int(input('Digite a velocidade atual do carro: '))
if vel > 80:
    print('Voce foi multado por exceder o limite de velocidade de 80Km/h!\nValor da multa: R${:.2f}.'.format((vel - 80) * 7))
print('Tenha um bom dia! Dirija com segurança!')

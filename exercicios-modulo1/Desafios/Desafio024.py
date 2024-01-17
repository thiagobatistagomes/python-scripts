# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
print('====== DESAFIO 24 ======')
cidade = str(input('Digite o nome da cidade: ')).strip()
print('Analisando se {} começa ou não com Santo: '.format(cidade))
cidade = cidade.capitalize()
print('{}'.format('Santo' in cidade))
# outra solução: print(cidade[:5].capitalize() == 'Santo')

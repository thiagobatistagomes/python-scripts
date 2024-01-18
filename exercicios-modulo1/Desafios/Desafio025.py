# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
print('====== DESAFIO 25 ======')
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando se {} tem Silva...'.format(nome))
print('{}'.format('SILVA' in nome.upper()))

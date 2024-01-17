# Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas, o nome com todas as letras minúsculas, quantas letras ao todo(sem considerar espaços), quantas letras tem o primeiro nome.
print('====== DESAFIO 22 ======')
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas: {}\nSeu nome em minúsculas: {}'.format(nome.upper(),nome.lower(),len(nome)))
lista = nome.split()
qtdLetras = ''.join(lista)
print('Seu nome tem ao todo: {} letras.\nSeu primeiro nome é {} e ele tem {} letras.'.format(len(qtdLetras), lista[0], len(lista[0])))
# outra forma de contar as letras sem considerar espaços e sem usar lista é:
# len(nome) - nome.count(' ')
# outra forma de descobrir quantas letras tem o primeiro nome é:
# nome.find(' ')

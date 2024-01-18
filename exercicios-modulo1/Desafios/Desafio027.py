# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. Ex: Ana Maria de Souza, primeiro: Ana, último = Souza
print('====== DESAFIO 27 ======')
nome = str(input('Digite seu nome: ')).strip()
lista = nome.split()
print('Primeiro: {}\nÚltimo: {}'.format(lista[0], lista[len(lista) - 1]))

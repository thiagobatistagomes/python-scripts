# Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
print('====== DESAFIO 13 ======')
salario = float(input('Digite o valor do salário: R$'))
novoSalario = salario + (salario * 0.15)
print('Salário com 15% de aumento: R${:.2f}'.format(novoSalario))

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00 calcule um aumento de 10%. Para os inferiores ou iguais o aumento é de 15%.
print('====== DESAFIO 34 ======')
salario = float(input('Digite seu salário: '))
if salario <= 1250:
    print('Seu novo salário é: R${:.2f}'.format(salario + (salario * 0.15)))
else:
    print('Seu novo salário é: R${:.2f}'.format(salario + (salario * 0.1)))

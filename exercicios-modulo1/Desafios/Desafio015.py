#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('====== DESADIO 15 ======')
dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
preco = (60 * dias) + (0.15 * km)
print('O total a pagar é de R${:.2f}'.format(preco))

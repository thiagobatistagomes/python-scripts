# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
print('====== DESAFIO 12 ======')
preco = float(input('Digite o preco do produto: R$'))
desconto = preco - preco * 0.05
print('Preço com 5% de desconto: R${:.2f}'.format(desconto))

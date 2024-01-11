# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considerando US$ 1,00 = R$ 4,88
print('====== DESAFIO 10 ======')
n = float(input('Quanto dinheiro você tem disponível em R$? '))
print('Você pode comprar até {:.2f} dólares.'.format(n / 4.88))

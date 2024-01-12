# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considerando US$ 1,00 = R$ 4,88 e € 1,00 = R$ 5,32
print('====== DESAFIO 10 ======')
n = float(input('Quanto dinheiro você tem disponível em R$? '))
print('Você pode comprar até {:.2f} dólares.\nVocê pode comprar até {:.2f} euros.'.format(n / 4.88, n / 5.32))

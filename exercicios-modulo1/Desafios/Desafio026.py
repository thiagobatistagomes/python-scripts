# Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A", Em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
print('====== DESAFIO 26 ======')
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na {}ª posição.'.format(frase.find('A') + 1))
print('A letra "A" aparece pela última vez na {}ª posição.'.format(frase.rfind('A') + 1))

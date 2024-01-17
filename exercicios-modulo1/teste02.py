frase = 'Fui ao norte em busca de Ouro.'
print('Fatiamento: {}\nComprimento: {}\nQtd de Os: {}\n{}\n{}'.format(frase[7:], len(frase), frase.count('o'), frase.find('nor'), 'norte' in frase))
# transformação
print(frase.replace('ouro','prata'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
# divisão
lista = frase.split()
print(lista)
frase = ' '.join(lista)
print(frase)

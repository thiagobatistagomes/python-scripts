nome = str(input('Digite seu nome completo: ')).strip()
if 'Thiago' in nome and 'Batista' in nome and 'Gomes' in nome:
    print('Prazer em te ver novamente, mestre!')
    mestre = 1
else:
    print('Você é apenas um cidadão comum!')
    mestre = 0
print('Bom dia, {}!'.format(nome))
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
if m >= 6 and mestre:
    print('Parabéns mestre, sua média é {} e você passou!'.format(m))
if m >= 6 and mestre == 0:
    print('Parabéns {}, sua média é {} e você passou! Porém meu mestre tirou nota maior!'.format(nome, m))
if m < 6 and mestre:
    print('Impossível, você deve ser um impostor. Meu mestre jamais tiraria {}! Reprovado!'.format(m))
if m < 6 and mestre == 0:
    print('Sinto muito {}, sua média é {}, e você não conseguiu nota suficiente para passar!'.format(nome, m))    

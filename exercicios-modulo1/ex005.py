larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {} X {} e sua área é de {}M².'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede você precisará de {}l de tinta.'.format(tinta))

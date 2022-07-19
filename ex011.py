largura = float(input('-> Informe a largura da parede: '))
altura = float(input('-> Informe a altura da parede: '))

area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {}m x {}m e sua área é de {}m²...'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
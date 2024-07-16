l = float(input('Qual a largura da parede?'))
a = float(input('Qual a altura da parede?'))
c = l*a
print('A parede possui dimensões de {}x{} e sua área é de {}m²'. format(l,a,c,))
t = c/2
print('Para pintar essa parede você precisará de {:.1f}L de tinta'.format(t))
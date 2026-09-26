altura = float(input("Qual a altura da parede? "))
largura = float(input("Qual a largura da parede? "))
demaos = int(input("Quantas demãos dará? "))

area = altura * largura
rendimento = 2
tinta = (area * demaos) / rendimento

print("Sua parede tem {}m² e você precisará de {:.1f} litros de tinta aplicando {} demão(s)."
      .format(area, tinta, demaos))
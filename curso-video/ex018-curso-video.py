from math import sin, cos, tan, radians

angulo = int(input("Qual o ângulo? "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("O seno será: {:.2f}; o cosseno será: {:.2f}; e a tangente será: {:.2f}"
      .format(seno, cosseno, tangente))

print("="* 40)


#fazendo sem biblioteca
angulo = int(input("Qual o ângulo? "))

pi = 3.141592653589793
radianos = angulo * pi / 180
seno = radianos - (radianos ** 3) / 6
cosseno = 1 - (radianos ** 2) / 2
tangente = radianos + (radianos ** 3) / 3

print("O seno será {:.2f}; o cosseno será {:.2f}; e a tangente será: {:.2f}"
      .format(seno, cosseno, tangente))
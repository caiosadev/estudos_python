from math import hypot #hypot faz o cálculo da hipotenusa

cateto_oposto = int(input("Qual cumprimento do cateto oposto? "))
cateto_adjacente = int(input("Qual cumprimento do cateto adjacente? "))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print("A hipotenusa vai medir: {:.2f}" .format(hipotenusa))


#solução matemática sem a biblioteca
cateto_oposto = int(input("Qual cumprimento do cateto oposto? "))
cateto_adjacente = int(input("Qual cumprimento do cateto adjacente? "))

hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

print("A hipotenusa vai medir: {:.2f}" .format(hipotenusa))
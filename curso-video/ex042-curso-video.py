reta1 = float(input('Cumprimento da reta 1: '))
reta2 = float(input('Cuprimento da reta 2: '))
reta3 = float(input('Cumprimento da reta 3: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('As retas podem formar um triângulo.')
    
    if reta1 == reta2 == reta3:
        print('E o triângulo formado é equilátero.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
            print('E o triângulo formado é isóceles')
    else:
                print('E o triângulo formado é escaleno.')
else:
    print('As retas não podem formar um triângulo.')